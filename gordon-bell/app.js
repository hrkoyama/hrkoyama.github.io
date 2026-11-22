'use strict';
let db, visible = [], rosterVisible = [];
const $ = id => document.getElementById(id);
const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const link = (url, label) => url ? `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)} ↗</a>` : `<span class="offline-source">${esc(label)} (preserved offline)</span>`;
const src = (ids) => (ids || []).map(id => link(db.sources[id].url, db.sources[id].label)).join(' ');
const doi = p => p.doi ? 'https://doi.org/' + p.doi : null;
function doiLink(p, detail=false) { if(p.citation_type==='techreport' && p.doi) return link(doi(p),'Related proceedings DOI: '+p.doi); return p.doi ? link(doi(p), p.doi_verification?.status === 'unverified' ? 'DOI candidate: '+p.doi+(detail?' — direct verification pending':'') : 'DOI: '+p.doi) : '<span class="unresolved-doi">DOI unresolved for this version</span>'; }
function measurement(m) { return `${m.relation && m.relation !== '=' ? m.relation+' ' : ''}${m.value.toLocaleString('en-US')} ${m.unit}`; }
function stageLabel(m) { return ({preserved_proceedings_manuscript:'Preserved proceedings manuscript',submitted_manuscript:'Submitted manuscript',revised_manuscript:'Revised manuscript',conference_presentation:'Conference presentation',official_award_announcement:'Official award announcement',later_followup:'Later follow-up',author_preprint:'Author preprint',pre_conference_preprint:'Pre-conference preprint',archived_author_manuscript:'Archived author manuscript (revision date not stated)',later_author_manuscript:'Later author manuscript (after conference)',preprint:'Author preprint',author_manuscript_original_submission_baseline:'Original-submission baseline reported in author manuscript',author_reported_implementation_update_in_manuscript:'Implementation update reported in author manuscript'})[m.evidence_stage] || m.source_version_description || m.evidence_stage?.replaceAll('_',' ') || 'Source manuscript'; }
function awardLabel(p) { if(!p.award && p.year<=1990) return 'COMPETITION ENTRY · AWARD NOT CHECKED'; return p.award?.label || (p.award_status?.startsWith('Source conflict') ? 'AWARD CLAIMS CONFLICT' : p.award_status?.startsWith('Outcome checked') ? 'FINALIST' : 'FINALIST · AWARD NOT CHECKED'); }
function reviewedVersions(p) { return (p.reviewed_versions || [{evidence_stage:'preserved_proceedings_manuscript',source_revision_date:null}]).map(v=>stageLabel(v)+(v.source_revision_date?' · '+v.source_revision_date:'')).join('; '); }
function fillSelect(id, values) { for (const value of [...new Set(values)].sort()) { const o = document.createElement('option'); o.value = value; o.textContent = value; $(id).append(o); } }
function catalogueMatches(p,r,q) {
  const detailed=db.papers.find(d=>d.id===p.detailed_paper_id);
  return !q || [p.title,p.publisher_title,p.doi,r.year,...p.authors,...(p.search_aliases||[]),p.award_result?.label,p.award_result?.category,...(p.award_result?.recipients||[]),...(p.award_result?.claims||[]).flatMap(c=>[c.outcome,c.category,c.project_title_as_printed,...(c.recipients||[])]),...(p.bibliography_review?.named_participants||[]),...(p.bibliographic_versions||[]).flatMap(v=>v.authors||[]),detailed?.title,...(detailed?.authors||[]),...(detailed?.title_aliases||[]).map(a=>a.title),...(detailed?.machines||[])].join(' ').toLowerCase().includes(q);
}
function catalogueMatchCount(q) { return (db.annual_rosters||db.recent_rosters).reduce((n,r)=>n+r.records.filter(p=>catalogueMatches(p,r,q)).length,0); }
function syncArchiveSearch(from) {
  const other=from==='search'?'recent-search':'search'; $(other).value=$(from).value; if(from==='search') { $('recent-year').value='all'; $('roster-doi').value='all'; } renderRecent(); render();
}
function render() {
  const q = $('search').value.toLowerCase().trim();
  visible = db.papers.filter(p => {
    const text = [p.year, p.title, ...p.title_aliases.map(a => a.title), ...p.authors, ...p.machines, p.field, p.summary, p.doi].join(' ').toLowerCase();
    return (!q || text.includes(q)) && ($('paper-year').value === 'all' || String(p.year) === $('paper-year').value) && ($('result').value === 'all' || Boolean(p.award) === ($('result').value === 'winner')) && ($('field').value === 'all' || p.field === $('field').value) && ($('machine').value === 'all' || p.machines.includes($('machine').value));
  });
  $('count').textContent = `${visible.length} of ${db.papers.length} papers`;
  const catalogueCount=catalogueMatchCount(q);
  $('search-coverage').innerHTML=q?`${catalogueCount} candidate records match in the <a href="#recent">annual index</a>; ${visible.length} reviewed manuscripts match the detail filters.`:'';
  $('list').innerHTML = visible.length ? visible.map(p => `<article class="card"><div class="year">${p.year}</div><div><span class="tag ${p.award ? 'winner' : ''}">${esc(awardLabel(p))}</span><h3><button class="title-button" data-paper="${esc(p.id)}">${esc(p.title)}</button></h3><p class="authors">${esc(p.authors.join(' · '))}</p><p class="card-summary">${esc(p.summary)}</p><p class="version-note">Performance source: ${esc(reviewedVersions(p))}</p><div class="paper-links">${doiLink(p)}<button data-paper="${esc(p.id)}">Details & sources</button><span>${esc(p.field)}</span></div></div><aside class="performance"><strong>${esc(p.machines.join(' / '))}</strong>${p.measurements.length ? p.measurements.map(m => `<div class="measure"><b>${esc(measurement(m))}</b><small>${esc(m.precision)} · ${esc(m.scope)}</small></div>`).join('') : '<p>Performance observation not yet extracted.</p>'}</aside></article>`).join('') : `<p class="empty">No reviewed manuscripts match these filters.${catalogueCount&&q?' <a href="#recent">View '+catalogueCount+' matching candidate records in the annual index.</a>':' Try another author, machine or research area.'}</p>`;
}
function verificationNotice(v) {
  if(typeof v==='string') return esc(v);
  return `${esc(v.status)}. ${esc(v.limits||'')}<details><summary>Audit method and locations</summary><p>${esc(v.method)}</p><p>${esc(v.title_author_locations||'')} ${esc(v.performance_locations||'')}</p></details>`;
}
function manuscriptEvidence(e) {
  if(!e) return '';
  const html=e.media_type==='text/html'||e.kind?.includes('html')||/\.html?$/i.test(e.filename);
  const derivative=e.kind==='reading_derivative_from_preserved_author_postscript';
  const format=html?'HTML manuscript':derivative?'PostScript original · '+e.page_count+' pages in a local PDF reading derivative':e.page_count?e.page_count+' PDF pages':'Source manuscript';
  return `<h3>Reviewed manuscript version</h3><p>${link(e.source_url,'Read source manuscript')} · ${esc(format)}</p>${e.companion_postscript?`<p>Companion PostScript: ${esc(e.companion_postscript.page_count)} pages. Local PDF reading derivative: ${esc(e.reading_derivative.page_count)} pages.</p>`:''}${e.note?`<p>${esc(e.note)}</p>`:''}<p>The title, ordered byline and selected machine/performance fields were checked against this version. A later proceedings or presentation version may differ.</p><details><summary>Verified file identity</summary><p>${derivative?'Reading derivative SHA-256':'Reviewed source SHA-256'}: <code>${esc(e.sha256)}</code></p>${e.original_sha256?`<p>Original PostScript SHA-256: <code>${esc(e.original_sha256)}</code></p>`:''}${e.companion_postscript?`<p>Companion PostScript SHA-256: <code>${esc(e.companion_postscript.sha256)}</code></p>`:''}</details>`;
}
function citationVersionNote(p) {
  if(!p.citation_type) return '';
  if(p.citation_type==='techreport') return `<p class="notice">Reviewed technical report: ${esc(p.report_number)} · ${esc(p.institution)} · ${esc(p.citation_year)}. Competition index year: ${p.year}. The earlier original submission is a distinct version.</p>`;
  if(p.citation_type==='article') return `<p class="notice">Reviewed journal article: ${esc(p.journal)} · ${esc(p.citation_year)}. Competition index year: ${p.year}. This DOI identifies the later article; the original submitted file remains unrecovered.</p>`;
  if(p.evidence_stage==='preserved_proceedings_manuscript') return '<p class="notice">Reviewed preserved conference manuscript. Its file identity and version-specific values are recorded separately from original submissions and conference-day updates.</p>';
  return '<p class="notice">Reviewed author-hosted conference manuscript. Its byline and values remain separate from the updated committee submission and exact proceedings bytes.</p>';
}
function doiAvailability(p) {
  const d=p.doi_verification;
  return d?.resolver_http_status===404?`<p class="notice">Publisher-assigned DOI. The recorded resolver check returned HTTP 404 on ${esc(d.resolver_checked_on)}; identifier assignment and link availability are separate.</p>`:'';
}
function showPaper(id) {
  const p = db.papers.find(p => p.id === id); if (!p) return;
  const rows = p.measurements.map(m => `<tr><td><strong>${esc(measurement(m))}</strong><small>${esc(m.machine)}</small></td><td>${esc(m.precision)}</td><td>${esc(m.scope)}<small>${esc(m.scale)}</small>${m.note ? `<small>${esc(m.note)}</small>` : ''}<details><summary>Counting and timing method</summary><p>${esc(m.measurement_method || 'Not extracted')}</p></details></td><td>${esc(stageLabel(m))}<small>Revision: ${esc(m.source_revision_date || 'not stated')}</small><small>Measured: ${esc(m.measurement_date || m.measurement_date_note || 'not established')}</small><small>Conference update: ${esc(m.conference_update_status)}</small><small>Final score: ${esc(m.final_score_status)}</small><small>Checked: ${esc(m.checked_on)}</small></td><td>${src([m.source_id])}<small>${esc(m.location)}</small></td></tr>`).join('');
  const sources = Object.entries(p.provenance).filter(([, ids]) => ids.length).map(([field, ids]) => `<li><strong>${esc(field[0].toUpperCase()+field.slice(1))}:</strong> ${src(ids)}</li>`).join('');
  const local = (p.local_evidence || []).map(e => `<h3>Preserved proceedings evidence</h3><p><strong>${esc(e.volume)} / ${esc(e.code)}</strong></p><p>Index title: ${esc(e.title)}</p><p>Original relative PDF path: <code>${esc(e.pdf_relative_path)}</code><br>Size: ${e.size_bytes.toLocaleString('en-US')} bytes</p><details><summary>File identity and verification</summary><p>Verified SHA-256: <code>${esc(e.sha256)}</code></p><p>Local copied bytes independently matched; selected manuscript fields checked ${esc(e.checked_on)}. Original PDFs are not hosted by this site. The DOI source link points to the publication record, not necessarily these exact manuscript bytes.</p></details>`).join('');
  const configurations = (p.machine_configurations || []).map(m => `<li><strong>${esc(m.name)}</strong> — ${esc(m.facility)}<p>${esc(m.configuration)}</p><small>${esc(m.location)} ${esc(m.note || '')}</small></li>`).join('');
  const abstractIds = p.provenance.abstract;
  const webEvidence = manuscriptEvidence(p.local_fulltext);
  $('detail-body').innerHTML = `<span class="eyebrow">${p.year} / ${esc(p.field)}</span><h2 id="detail-title">${esc(p.title)}</h2><span class="tag ${p.award ? 'winner' : ''}">${esc(awardLabel(p))}</span><p class="detail-authors">${esc(p.authors.join(' · '))}</p><p>${doiLink(p,true)}</p>${doiAvailability(p)}${citationVersionNote(p)}<div class="notice">${verificationNotice(p.verification)}. Archive updated: ${esc(db.updated_on)}.</div><h3>Abstract & research summary</h3><p>${esc(p.summary)}</p><p class="source-links">Editorial summary. Read the original abstract: ${src(abstractIds)}</p><h3>Reported performance</h3>${rows ? `<div class="table-wrap"><table><thead><tr><th>REPORTED VALUE / MACHINE</th><th>PRECISION</th><th>SCOPE / SCALE / METHOD</th><th>RESULT STAGE / DATE</th><th>EVIDENCE</th></tr></thead><tbody>${rows}</tbody></table></div>` : '<p>No performance observation has been extracted. Hardware capacity is not substituted.</p>'}<h3>Machines and configuration</h3><ul>${configurations}</ul><p class="source-links">${src(p.provenance.machines)}</p>${p.title_aliases.length ? `<details class="aliases"><summary>Source title variants (${p.title_aliases.length})</summary><ul>${p.title_aliases.map(a => `<li>${esc(a.title)} — ${src([a.source_id])}</li>`).join('')}</ul></details>` : ''}${local}${webEvidence}<h3>Research notes</h3><ul>${p.notes.map(n => `<li>${esc(n)}</li>`).join('')}</ul><h3>Field-level evidence</h3><ul class="source-list">${sources}</ul><p class="source-links">Local manuscript bytes and cited fields have been checked. DOI/abstract links are publication references and do not guarantee unrestricted access. Manuscript performance is not automatically the final conference score.</p>`;
  $('detail').showModal();
}
function download(name, content, type) { const a = document.createElement('a'); const url = URL.createObjectURL(new Blob([content], {type})); a.href = url; a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); }
function exportCSV() {
  const columns = ['year','title','authors','award','doi','machine','relation','value','unit','precision','scope','scale','source_url','source_location','evidence_stage','source_revision_date','measurement_date','measurement_date_note','presentation_date','checked_on','conference_update_status','final_score_status','measurement_method','doi_verification','award_status','publication_year','publication_type','related_publication_doi','doi_scope'];
  const lines = [columns];
  for (const p of visible) for (const m of (p.measurements.length ? p.measurements : [null])) lines.push([p.year,p.title,p.authors.join('; '),p.award?.label || p.selection || 'Finalist',p.citation_type==='techreport'?'':(p.doi || ''),m?.machine || p.machines.join('; '),m?.relation === '=' ? 'equal' : (m?.relation || ''),m?.value ?? '',m?.unit || '',m?.precision || '',m?.scope || '',m?.scale || '',m ? db.sources[m.source_id].url : '',m?.location || '',m?.evidence_stage || '',m?.source_revision_date || '',m?.measurement_date || '',m?.measurement_date_note || '',m?.presentation_date || '',m?.checked_on || '',m?.conference_update_status || '',m?.final_score_status || '',m?.measurement_method || '',p.doi_verification?.status || 'existing bibliographic evidence',p.award_status || '',p.citation_year||p.year,p.citation_type||'inproceedings',p.citation_type==='techreport'?(p.doi||''):'',p.citation_type==='techreport'?'No DOI established for reviewed report; related proceedings DOI is separate':p.citation_year&&p.citation_year!==p.year?'DOI identifies the later publication, not the original competition submission':'DOI identifies the cited publication; manuscript version may differ']);
  const cell = v => { const s=String(v ?? ''); return '"'+(/^[=+\-@]/.test(s) ? "'" : '')+s.replaceAll('"','""')+'"'; };
  download('gordon-bell-archive.csv', '\uFEFF'+lines.map(row => row.map(cell).join(',')).join('\r\n'), 'text/csv;charset=utf-8');
}
function exportBib() {
  const bibEsc = s => String(s).replace(/[{}\\]/g, c => '\\'+c);
  const entries=visible.map(p=>{
    const type=p.citation_type||'inproceedings', year=p.citation_year||p.year;
    const fields=[['title',p.citation_title||p.title],['author',(p.citation_authors||p.authors).join(' and ')],['year',year]];
    if(type==='article') { fields.push(['journal',p.journal],['volume',p.volume],['number',p.issue],['pages',p.pages]); }
    else if(type==='techreport') { fields.push(['institution',p.institution],['number',p.report_number]); }
    else fields.push(['booktitle',p.booktitle||'Proceedings of SC'+String(p.year).slice(-2)]);
    if(type!=='techreport' && p.doi && p.doi_verification?.status!=='unverified') fields.push(['doi',p.doi],['url',doi(p)]);
    else {
      if(p.local_fulltext?.source_url) fields.push(['url',p.local_fulltext.source_url]);
      if(p.doi && type!=='techreport') fields.push(['note','DOI candidate '+p.doi+' remains unverified; manuscript evidence audited']);
    }
    if(year!==p.year) fields.push(['note','Reviewed publication year '+year+'; competition entry '+p.year+'. Original submitted file not identified as this publication.']);
    return '@'+type+'{'+p.id+',\n'+fields.filter(([,v])=>v!=null&&v!=='').map(([k,v])=>'  '+k+' = {'+bibEsc(v)+'}').join(',\n')+'\n}';
  });
  download('gordon-bell-archive.bib',entries.join('\n\n'),'text/plain;charset=utf-8');
}
function auditedHolding(r) {
  const hashes=new Set(r.body_files.map(f=>f.sha256));
  return db.papers.find(p=>p.year===r.year&&[p.local_fulltext?.sha256,p.local_fulltext?.original_sha256,p.local_fulltext?.companion_postscript?.sha256,...(p.local_evidence||[]).map(e=>e.sha256)].some(h=>h&&hashes.has(h)));
}
function renderHoldings() {
  const q=$('holdings-search').value.trim().toLowerCase(), year=$('holdings-year').value;
  const rows=db.holdings.records.filter(r => (year==='all'||String(r.year)===year) && (!q||[r.title,r.year,r.code,...(r.authors||[])].join(' ').toLowerCase().includes(q)));
  $('holdings-count').textContent=`${rows.length} of ${db.holdings.records.length} local candidate records`;
  $('holdings-list').innerHTML=rows.map(r=>{const reviewed=auditedHolding(r);return `<details class="holding"><summary><span>${r.year} / ${esc(r.code)}</span> ${esc(r.title)}</summary><p>${esc(reviewed?reviewed.content_status:r.content_status)}</p>${reviewed?`<p><button data-paper="${esc(reviewed.id)}">Read manuscript audit for these verified bytes</button></p>`:''}${r.authors?`<p>${esc(r.authors.join(' · '))}</p>`:''}${r.award_status?`<p>${esc(r.award_status)}</p>`:''}<p>Source volume: ${esc(r.source_directory)}</p><ul>${r.body_files.map(f=>`<li><code>${esc(f.relative_path)}</code> · ${f.size_bytes.toLocaleString('en-US')} bytes</li>`).join('')}</ul><p>SHA-256-verified local copies. Full text is retained offline; this site provides metadata, not manuscript downloads.</p></details>`;}).join('');
}
function annualReviewNotes(y) {
  const p=y.partial_manuscript_review, r=y.recovery_review;
  let html=p?`<p class="notice">${esc(p.note)}</p><p class="source-links">${src(p.source_ids)}</p>`:'';
  if(p?.program_bibliography) { const b=p.program_bibliography; html+=`<details><summary>Recovered NWT program title and participant order</summary><p>${esc(b.nwt_title)}</p><p>${esc(b.nwt_program_author_order.join(' · '))}</p><p>${esc(b.note)}</p></details>`; }
  if(r) html+=`<details><summary>Source recovery review</summary><p>${esc(r.reason||r.status)}</p>${r.next_action?'<p>'+esc(r.next_action)+'</p>':''}${r.source_ids?'<p class="source-links">'+src(r.source_ids)+'</p>':''}${r.source_url?link(r.source_url,'Next primary source'):''}</details>`;
  if(y.separate_performance_events) html+=`<details><summary>${y.separate_performance_events.length} dated institutional observations · outside manuscript totals</summary>${y.separate_performance_events.map(e=>`<p><strong>Published ${esc(e.published_on)}</strong> · ${esc(e.evidence_stage.replaceAll('_',' '))}</p>${e.measurements.map(m=>`<p><strong>${esc(m.value)} ${esc(m.unit)}</strong> · ${esc(m.machine)}<br>${esc(m.scope)}<br>Scale: ${esc(m.scale)}<br>Precision: ${esc(m.precision)}<br>Method: ${esc(m.measurement_method)}<br>Measured: ${esc(m.measurement_date_note)}<br>Location: ${esc(m.location)}. Final conference score unestablished.</p>`).join('')}<p>${esc(e.note)}</p><p class="source-links">${src([e.source_id])}</p>`).join('')}</details>`;
  return html;
}
function renderYearCoverage() {
  const audit=db.annual_review, view=$('coverage-view').value;
  const rows=audit.rows.filter(y=>view==='all'||(view==='untouched'&&y.queue_status!=='context_only'&&!y.manuscript_audits)||(view==='reviewed'&&y.manuscript_audits)||(view==='continuation'&&audit.continuation?.target_years.includes(y.year))||(view==='early'&&audit.early_recovery?.target_years.includes(y.year))||(view==='batches'&&audit.year_batches?.completed.some(b=>b.year===y.year)));
  $('annual-review-summary').textContent=`${audit.calendar_years} calendar years inventoried · ${audit.summary.indexed_years} annual index groups · ${audit.summary.manuscript_years} years with manuscript audits · ${audit.summary.awaiting_first_manuscript_years.length} indexed years await their first manuscript. Inventory reviewed ${audit.checked_on}; original source-check dates retained.`;
  const continuation=audit.continuation;
  $('continuation-summary').textContent=continuation?`Pass from ${continuation.start_year}: ${continuation.completed.length} of ${continuation.target_years.length} previously untouched years now have a first manuscript audit.${continuation.blocked.length?' '+continuation.blocked.length+' require source recovery.':''}${continuation.pending_years.length?' '+continuation.pending_years.length+' await review.':''}`:'';
  const early=audit.early_recovery;
  $('early-recovery-summary').textContent=early?`Early-year recovery: ${early.completed.length} of ${early.target_years.length} years have a complete reviewed version (1988, 1990, 1994, 1998). Original submissions, later author/publication versions and score updates remain distinct.`:'';
  const batches=audit.year_batches?.completed||[];
  $('year-batch-summary').textContent=batches.length?'Year batches checked: '+batches.map(b=>b.year+' · '+b.indexed_manuscripts_checked+' of '+b.indexed_manuscripts_checked+' indexed manuscripts ('+b.new_manuscripts+' added in this batch)').join('; ')+'. Complete preserved versions reviewed; publication-version comparisons and final conference scores remain separate.':'';
  $('coverage-count').textContent=`${rows.length} of ${audit.calendar_years} calendar years shown`;
  $('year-coverage').innerHTML=rows.map(y=>{
    const context=y.queue_status==='context_only';
    const roster=y.indexed_entries==null?(context?'Year-label transition':'Not recovered'):y.indexed_entries+' indexed'+(y.expected_entries==null?' · total unconfirmed':y.indexed_entries<y.expected_entries?' of '+y.expected_entries+' expected':' against '+y.expected_entries+' in the source');
    const awards=context?'Context only':y.indexed_entries==null?'Roster needed':`${y.award_supported_entries} supported · ${y.award_conflicts} conflicting · ${y.award_unestablished_entries} unestablished`+(y.other_entrant_entries?` · ${y.other_entrant_entries} explicitly Other entrants`:'');
    const bibliography=context?'Context only':y.indexed_entries==null?'Roster needed':`${y.verified_dois} DOI matched · ${y.unresolved_dois} unresolved · ${y.publication_byline_gaps} empty author fields · ${y.manuscript_byline_checked_entries} manuscript bylines checked`;
    return `<article class="year-cell ${y.manuscript_audits?'audited':''}"><h3>${y.year}</h3><span class="tag ${y.manuscript_audits?'winner':'pending'}">${context?'Year-label transition':y.manuscript_audits?y.manuscript_audits+' manuscript'+(y.manuscript_audits===1?'':'s')+' checked':'First manuscript pending'}</span><dl><dt>Roster</dt><dd>${esc(roster)}<small>${esc(y.roster_status.replaceAll('_',' '))}</small></dd><dt>Awards</dt><dd>${esc(awards)}</dd><dt>Bibliography</dt><dd>${esc(bibliography)}</dd><dt>Manuscripts</dt><dd>${y.offline_candidate_bodies} candidate bodies in original-copy receipts · ${y.first_page_only_checks} additional byline-only first-page checks</dd><dt>Performance</dt><dd>${y.performance_observations} scoped observations · final conference scores unestablished</dd></dl>${annualReviewNotes(y)}${y.doi_resolution_note?`<p class="notice">${esc(y.doi_resolution_note)}</p>`:''}${y.performance_history_note?`<p>${esc(y.performance_history_note)}</p>`:''}<p class="next-evidence"><strong>Next evidence</strong> ${esc(y.batch_next_action||y.next_action)}</p>${y.manuscript_ids.map(id=>`<button data-paper="${esc(id)}">${esc(db.papers.find(p=>p.id===id).title)}</button>`).join(' ')}<details><summary>Source dates and byline status</summary><p>Source checks: ${esc(y.evidence_checked_on.join(', ')||'not established')}. Calendar inventory: ${esc(y.inventory_reviewed_on)}.</p>${Object.entries(y.byline_status_counts).map(([status,n])=>`<p>${n} · ${esc(status.replaceAll('_',' '))}</p>`).join('')}<p class="source-links">${src(y.source_ids)}</p></details><p class="annual-links">${annualLinks(y.sc_links)||'SC conference series began in 1988.'}</p></article>`;
  }).join('');
}
function annualLinks(s) {
  if(!s) return '';
  return [s.website_url&&link(s.website_url,'SC website'),s.proceedings_url&&link(s.proceedings_url,'Proceedings'),s.history_pdf_url&&link(s.history_pdf_url,'SC history PDF')].filter(Boolean).join(' ');
}
function rosterStatus(r) {
  const status=r.roster_completeness.status;
  if(r.postconference_review) return 'Postconference program and publication review · '+r.postconference_review.checked_on;
  if(status==='preserved_session_roster_award_results_reviewed') return 'Preserved session list · individual award results reviewed '+r.historical_review.checked_on;
  if(r.roster_completeness.expected_count==null || status.includes('partial')) return 'Partial roster · further candidates may be missing';
  if(status.includes('award_labels_unresolved')) return 'Preserved session list · finalist/winner labels unresolved';
  return r.source_method==='Preserved conference index' ? 'Preserved official index enumerated' : 'Primary source roster enumerated';
}
function historicalReview(p, ref) {
  const claims=p.award_result?.claims||[], b=p.bibliography_review, result=p.award_review;
  const award=claims.length?`<details class="award-history" ${p.award_result.status==='source_conflict'?'open':''}><summary>Award wording by source</summary><p>${esc(p.award_result.evidence_note)}</p>${claims.map(c=>`<section class="byline-version"><h5>${esc(c.outcome)} · ${esc(c.category)}</h5>${c.recipients?.length?`<p>Names in this award source: ${esc(c.recipients.join(' · '))}</p>`:''}${c.project_title_as_printed?`<p>Project title in this source: ${esc(c.project_title_as_printed)}</p>`:''}<p>${esc(c.location)}. ${ref(c.source_id,'Award source')}</p>${c.note?`<p>${esc(c.note)}</p>`:''}</section>`).join('')}<p>Reviewed ${esc(p.award_result.checked_on)}. Award-source names are separate from the publication byline.</p></details>`:'';
  const review=result?`<p class="record-review">${esc(result.label)}. ${esc(result.note)} Reviewed ${esc(result.checked_on)}. ${ref(result.source_id,'Result evidence')}</p>`:'';
  const bibliography=b?`<details class="bibliography-review"><summary>Bibliography review · ${esc(b.checked_on)}</summary><p>${esc(b.note)}</p>${p.authors_source_id?`<p><strong>Paper authors (${p.authors.length}):</strong> ${esc(p.authors.join(' · '))}</p><p>${esc(b.byline_scope||'Ordered byline checked on manuscript first page')}. ${ref(p.authors_source_id,'Byline evidence')}</p>`:''}${b.named_participants?.length?`<p><strong>${esc(b.names_kind)}:</strong> ${esc(b.named_participants.join(' · '))}</p>`:''}${p.award_result?.recipients?.length?`<p><strong>Names in award announcement (${p.award_result.recipients.length}):</strong> ${esc(p.award_result.recipients.join(' · '))}</p>`:''}${b.registry_lookup_date?`<p>Registry/catalog lookup evidence retained from ${esc(b.registry_lookup_date)}; reviewed with the current title/byline evidence. An unresolved match does not prove that no DOI exists.</p>`:''}${b.next_evidence?`<p>Still needed: ${esc(b.next_evidence)}</p>`:''}<p>Performance audit: ${esc(b.performance_audit)}. ${b.source_ids.map(s=>ref(s,'Bibliographic source')).join(' ')}</p></details>`:'';
  return award+review+bibliography;
}
function authorEvidenceNote(p) {
  if(p.detailed_paper_id) return 'This annual byline follows its cited bibliographic source. The linked manuscript audit has its own checked byline; versions may differ.';
  if(p.authors_status?.startsWith('ordered_byline_checked')) return 'Ordered names checked on the cited manuscript first page. This bibliography check does not include performance methodology.';
  if(p.detailed_paper_id) return 'Registry names are preserved here; the reviewed manuscript byline is shown in Manuscript details.';
  return /registry|crossref|publisher_deposited/i.test(p.authors_status)?'Names follow publisher-deposited registry order; the PDF byline has not been audited here.':'Names follow the cited source; the full publication byline has not been reconciled here.';
}
function annualPerformanceHistory(p, ref) {
  const review=p.performance_review, updates=review?.performance_updates||[];
  if(!updates.length) return '';
  const baseline=review.baseline_comparison;
  const baselineHtml=baseline?`<section class="byline-version"><h5>Author-hosted finalist manuscript · revision date not stated</h5><p>${esc(baseline.throughput.value.toLocaleString('en-US'))} ${esc(baseline.throughput.unit)} · ${esc(baseline.scale.apus.toLocaleString('en-US'))} APUs · ${esc(baseline.speedup.value)}× reported speedup.</p><p>${esc(baseline.throughput.scope)}. ${esc(baseline.throughput.precision)}. ${esc(baseline.audit_limit)}</p><p>${ref(baseline.source_id,'Manuscript source')}</p></section>`:'';
  return `<details class="performance-updates" open><summary>Reported result history · source stages and conditions differ</summary><p>These records are separate from the selected manuscript audits. No final conference score is established, and matching measurement conditions are not assumed.</p>${baselineHtml}${updates.map(u=>`<section class="byline-version"><h5>Conference-period institutional announcement · ${esc(u.published_on)}</h5><ul>${u.measurements.map(m=>`<li><strong>${esc(m.comparison_operator==='='?'':m.comparison_operator+' ')}${esc(m.value.toLocaleString('en-US'))} ${esc(m.unit)}</strong> — ${esc(m.metric)}. ${esc(m.scope)}.</li>`).join('')}</ul><p>Scale: ${esc(u.measurements[0].scale)}. ${esc(u.limitations)}</p><p>${ref(u.source_id,'Institutional announcement')}</p></section>`).join('')}</details>`;
}
function annualReview(p, ref) {
  if(!p.postconference_status) return '';
  const state=p.postconference_status;
  const award=p.award_result?'Award verified from ACM; announced '+p.award_result.announcement_date:'Finalist membership verified; individual award outcome not established here';
  const versions=(p.bibliographic_versions||[]).map(v=>`<section class="byline-version"><h5>${esc(v.version_label)} · ${v.authors.length} authors</h5><p>${esc(v.authors.join(' · '))}</p><p>${ref(v.source_id,'Byline source')}</p></section>`).join('');
  return `<p class="record-review">${esc(award)}. Conference-day update and final score: unverified. Reviewed ${esc(state.checked_on)}.</p><details class="byline-history"><summary>Ordered author lists by source and retrieval date</summary><p>Dates below are retrieval dates. A source revision date is not stated. Publisher and official-program lists remain separate.</p>${versions}</details>${annualPerformanceHistory(p,ref)}`;
}
function annualSnapshot(r) {
  if(!r.preconference_snapshot) return '';
  const old=r.preconference_snapshot;
  return `<details class="roster-evidence preconference-history"><summary>Archived preconference snapshot · ${esc(old.checked_on)}</summary><p>The six scheduled entries and publisher bylines were captured before SC26. That snapshot established membership and publisher-assigned DOIs; it did not establish award outcomes or final scores.</p><ul>${old.records.map(p=>`<li>${esc(p.title)} · ${p.authors.length} publisher-listed authors</li>`).join('')}</ul><p>Complete source-linked metadata is retained in the full JSON export. Each current entry also shows its dated author lists.</p></details>`;
}
function renderRecent() {
  const q=$('recent-search').value.trim().toLowerCase(), year=$('recent-year').value, doiState=$('roster-doi').value;
  const catalogue=db.annual_rosters || db.recent_rosters;
  let total=0,matched=0; rosterVisible=[];
  const html=catalogue.map(r=>{
    total+=r.records.length;
    const records=r.records.filter(p=>(year==='all'||String(r.year)===year)&&catalogueMatches(p,r,q)&&(doiState==='all'||(doiState==='verified'&&p.doi_status==='verified')||(doiState==='unresolved'&&!['verified','not_applicable'].includes(p.doi_status))||(doiState==='not_applicable'&&p.doi_status==='not_applicable')));
    matched+=records.length;
    if(!records.length) return '';
    const sources=Object.fromEntries(r.sources.map(s=>[s.id,s]));
    for(const p of records) rosterVisible.push({year:r.year,...p,conference_year:r.conference_year||r.year,year_label:r.year_label||String(r.year),entry_type:r.roster_completeness.membership_label||'candidates',title_source:sources[p.title_source_id],award_source:sources[p.award_result?.source_id],authors_source:sources[p.authors_source_id],award_review_source:sources[p.award_review?.source_id],award_claims:(p.award_result?.claims||[]).map(c=>({...c,source_url:sources[c.source_id]?.url||''})),roster_status:r.roster_completeness.status});
    const ref=(id,label)=>sources[id]?link(sources[id].url,label||sources[id].label):'';
    const rosterSources=r.roster_completeness.basis_source_ids.map(id=>ref(id)).join(' ');
    const note=r.roster_completeness.note || r.notes?.[0] || '';
    const open=year!=='all'||q||doiState!=='all';
    const membership=r.roster_completeness.membership_label || 'candidates';
    const partial=r.roster_completeness.expected_count==null || r.roster_completeness.status.includes('partial');
    const countLabel=partial ? r.records.length+' identified · partial list' : r.records.length+' '+membership+(r.roster_completeness.status.includes('award_labels_unresolved')?' · labels unresolved':'');
    return `<details class="roster-year" ${open?'open':''}><summary><strong>${r.year}${r.event_label?' · '+esc(r.event_label):' / SC'+String(r.year).slice(-2)}</strong><span>${esc(countLabel)} · ${r.verified_doi_count} DOI verified</span></summary><p class="annual-links">${/Compcon/i.test(r.event_label||'')?'SC resources for '+esc(r.conference_year)+' (separate from the Compcon presentation): ':''}${annualLinks(r.sc_links)}</p><details class="roster-evidence"><summary>Annual source evidence</summary><p class="source-links">${rosterSources}</p>${note?`<p>${esc(note)}</p>`:''}</details><p class="roster-status">${esc(rosterStatus(r))} · ${r.detailed_paper_count || 0} detailed manuscript audits · Conference-day scores unverified.</p>${r.postconference_review?`<p class="conference-review notice">${esc(r.postconference_review.note)} ${ref(r.postconference_review.award_source_id,'ACM award announcement')}</p>`:''}${annualSnapshot(r)}${r.roster_recovery_on?`<p class="notice">${esc(note)}</p>`:""}<ol class="roster-records">${records.map(p=>`<li>${p.award_result?`<p class="award-result"><span class="tag ${p.award_result.status==='verified'?'winner':'pending'}">${esc(p.award_result.label)}</span>${ref(p.award_result.source_id,'Award evidence')}</p>`:''}<h4>${esc(p.title)}</h4>${p.title_kind==='editorial_description'?'<p class="title-kind">Editorial description; formal paper title not recovered.</p>':p.title_kind==='corporate_entry'?'<p class="title-kind">Organization-level finalist; no single paper is implied.</p>':p.title_kind==='publisher_title'?'<p class="title-kind">Publication title; original selection title not recovered.</p>':''}<div class="paper-links">${p.doi_status==='verified'?link('https://doi.org/'+p.doi,'DOI: '+p.doi):p.doi_status==='not_applicable'?'<span>DOI not applicable to this organization-level entry</span>':'<span class="unresolved-doi">DOI unresolved</span>'}${p.doi_verification?.resolver_status==='not_found'?'<span class="unresolved-doi">Publisher-assigned DOI; resolver returned HTTP 404 (checked '+esc(p.doi_verification.resolver_checked_on)+')</span>':''}${p.detailed_paper_id?`<button data-paper="${esc(p.detailed_paper_id)}">Manuscript details</button>`:''}${ref(p.title_source_id,'Title source')}${p.publication_url?link(p.publication_url,'Publisher record'):''}${p.doi_status==='verified'?ref(p.doi_source_id,'DOI verification'):''}</div>${historicalReview(p,ref)}${annualReview(p,ref)}<details><summary>Bibliographic evidence & title variants</summary>${p.publisher_title&&p.publisher_title!==p.title?`<p>Publisher title: ${esc(p.publisher_title)}</p>`:''}${p.authors.length?`<p>${esc(p.authors.join(' · '))}</p><p>${esc(authorEvidenceNote(p))}</p>`:/corporate|not_applicable/i.test(p.authors_status)?'<p>Organization-level entry; no single paper byline.</p>':'<p>Author list not yet verified.</p>'}${p.award_result?.evidence_note?`<p>${esc(p.award_result.evidence_note)}</p>`:''}${p.notes.length?`<ul>${p.notes.map(n=>`<li>${esc(n)}</li>`).join('')}</ul>`:''}<p>Checked ${esc(r.checked_on)}. ${p.detailed_paper_id?'Selected manuscript fields checked; see Manuscript details for version-specific values and award evidence.':'Manuscript, performance and award-outcome checks remain separate from this bibliography.'}</p></details></li>`).join('')}</ol></details>`;
  }).join('');
  $('recent-count').textContent=`${matched} of ${total} indexed entries`;
  $('recent-list').innerHTML=html||'<p class="empty">No annual records match these filters.</p>';
}
function rosterCSV() {
  const columns=['record_id','year','conference_year','year_label','entry_type','title_kind','selection_title','publisher_title','doi','doi_status','authors','authors_status','roster_status','title_source_url','preserved_source_reference','doi_resolver_status','doi_resolver_checked_on','award_label','award_category','award_status','award_source_url','award_announcement_date','reviewed_on','program_authors','conference_day_update_status','final_score_status','performance_update_count','performance_update_sources','authors_source_url','bibliography_reviewed_on','bibliography_status','award_outcome','award_announcement_recipients','award_claims_json','award_review_status','award_review_source_url'];
  const rows=rosterVisible.map(p=>[p.id,p.year,p.conference_year,p.year_label,p.entry_type,p.title_kind||'source_title',p.title,p.publisher_title||'',p.doi||'',p.doi_status,p.authors.join('; '),p.authors_status,p.roster_status,p.title_source?.url||'',p.title_source?.local_reference||'',p.doi_verification?.resolver_status||'',p.doi_verification?.resolver_checked_on||'',p.award_result?.label||'',p.award_result?.category||'',p.award_result?.status||'',p.award_source?.url||'',p.award_result?.announcement_date||'',p.postconference_status?.checked_on||'',(p.bibliographic_versions?.find(v=>v.source_id.includes('_program'))?.authors||[]).join('; '),p.postconference_status?.conference_day_update||'',p.postconference_status?.final_score_status||'',p.performance_review?.performance_updates?.length||0,(p.performance_review?.performance_updates||[]).map(u=>u.source_id).join('; '),p.authors_source?.url||'',p.bibliography_review?.checked_on||'',p.bibliography_review?.status||'',p.award_result?.outcome||'',(p.award_result?.recipients||[]).join('; '),p.award_claims?.length?JSON.stringify(p.award_claims):'',p.award_review?.status||'',p.award_review_source?.url||'']);
  const cell=v=>'"'+String(v).replace(/^[=+\-@]/,"'$&").replaceAll('"','""')+'"';
  return '\uFEFF'+[columns,...rows].map(row=>row.map(cell).join(',')).join('\r\n');
}

async function init() {
  try {
    const response = await fetch('data.json?v=year-batch-2006-20261122'); if (!response.ok) throw new Error('Data request failed'); db = await response.json();
    $('catalogue-gaps').textContent='Years with no identified entry: '+(db.catalogue_summary.uncovered_years.join(', ')||'none')+'. Partial lists (further entries or total unconfirmed): '+db.catalogue_summary.partial_years.join(', ')+'. Historical year-label transition: '+db.catalogue_summary.context_years.map(y=>y+' → '+db.year_contexts.find(c=>c.year===y).target_year).join(', ')+'. Indexed years do not imply complete annual rosters.'; $('stat-papers').textContent=db.papers.length; $('stat-roster-years').textContent=db.catalogue_summary.years; $('stat-candidates').textContent=db.catalogue_summary.records; $('stat-dois').textContent=db.catalogue_summary.verified_dois; $('detail-scope').textContent=`${db.papers.length} selected papers · ${db.papers.reduce((n,p)=>n+p.measurements.length,0)} performance observations · ${new Set(db.papers.map(p=>p.year)).size} conference years`;
    fillSelect('paper-year',db.papers.map(p=>String(p.year))); fillSelect('field',db.papers.map(p=>p.field)); fillSelect('machine',db.papers.flatMap(p=>p.machines));
    for (const id of ['paper-year','result','field','machine']) $(id).addEventListener('change',render);
    $('search').addEventListener('input',()=>syncArchiveSearch('search'));
    for(const id of ['list','recent-list','year-coverage','holdings-list']) $(id).addEventListener('click',e=>{const b=e.target.closest('[data-paper]'); if(b) showPaper(b.dataset.paper);});
    $('coverage-view').addEventListener('change',renderYearCoverage);
    $('close').addEventListener('click',()=> $('detail').close());
    $('detail').addEventListener('click',e=>{if(e.target===$('detail')){const r=$('detail').getBoundingClientRect(); if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom) $('detail').close();}});
    $('csv').addEventListener('click',exportCSV);$('bib').addEventListener('click',exportBib);
    $('coverage-links').innerHTML=src(['selection','schedule','awards']);
    $('issues').innerHTML=db.issues.map(i=>`<article class="issue"><span class="tag ${i.state==='Open'||i.state==='Blocked'?'pending':''}">${esc(i.state)}</span><h4>${esc(i.title)}</h4><p>${esc(i.detail)}</p></article>`).join('');
    fillSelect('holdings-year',db.holdings.records.map(r=>String(r.year)));
    $('holdings-search').addEventListener('input',renderHoldings); $('holdings-year').addEventListener('change',renderHoldings);
    fillSelect('recent-year',db.annual_rosters.map(r=>String(r.year))); $('roster-csv').addEventListener('click',()=>download('gordon-bell-candidate-index.csv',rosterCSV(),'text/csv;charset=utf-8'));
    $('recent-search').addEventListener('input',()=>syncArchiveSearch('recent-search')); $('recent-year').addEventListener('change',renderRecent); $('roster-doi').addEventListener('change',renderRecent);
    renderYearCoverage(); renderHoldings(); renderRecent(); render();
  } catch(err) { $('list').innerHTML='<p class="empty">The research records could not be loaded. Please reload the page.</p>'; console.error(err); }
}
init();
