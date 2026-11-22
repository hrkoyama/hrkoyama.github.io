// Local, precomputed data only. Importing this module never starts playback.
const widgets = new WeakMap();
const documents = new WeakMap();
const seriesKeys = ['damping_only', 'dispersion_only', 'lax_wendroff'];
const colors = ['#a24722', '#326c94', '#67509b'];
let nextId = 0;

const copy = {
  en: {
    title: 'One wave, three kinds of evolution',
    intro: 'All panels start from the same periodic pulse and use the same time and axes. The wave wraps around at the domain boundary.',
    loading: 'Loading the local wave data…',
    ready: 'Ready. Playback starts only when you press Play.',
    unavailable: 'The playback could not load. The static comparison remains available.',
    play: 'Play', pause: 'Pause', reset: 'Reset',
    position: 'Time step', exact: 'Exact translation · dashed black',
    numerical: 'Panel result · solid color',
    time: 'Time', step: 'step', period: 'T = L / |a|',
    note: 'Use the slider with the arrow keys, Home, or End. Playback stops at the last frame. A is a constructed diagnostic isolating damping; B evolves the semidiscrete equation exactly in time; C is a fully discrete method.',
    reduced: 'Reduced motion is enabled: playback advances more slowly. The slider also works without animation.',
    paused: 'Paused.', playing: 'Playing.', finished: 'Reached the last frame.',
    hidden: 'Paused because the page is hidden.', resetDone: 'Reset to the initial wave.',
    minimum: 'min', maximum: 'max', error: 'relative L² error', norm: 'discrete L² / initial',
    exactRange: 'Exact wave',
    panels: [
      ['A · Damping only', 'Constructed diagnostic: upwind damping with exact Fourier phases.'],
      ['B · Dispersion only', 'Centered spatial derivative, evolved exactly in time: |G| = 1.'],
      ['C · Lax–Wendroff', 'Actual fully discrete update: damping and dispersion occur together.'],
    ],
  },
  ja: {
    title: '同じ波を、3通りの時間発展で比べる',
    intro: '全パネルで初期の周期パルス・時刻・座標軸をそろえています。波は領域の端から反対側へ回り込みます。',
    loading: 'ローカルの波形データを読み込んでいます…',
    ready: '準備できました。「再生」を押すと時間発展が始まります。',
    unavailable: '再生データを読み込めませんでした。静止図で比較できます。',
    play: '再生', pause: '一時停止', reset: '最初に戻す',
    position: '時間ステップ', exact: '厳密な移流 · 黒の破線',
    numerical: '各パネルの結果 · 色の実線',
    time: '時刻', step: 'ステップ', period: 'T = L / |a|',
    note: 'スライダーは矢印キー・Home・Endで操作できます。再生は最終フレームで止まります。Aは減衰だけを取り出す診断用の構成、Bは半離散式の厳密な時間発展、Cは完全離散化した手法です。',
    reduced: '動きを減らす設定が有効なため、再生をゆっくり進めます。スライダーならアニメーションなしで比較できます。',
    paused: '一時停止しました。', playing: '再生中です。', finished: '最終フレームに到達しました。',
    hidden: 'ページが非表示になったため、一時停止しました。', resetDone: '初期の波形に戻しました。',
    minimum: '最小値', maximum: '最大値', error: '相対L²誤差', norm: '離散L² / 初期値',
    exactRange: '厳密解',
    panels: [
      ['A · 振幅の減衰だけ', '診断用の構成：風上差分の減衰率と、厳密なフーリエ位相を組み合わせる。'],
      ['B · 位相の分散だけ', '空間の中心差分を時間方向に厳密に発展させる。|G| = 1。'],
      ['C · Lax–Wendroff法', '実際の完全離散化：振幅の減衰と位相の分散が同時に生じる。'],
    ],
  },
};

const finiteArray = values => Array.isArray(values) && values.every(Number.isFinite);

/** Reject incomplete or inconsistent assets before drawing a misleading plot. */
export function validateWaveEvolutionData(data) {
  const invalid = () => { throw new Error('Invalid wave-evolution data'); };
  if (!data || data.schema_version !== 1 || !data.parameters) invalid();
  const {x, steps, time, series, parameters, y_limits: bounds} = data;
  const domain = parameters.domain;
  if (!finiteArray(domain) || domain.length !== 2 || domain[0] >= domain[1]) invalid();
  if (!finiteArray(bounds) || bounds.length !== 2 || bounds[0] >= bounds[1]) invalid();
  if (!Number.isFinite(parameters.dt) || parameters.dt <= 0 || !Number.isFinite(parameters.advection_speed)) invalid();
  if (!finiteArray(x) || x.length < 3 || parameters.n !== x.length) invalid();
  if (x.some((value, i) => value < domain[0] || value >= domain[1] || (i && value <= x[i - 1]))) invalid();
  if (!finiteArray(steps) || steps.length < 2 || steps[0] !== 0 || steps.some((value, i) => !Number.isInteger(value) || (i && value <= steps[i - 1]))) invalid();
  if (!finiteArray(time) || time.length !== steps.length || time[0] !== 0 || time.some((value, i) => (i && value <= time[i - 1]) || Math.abs(value - steps[i] * parameters.dt) > 1e-6)) invalid();
  for (const key of ['exact', ...seriesKeys]) {
    const frames = series?.[key];
    if (!Array.isArray(frames) || frames.length !== steps.length) invalid();
    for (const frame of frames) {
      if (!finiteArray(frame) || frame.length !== x.length || frame.some(value => value < bounds[0] - 1e-6 || value > bounds[1] + 1e-6)) invalid();
    }
  }
  return data;
}

/** Discrete sample metrics provide a readable counterpart to each canvas. */
export function waveFrameStatistics(data, key, frameIndex) {
  const values = data.series[key]?.[frameIndex];
  const exact = data.series.exact[frameIndex];
  if (!values || !exact) throw new RangeError('Unknown wave frame');
  let minimum = Infinity, maximum = -Infinity, errorSquared = 0, exactSquared = 0, normSquared = 0, initialSquared = 0;
  for (let j = 0; j < values.length; j++) {
    minimum = Math.min(minimum, values[j]);
    maximum = Math.max(maximum, values[j]);
    errorSquared += (values[j] - exact[j]) ** 2;
    exactSquared += exact[j] ** 2;
    normSquared += values[j] ** 2;
    initialSquared += data.series[key][0][j] ** 2;
  }
  return {
    minimum, maximum,
    relativeL2: Math.sqrt(errorSquared / (exactSquared || 1)),
    l2Ratio: initialSquared ? Math.sqrt(normSquared / initialSquared) : normSquared ? Infinity : 1,
  };
}

function registryFor(doc) {
  let registry = documents.get(doc);
  if (registry) return registry;
  const view = doc.defaultView;
  registry = {items: new Set(), observer: null};
  const pauseHidden = () => {
    if (doc.hidden) for (const item of registry.items) item.pauseHidden();
  };
  const pausePage = () => {
    for (const item of registry.items) item.pauseHidden();
  };
  doc.addEventListener('visibilitychange', pauseHidden);
  view.addEventListener('pagehide', pausePage);
  if (view.MutationObserver) {
    registry.observer = new view.MutationObserver(records => {
      // Text changes during playback cannot detach a widget.
      if (!records.some(record => Array.from(record.removedNodes).some(node => node.nodeType === 1))) return;
      for (const item of Array.from(registry.items)) if (!item.element.isConnected) item.cleanup();
    });
    registry.observer.observe(doc.documentElement, {childList: true, subtree: true});
  }
  registry.dispose = () => {
    if (registry.items.size) return;
    registry.observer?.disconnect();
    doc.removeEventListener('visibilitychange', pauseHidden);
    view.removeEventListener('pagehide', pausePage);
    documents.delete(doc);
  };
  documents.set(doc, registry);
  return registry;
}

function createWidget(element) {
  const doc = element.ownerDocument;
  const view = doc.defaultView;
  const text = copy[element.dataset.lang === 'ja' || (!element.dataset.lang && doc.documentElement.lang === 'ja') ? 'ja' : 'en'];
  const id = `wave-evolution-${++nextId}`;
  const abort = new view.AbortController();
  const listeners = [];
  let data, frameIndex = 0, playing = false, disposed = false, animation = 0, lastTick = 0, observer;
  const listen = (target, event, handler) => {
    target.addEventListener(event, handler);
    listeners.push(() => target.removeEventListener(event, handler));
  };
  element.classList.add('wave-evolution');
  element.dataset.waveState = 'loading';
  element.setAttribute('role', 'group');
  element.setAttribute('aria-labelledby', `${id}-title`);
  element.setAttribute('aria-busy', 'true');
  // Every string here is a fixed local translation, never fetched markup.
  element.innerHTML = `<p class="wave-title" id="${id}-title">${text.title}</p>
    <p class="wave-intro">${text.intro}</p>
    <div class="wave-controls">
      <div class="wave-buttons"><button type="button" class="wave-play" disabled>${text.play}</button><button type="button" class="wave-reset" disabled>${text.reset}</button></div>
      <output class="wave-time" id="${id}-time" for="${id}-step" aria-live="off"></output>
      <div class="wave-slider"><label for="${id}-step">${text.position}</label><input id="${id}-step" class="wave-step" type="range" min="0" max="1" step="1" value="0" disabled><span class="wave-range-ends" aria-hidden="true"><span>0</span><span class="wave-final-step"></span></span></div>
    </div>
    <div class="wave-legend"><span class="wave-exact">${text.exact}</span><span class="wave-computed">${text.numerical}</span></div>
    <p class="wave-domain" id="${id}-domain"></p>
    <div class="wave-panels">${text.panels.map((panel, i) => `<section class="wave-panel"><h4 id="${id}-panel-${i}">${panel[0]}</h4><p class="wave-panel-note" id="${id}-note-${i}">${panel[1]}</p><canvas class="wave-canvas" role="img" aria-labelledby="${id}-panel-${i}" aria-describedby="${id}-time ${id}-domain ${id}-note-${i} ${id}-metrics-${i}"></canvas><p class="wave-metrics" id="${id}-metrics-${i}"></p></section>`).join('')}</div>
    <p class="wave-help">${text.note}</p><p class="wave-reduced" hidden>${text.reduced}</p>
    <p class="wave-status" role="status" aria-live="polite" aria-atomic="true">${text.loading}</p>`;
  const get = selector => element.querySelector(selector);
  const play = get('.wave-play'), reset = get('.wave-reset'), slider = get('.wave-step');
  const clock = get('.wave-time'), status = get('.wave-status');
  const canvases = Array.from(element.querySelectorAll('.wave-canvas'));
  const metrics = Array.from(element.querySelectorAll('.wave-metrics'));
  const contexts = canvases.map(canvas => canvas.getContext('2d'));
  const reduced = view.matchMedia?.('(prefers-reduced-motion: reduce)');
  const updateMotion = () => { get('.wave-reduced').hidden = !reduced?.matches; };
  updateMotion();
  if (reduced?.addEventListener) listen(reduced, 'change', updateMotion);
  const number = value => (Math.abs(value) < 0.0005 ? 0 : value).toFixed(3);
  const statsText = stats => `${text.minimum} ${number(stats.minimum)} · ${text.maximum} ${number(stats.maximum)} · ${text.norm} ${number(stats.l2Ratio)} · ${text.error} ${number(stats.relativeL2)}`;

  function drawPanel(canvas, ctx, key, color) {
    const width = canvas.getBoundingClientRect().width;
    if (width <= 0) return;
    const height = 172, dpr = Math.min(view.devicePixelRatio || 1, 3);
    const pixelsWide = Math.round(width * dpr), pixelsHigh = Math.round(height * dpr);
    if (canvas.width !== pixelsWide || canvas.height !== pixelsHigh) {
      canvas.width = pixelsWide; canvas.height = pixelsHigh;
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, width, height);
    const left = 43, right = 13, top = 13, bottom = 31;
    const [xMin, xMax] = data.parameters.domain, [yMin, yMax] = data.y_limits;
    const px = x => left + (x - xMin) / (xMax - xMin) * (width - left - right);
    const py = y => height - bottom - (y - yMin) / (yMax - yMin) * (height - top - bottom);
    ctx.font = '11px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';
    ctx.fillStyle = '#56635b';
    ctx.textAlign = 'right';
    const tickStep = 10 ** Math.floor(Math.log10(yMax - yMin)) / 2;
    for (let value = Math.ceil(yMin / tickStep) * tickStep; value <= yMax; value += tickStep) {
      ctx.beginPath(); ctx.strokeStyle = Math.abs(value) < 1e-8 ? '#aeb7ad' : '#e1e2d8'; ctx.lineWidth = 1;
      ctx.moveTo(left, py(value)); ctx.lineTo(width - right, py(value)); ctx.stroke();
      ctx.fillText(Number(value.toFixed(3)).toString(), left - 8, py(value) + 4);
    }
    ctx.textAlign = 'center';
    for (let j = 0; j <= 4; j++) {
      const x = xMin + (xMax - xMin) * j / 4;
      ctx.fillText(Number(x.toFixed(3)).toString(), px(x), height - bottom + 18);
    }
    ctx.textAlign = 'left'; ctx.fillText('u', 9, top + 1);
    ctx.textAlign = 'right'; ctx.fillText('x', width - 2, height - 4);
    const curve = (values, stroke, dash, lineWidth) => {
      ctx.beginPath(); ctx.strokeStyle = stroke; ctx.setLineDash(dash); ctx.lineWidth = lineWidth;
      data.x.forEach((x, j) => j ? ctx.lineTo(px(x), py(values[j])) : ctx.moveTo(px(x), py(values[j])));
      // The endpoint is the first sample of the next periodic copy.
      ctx.lineTo(px(xMax), py(values[0])); ctx.stroke(); ctx.setLineDash([]);
    };
    curve(data.series[key][frameIndex], color, [], 2.4);
    curve(data.series.exact[frameIndex], '#252b28', [5, 4], 1.7);
  }

  function draw() {
    if (!data || disposed) return;
    for (let i = 0; i < seriesKeys.length; i++) drawPanel(canvases[i], contexts[i], seriesKeys[i], colors[i]);
  }

  function showFrame(index) {
    frameIndex = Math.max(0, Math.min(data.steps.length - 1, index));
    const step = data.steps[frameIndex], time = data.time[frameIndex];
    const period = (data.parameters.domain[1] - data.parameters.domain[0]) / Math.abs(data.parameters.advection_speed);
    slider.value = String(frameIndex);
    slider.setAttribute('aria-valuetext', `${text.step} ${step}; t = ${number(time)}`);
    clock.textContent = `${text.time} t = ${number(time)}${Number.isFinite(period) ? ` (${number(time / period)} T)` : ''} · ${text.step} ${step}`;
    clock.title = text.period;
    for (let i = 0; i < seriesKeys.length; i++) metrics[i].textContent = statsText(waveFrameStatistics(data, seriesKeys[i], frameIndex));
    draw();
  }

  function pause(message) {
    playing = false;
    view.cancelAnimationFrame(animation);
    animation = 0;
    play.textContent = text.play;
    element.dataset.waveState = data ? 'paused' : 'loading';
    if (message) status.textContent = message;
  }

  function tick(now) {
    if (!playing || disposed) return;
    if (!element.isConnected) { cleanup(); return; }
    const interval = reduced?.matches ? 200 : 1000 / 12;
    if (now - lastTick >= interval) {
      lastTick = now;
      showFrame(frameIndex + 1);
      if (frameIndex === data.steps.length - 1) { pause(text.finished); return; }
    }
    animation = view.requestAnimationFrame(tick);
  }

  listen(play, 'click', () => {
    if (!data) return;
    if (playing) { pause(text.paused); return; }
    if (frameIndex === data.steps.length - 1) showFrame(0);
    playing = true;
    lastTick = view.performance.now();
    play.textContent = text.pause;
    status.textContent = text.playing;
    element.dataset.waveState = 'playing';
    animation = view.requestAnimationFrame(tick);
  });
  listen(reset, 'click', () => { if (data) { pause(text.resetDone); showFrame(0); } });
  listen(slider, 'input', () => { if (data) { pause(text.paused); showFrame(Number(slider.value)); } });

  const registry = registryFor(doc);
  const item = {element, cleanup, pauseHidden: () => { if (playing) pause(text.hidden); }};
  registry.items.add(item);
  function cleanup() {
    if (disposed) return;
    disposed = true;
    pause();
    abort.abort();
    observer?.disconnect();
    for (const remove of listeners) remove();
    registry.items.delete(item);
    registry.dispose();
    widgets.delete(element);
  }

  async function load() {
    try {
      if (contexts.some(context => !context)) throw new Error('Canvas unavailable');
      const source = new URL(element.dataset.src, doc.baseURI);
      if (!element.dataset.src || source.origin !== new URL(doc.baseURI).origin) throw new Error('Local source required');
      const response = await view.fetch(source, {signal: abort.signal, credentials: 'same-origin'});
      if (!response.ok) throw new Error('Wave data unavailable');
      const loaded = validateWaveEvolutionData(await response.json());
      if (disposed) return;
      data = loaded;
      slider.max = String(data.steps.length - 1);
      get('.wave-final-step').textContent = String(data.steps.at(-1));
      for (const control of [play, reset, slider]) control.disabled = false;
      element.dataset.waveState = 'paused';
      element.setAttribute('aria-busy', 'false');
      status.textContent = text.ready;
      const exact = waveFrameStatistics(data, 'exact', 0);
      get('.wave-legend').title = `${text.exactRange}: ${text.minimum} ${number(exact.minimum)} · ${text.maximum} ${number(exact.maximum)}`;
      const [start, end] = data.parameters.domain;
      const period = (end - start) / Math.abs(data.parameters.advection_speed);
      get('.wave-domain').textContent = `x ∈ [${start}, ${end}]${Number.isFinite(period) ? ` · ${text.period} = ${number(period)}` : ''}`;
      showFrame(0);
      if (view.ResizeObserver) {
        observer = new view.ResizeObserver(draw);
        observer.observe(element);
      } else listen(view, 'resize', draw);
    } catch (error) {
      if (disposed || error.name === 'AbortError') return;
      element.dataset.waveState = 'error';
      element.setAttribute('aria-busy', 'false');
      get('.wave-panels').hidden = true;
      get('.wave-legend').hidden = true;
      get('.wave-domain').hidden = true;
      get('.wave-help').hidden = true;
      get('.wave-reduced').hidden = true;
      status.textContent = text.unavailable;
    }
  }
  load();
  return cleanup;
}

/** Wire newly inserted reading content; repeated calls leave existing controls intact. */
export function wireWaveEvolution(root = globalThis.document) {
  if (!root?.querySelectorAll) return () => {};
  const elements = Array.from(root.querySelectorAll('[data-wave-evolution]'));
  if (root.matches?.('[data-wave-evolution]')) elements.unshift(root);
  const cleanups = elements.map(element => {
    if (!widgets.has(element)) widgets.set(element, createWidget(element));
    return widgets.get(element);
  });
  return () => cleanups.forEach(cleanup => cleanup());
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => wireWaveEvolution(), {once: true});
  else wireWaveEvolution();
}
