// Generated from frontend/search/compact-index.mjs by scripts/search_assets.py. Edit the source template.
/** Restore the optional lossless row-value and details.keys string pool. */
export const ROW_STRING_LIMITS=Object.freeze({pool:50000,poolUnits:8200000,stringUnits:1000000,expandedUnits:16400000,nodes:1000000,depth:64,rows:2000});
const ENCODING='shared-raw-strings-v1',PREFIX='~s:';
const own=(value,key)=>Object.prototype.hasOwnProperty.call(value,key);
const plain=value=>value!==null&&typeof value==='object'&&!Array.isArray(value)&&Object.getPrototypeOf(value)===Object.prototype;
const scalarString=value=>typeof value==='string'&&!/[\uD800-\uDFFF]/u.test(value);
const invalid=()=>{throw Error('Invalid pooled row strings');};
const ROW_LITERAL='scalar-bijection-v1',ROW_LITERAL_ALPHABET_LIMIT=8192;
/** The marked subset has stricter traversal limits; the writer falls back unmarked. */
export function restoreRowLiterals(data){
 if(!data||typeof data!=='object')return data;
 if(!own(data,'row_literal_encoding')){if(own(data,'row_literal_alphabet'))invalid();return data;}
 if(!plain(data)||data.format!=='compact-search-v1'||!['atlas','site'].includes(data.kind)||
    data.row_literal_encoding!==ROW_LITERAL||!own(data,'row_literal_alphabet')||
    data.row_string_encoding!==ENCODING||data.row_structure_encoding!=='key-shapes-v1')invalid();
 const table=data.row_literal_alphabet;
 if(!scalarString(table)||table.length>2*ROW_LITERAL_ALPHABET_LIMIT)invalid();
 const alphabet=Array.from(table);
 if(!alphabet.length||alphabet.length>ROW_LITERAL_ALPHABET_LIMIT||new Set(alphabet).size!==alphabet.length)invalid();
 const dense=x=>Array.isArray(x)&&Object.getPrototypeOf(x)===Array.prototype;
 const field=data.kind==='atlas'?'entries':'documents';
 if(!own(data,field)||!own(data,'row_strings')||!own(data,'row_shapes')||
    !plain(data.details)||!own(data.details,'keys'))invalid();
 const roots=[[field,data[field]],['row_strings',data.row_strings],['row_shapes',data.row_shapes],['details.keys',data.details.keys]];
 if(roots.some(([,v])=>!dense(v))||data[field].length>ROW_STRING_LIMITS.rows||
    data.row_strings.length>ROW_STRING_LIMITS.pool||data.row_shapes.length>ROW_STRING_LIMITS.pool)invalid();
 const counts=new Array(alphabet.length).fill(0),rootUnits=new Map();
 let nodes=0,total=0;
 const index=c=>{const cp=c.codePointAt(0);return cp>=32&&cp<=126?alphabetASCII.indexOf(c):cp>=128?alphabetASCII.length+cp-128:-1;};
 // Validate the entire encoded forest before allocating any reconstructed root/string.
 const scan=(value,depth,root)=>{
  if(++nodes>ROW_STRING_LIMITS.nodes||depth>ROW_STRING_LIMITS.depth)invalid();
  if(depth===1&&root===field&&!dense(value))invalid();
  if(depth===1&&['row_strings','details.keys'].includes(root)&&typeof value!=='string')invalid();
  if(root==='row_shapes'&&((depth===1&&!dense(value))||(depth>=2&&typeof value!=='string')))invalid();
  if(typeof value==='string'){
   if(!scalarString(value))invalid();let size=0;
   for(const c of value){
    const i=index(c);if(i<0||i>=alphabet.length)invalid();
    const units=alphabet[i].length;size+=units;total+=units;
    const subtotal=(rootUnits.get(root)||0)+units;rootUnits.set(root,subtotal);
    if(total>ROW_STRING_LIMITS.expandedUnits||
       (['row_strings','row_shapes'].includes(root)&&subtotal>ROW_STRING_LIMITS.poolUnits)||
       (root==='row_strings'&&size>ROW_STRING_LIMITS.stringUnits))invalid();
    counts[i]++;
   }
  }else if(Array.isArray(value)){
   if(!dense(value)||value.length>ROW_STRING_LIMITS.nodes-nodes)invalid();
   for(let i=0;i<value.length;i++){if(!own(value,i))invalid();scan(value[i],depth+1,root);}
  }else if(value!==null&&typeof value!=='boolean'&&(typeof value!=='number'||!Number.isFinite(value)))invalid();
 };
 for(const [root,value]of roots)scan(value,0,root);
 for(let i=0;i<alphabet.length;i++)if(!counts[i]||(i&&(counts[i]>counts[i-1]||
    (counts[i]===counts[i-1]&&alphabet[i].codePointAt(0)<alphabet[i-1].codePointAt(0)))))invalid();
 const mapped=value=>{
  if(typeof value==='string'){const out=[];for(const c of value)out.push(alphabet[index(c)]);return out.join('');}
  return Array.isArray(value)?value.map(mapped):value;
 };
 const {row_literal_encoding,row_literal_alphabet,...header}=data;
 return {...header,[field]:mapped(data[field]),row_strings:mapped(data.row_strings),row_shapes:mapped(data.row_shapes),
  details:{...data.details,keys:mapped(data.details.keys)}};
}
/** Restore only the optional pool storage; reference IDs and all budgets stay fixed. */
export function restoreRowPool(data){
 data=restoreRowLiterals(data);
 if(!data||typeof data!=='object')return data;
 if(!own(data,'row_pool_encoding')){if(own(data,'row_pool_prefixes'))invalid();return data;}
 if(!plain(data)||data.format!=='compact-search-v1'||!['atlas','site'].includes(data.kind)||data.row_string_encoding!==ENCODING||data.row_pool_encoding!=='unicode-prefix-columns-v1')invalid();
 const suffixes=data.row_strings,value=data.row_pool_prefixes;
 if(!Array.isArray(suffixes)||Object.getPrototypeOf(suffixes)!==Array.prototype||suffixes.length>ROW_STRING_LIMITS.pool||typeof value!=='string'||value.length>4*Math.ceil(4*ROW_STRING_LIMITS.pool/3)||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(value))invalid();
 const raw=atob(value);if(btoa(raw)!==value)invalid();
 const prefixes=[];let number=0,factor=1,bytes=0;
 for(let i=0;i<raw.length;i++){
  const byte=raw.charCodeAt(i);number+=(byte%128)*factor;bytes++;
  if(number>ROW_STRING_LIMITS.stringUnits||bytes>4)invalid();
  if(byte<128){
   if(bytes>1&&byte===0)invalid();prefixes.push(number);if(prefixes.length>suffixes.length)invalid();
   number=0;factor=1;bytes=0;
  }else factor*=128;
 }
 if(bytes||prefixes.length!==suffixes.length)invalid();
 const pool=[],seen=new Set();let previous=[],units=0;
 for(let i=0;i<suffixes.length;i++){
  if(!own(suffixes,i)||!scalarString(suffixes[i]))invalid();
  const prefix=prefixes[i],suffix=suffixes[i];if(prefix>previous.length||suffix.length>ROW_STRING_LIMITS.stringUnits||suffix.length>ROW_STRING_LIMITS.poolUnits-units)invalid();
  let length=suffix.length;
  for(let j=0;j<prefix;j++){length+=previous[j].length;if(length>ROW_STRING_LIMITS.stringUnits||length>ROW_STRING_LIMITS.poolUnits-units)invalid();}
  const text=previous.slice(0,prefix).join('')+suffix;
  if(seen.has(text))invalid();seen.add(text);units+=length;
  pool.push(text);previous=Array.from(text);
 }
 const {row_pool_encoding,row_pool_prefixes,...header}=data;
 return {...header,row_strings:pool};
}
/** Restore dictionary key order and arrays without reference expansion. */
export function restoreRowShapes(data){
 data=restoreRowLiterals(data);
 if(!data||typeof data!=='object')return data;
 if(data.row_structure_encoding===undefined){if(own(data,'row_shapes'))invalid();return data;}
 if(!plain(data)||data.format!=='compact-search-v1'||!['atlas','site'].includes(data.kind)||data.row_structure_encoding!=='key-shapes-v1')invalid();
 const shapes=data.row_shapes,seen=new Set(),used=new Set();let schemaUnits=0,schemaKeys=0;
 const dense=a=>Array.isArray(a)&&Object.getPrototypeOf(a)===Array.prototype;
 if(!dense(shapes)||shapes.length>ROW_STRING_LIMITS.pool)invalid();
 for(let i=0;i<shapes.length;i++){
  if(!own(shapes,i)||!dense(shapes[i])||shapes[i].length>ROW_STRING_LIMITS.nodes-schemaKeys)invalid();
  const keys=shapes[i],names=new Set();schemaKeys+=keys.length;
  for(let j=0;j<keys.length;j++){
   if(!own(keys,j)||!scalarString(keys[j])||names.has(keys[j]))invalid();
   names.add(keys[j]);schemaUnits+=keys[j].length;if(schemaUnits>ROW_STRING_LIMITS.poolUnits)invalid();
  }
  const signature=JSON.stringify(keys);if(seen.has(signature))invalid();seen.add(signature);
 }
 const field=data.kind==='atlas'?'entries':'documents',packed=data[field];
 if(!dense(packed)||packed.length>ROW_STRING_LIMITS.rows)invalid();
 let nodes=0,units=0;
 const charge=s=>{if(!scalarString(s))invalid();units+=s.length;if(units>ROW_STRING_LIMITS.expandedUnits)invalid();return s;};
 const visit=(value,depth=0)=>{
  if(++nodes>ROW_STRING_LIMITS.nodes||depth>ROW_STRING_LIMITS.depth)invalid();
  if(Array.isArray(value)){
   if(!dense(value)||!value.length||!own(value,0)||!Number.isInteger(value[0])||value.length-1>ROW_STRING_LIMITS.nodes-nodes)invalid();
   const tag=value[0];for(let i=1;i<value.length;i++)if(!own(value,i))invalid();
   if(tag===-1)return value.slice(1).map(v=>visit(v,depth+1));
   if(tag<0||tag>=shapes.length||value.length!==shapes[tag].length+1)invalid();
   used.add(tag);
   return Object.fromEntries(shapes[tag].map((key,i)=>[charge(key),visit(value[i+1],depth+1)]));
  }
  if(typeof value==='string')return charge(value);
  if(value!==null&&typeof value!=='boolean'&&(typeof value!=='number'||!Number.isFinite(value)))invalid();
  return value;
 };
 const rows=[];
 for(let i=0;i<packed.length;i++){
  if(!own(packed,i)||!dense(packed[i])||!Number.isInteger(packed[i][0])||packed[i][0]<0)invalid();
  rows.push(visit(packed[i]));
 }
 if(used.size!==shapes.length)invalid();
 const {row_structure_encoding,row_shapes,...header}=data;
 return {...header,[field]:rows};
}
export function restoreRowStrings(data){
 data=restoreRowPool(data);
 data=restoreRowShapes(data);
 if(!data||typeof data!=='object')return data;
 if(data.row_string_encoding===undefined){
  if(own(data,'row_strings'))invalid();
  return data; // Old compact and already-unpacked payloads retain their API.
 }
 if(!plain(data)||data.format!=='compact-search-v1'||data.row_string_encoding!==ENCODING||!['atlas','site'].includes(data.kind))invalid();
 const pool=data.row_strings;
 if(!Array.isArray(pool)||Object.getPrototypeOf(pool)!==Array.prototype||pool.length>ROW_STRING_LIMITS.pool)invalid();
 let poolUnits=0;
 const seen=new Set();
 for(const text of pool){
  if(!scalarString(text)||text.length>ROW_STRING_LIMITS.stringUnits||seen.has(text))invalid();
  seen.add(text);poolUnits+=text.length;if(poolUnits>ROW_STRING_LIMITS.poolUnits)invalid();
 }
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||Object.getPrototypeOf(data[field])!==Array.prototype||data[field].length>ROW_STRING_LIMITS.rows)invalid();
 for(let i=0;i<data[field].length;i++)if(!own(data[field],i)||!plain(data[field][i]))invalid();
 let nodes=0,units=0;
 const charge=text=>{units+=text.length;if(units>ROW_STRING_LIMITS.expandedUnits)invalid();return text;};
 const restore=(value,depth=0)=>{
  if(++nodes>ROW_STRING_LIMITS.nodes||depth>ROW_STRING_LIMITS.depth)invalid();
  if(typeof value==='string'){
   if(!scalarString(value))invalid();
   if(!value.startsWith(PREFIX))return charge(value);
   const suffix=value.slice(PREFIX.length);
   if(suffix.startsWith('~'))return charge(PREFIX+suffix.slice(1));
   if(!/^(?:0|[1-9a-z][0-9a-z]{0,3})$/.test(suffix))invalid();
   const index=parseInt(suffix,36);
   if(index>=pool.length||index.toString(36)!==suffix)invalid();
   // Pool entries are raw strings, never recursively interpreted as tokens.
   return charge(pool[index]);
  }
  if(Array.isArray(value)){
   if(Object.getPrototypeOf(value)!==Array.prototype||value.length>ROW_STRING_LIMITS.nodes-nodes)invalid();
   const result=[];
   for(let i=0;i<value.length;i++){if(!own(value,i))invalid();result.push(restore(value[i],depth+1));}
   return result;
  }
  if(value&&typeof value==='object'){
   if(!plain(value))invalid();
   // CreateDataProperty preserves an own '__proto__' key without invoking a setter.
   return Object.fromEntries(Object.entries(value).map(([key,item])=>{if(!scalarString(key))invalid();charge(key);return [key,restore(item,depth+1)];}));
  }
  if(value!==null&&typeof value!=='boolean'&&(typeof value!=='number'||!Number.isFinite(value)))invalid();
  return value;
 };
 const rows=data[field].map(row=>restore(row));
 const {row_string_encoding,row_strings,...header}=data;
 const result={...header,[field]:rows};
 if(own(data,'details')){
  if(!plain(data.details))invalid();
  if(own(data.details,'keys')){
   if(!Array.isArray(data.details.keys)||data.details.keys.some(key=>typeof key!=='string'))invalid();
   const keys=restore(data.details.keys);
   result.details={...data.details,keys};
  }
 }
 return result;
}

/** Decode a fixed public vocabulary; fetch only fixed same-site detail assets. */
const decoded=new WeakMap(),pending=new Map();
const MAX_TERMS=500000,MAX_VOCABULARY_UNITS=8200000;
const ALPHABET='unicode-prefix-alphabet-v1';
const ALPHABET_COLUMNS='unicode-prefix-alphabet-columns-v1';
export const VOCABULARY_ALPHABET_LIMIT=8192;
const alphabetASCII=Array.from({length:95},(_,i)=>String.fromCharCode(i+32)).filter(c=>c!=='"'&&c!=='\\');
function suffixAlphabet(data){
 const fail=()=>{throw Error('Invalid vocabulary alphabet');};
 const value=data.vocabulary_alphabet;
 if(!plain(data)||data.format!=='compact-search-v1'||!['atlas','site'].includes(data.kind)||typeof value!=='string'||value.length>2*VOCABULARY_ALPHABET_LIMIT||!scalarString(value))fail();
 const symbols=Array.from(value);
 if(!symbols.length||symbols.length>VOCABULARY_ALPHABET_LIMIT||new Set(symbols).size!==symbols.length)fail();
 const counts=new Array(symbols.length).fill(0);
 return {
  decode(value,remaining){
   if(typeof value!=='string'||!scalarString(value))fail();
   const out=[];let units=0;
   for(const character of value){
    const cp=character.codePointAt(0);
    const index=cp>=32&&cp<=126?alphabetASCII.indexOf(character):cp>=128?alphabetASCII.length+cp-128:-1;
    if(index<0||index>=symbols.length)fail();
    const symbol=symbols[index];units+=symbol.length;
    if(units>remaining)fail();
    out.push(symbol);counts[index]++;
   }
   return out.join('');
  },
  finish(){
   for(let i=0;i<symbols.length;i++){
    if(!counts[i]||(i&&(counts[i]>counts[i-1]||(counts[i]===counts[i-1]&&symbols[i].codePointAt(0)<symbols[i-1].codePointAt(0)))))fail();
   }
  }
 };
}
function vocabularyColumns(data){
 const fail=()=>{throw Error('Invalid vocabulary columns');};
 const suffixes=data.terms,value=data.vocabulary_prefixes;
 if(!plain(data)||!Array.isArray(suffixes)||Object.getPrototypeOf(suffixes)!==Array.prototype||suffixes.length>MAX_TERMS||typeof value!=='string'||value.length>4*Math.ceil(4*MAX_TERMS/3)||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(value))fail();
 const raw=atob(value);if(btoa(raw)!==value)fail();
 const prefixes=[];let number=0,factor=1,bytes=0;
 for(let i=0;i<raw.length;i++){
  const byte=raw.charCodeAt(i);number+=(byte%128)*factor;bytes++;
  if(number>MAX_VOCABULARY_UNITS||bytes>4)fail();
  if(byte<128){
   if(bytes>1&&byte===0)fail();prefixes.push(number);if(prefixes.length>suffixes.length)fail();
   number=0;factor=1;bytes=0;
  }else factor*=128;
 }
 if(bytes||prefixes.length!==suffixes.length)fail();
 const packed=[];
 for(let i=0;i<suffixes.length;i++){if(!own(suffixes,i))fail();packed.push(prefixes[i],suffixes[i]);}
 return packed;
}
function vocabulary(data){
 const columns=data.vocabulary_encoding===ALPHABET_COLUMNS;
 if(!columns&&own(data,'vocabulary_prefixes'))throw Error('Invalid vocabulary columns');
 const packed=columns?vocabularyColumns(data):data.terms,alphabet=[ALPHABET,ALPHABET_COLUMNS].includes(data.vocabulary_encoding)?suffixAlphabet(data):null;
 if(!alphabet&&own(data,'vocabulary_alphabet'))throw Error('Invalid vocabulary alphabet');
 if(!Array.isArray(packed))throw Error('Invalid search vocabulary');
 if(data.vocabulary_encoding===undefined){
  if(packed.length>MAX_TERMS||packed.some(word=>typeof word!=='string'))throw Error('Invalid search vocabulary');
  return packed;
 }
 if(!['unicode-prefix-flat-v1',ALPHABET,ALPHABET_COLUMNS].includes(data.vocabulary_encoding)||packed.length%2||packed.length>2*MAX_TERMS)throw Error('Invalid search vocabulary');
 const words=[];let previous=[],units=0;
 for(let i=0;i<packed.length;i+=2){
  const prefix=packed[i];
  const suffix=alphabet?alphabet.decode(packed[i+1],MAX_VOCABULARY_UNITS-units):packed[i+1];
  if(!Number.isInteger(prefix)||prefix<0||prefix>previous.length||typeof suffix!=='string'||/[\uD800-\uDFFF]/u.test(suffix))throw Error('Invalid search vocabulary');
  if(suffix.length>MAX_VOCABULARY_UNITS-units)throw Error('Invalid search vocabulary');
  if(alphabet){
   let wordUnits=suffix.length;
   for(let j=0;j<prefix;j++){wordUnits+=previous[j].length;if(wordUnits>MAX_VOCABULARY_UNITS-units)throw Error('Invalid search vocabulary');}
  }
  // Python len/slicing count Unicode code points, unlike JS string offsets.
  const points=previous.slice(0,prefix).concat(Array.from(suffix)),word=points.join('');
  units+=word.length;if(units>MAX_VOCABULARY_UNITS)throw Error('Invalid search vocabulary');
  words.push(word);previous=points;
 }
 if(alphabet)alphabet.finish();
 return words;
}
function varints(value,limit){
 if(typeof value!=='string'||value.length>4*MAX_TERMS||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(value))throw Error('Invalid search terms');
 const raw=atob(value);
 if(btoa(raw)!==value)throw Error('Invalid search terms');
 const values=[];let number=0,factor=1,bytes=0;
 for(let i=0;i<raw.length;i++){
  const byte=raw.charCodeAt(i);number+=(byte%128)*factor;bytes++;
  if(number>=limit||bytes>3)throw Error('Invalid search terms');
  if(byte<128){
   if(bytes>1&&byte===0)throw Error('Invalid search terms');
   values.push(number);if(values.length>MAX_TERMS)throw Error('Invalid search terms');
   number=0;factor=1;bytes=0;
  }else factor*=128;
 }
 if(bytes)throw Error('Invalid search terms');
 return values;
}
// Posting-list limits bound both wire decoding and repeated-class expansion.
// They apply only to this optional codec; old indexes retain their loader API.
export const TERM_MEMBERSHIP_LIMITS=Object.freeze({channels:8000,memberships:2000000,textUnits:16400000,encodedUnits:16000000});
const INVERTED='inverted-membership-varint-base64-v1';
const membershipKeys=['term_channel_count','term_membership_ids','term_membership_classes'];
function invertTerms(data,words,field){
 const fail=()=>{throw Error('Invalid inverted search terms');};
 if(!plain(data)||!Array.isArray(data[field])||Object.getPrototypeOf(data[field])!==Array.prototype||data[field].length>2000)fail();
 const count=data.term_channel_count,packed=data.term_membership_classes;
 if(!Number.isInteger(count)||count<0||count>TERM_MEMBERSHIP_LIMITS.channels||!Array.isArray(packed)||Object.getPrototypeOf(packed)!==Array.prototype||packed.length>MAX_TERMS)fail();
 const channels=Array.from({length:count},()=>[]),seen=new Set();
 let encodedUnits=0,classMembers=0,expanded=0,textUnits=0;
 const referencedChannels=new Set();
 const classes=packed.map(value=>{
  if(typeof value!=='string'||seen.has(value))fail();
  seen.add(value);encodedUnits+=value.length;if(encodedUnits>TERM_MEMBERSHIP_LIMITS.encodedUnits)fail();
  let previous=0;
  const ids=varints(value,count).map((delta,i)=>{
   if(i&&delta===0)fail();
   previous+=delta;if(previous>=count)fail();return previous;
  });
  classMembers+=ids.length;if(classMembers>TERM_MEMBERSHIP_LIMITS.memberships)fail();return ids;
 });
 const ids=varints(data.term_membership_ids,classes.length);
 if(ids.length!==words.length)fail();
 const used=new Set();
 for(let term=0;term<ids.length;term++){
  const id=ids[term];used.add(id);
  for(const channel of classes[id]){
   if(++expanded>TERM_MEMBERSHIP_LIMITS.memberships)fail();
   textUnits+=words[term].length+(channels[channel].length?1:0);
   if(textUnits>TERM_MEMBERSHIP_LIMITS.textUnits)fail();
   channels[channel].push(words[term]);
  }
 }
 if(used.size!==classes.length)fail();
 const text=reference=>{
  // References form a bijection. Python and JS enumerate integer-like object
  // keys differently, so row/language enumeration need not equal channel order.
  if(!Number.isInteger(reference)||reference<0||reference>=count||referencedChannels.has(reference))fail();
  referencedChannels.add(reference);return channels[reference].join(' ');
 };
 const rows=[];
 for(let i=0;i<data[field].length;i++){
  const row=data[field][i];if(!own(data[field],i)||!plain(row))fail();
  const value=row.search_terms;
  const searchText=typeof value==='number'?text(value):plain(value)?Object.fromEntries(Object.entries(value).map(([language,reference])=>{
   if(!scalarString(language))fail();return [language,text(reference)];
  })):fail();
  const {search_terms,...record}=row;rows.push({...record,search_text:searchText});
 }
 if(referencedChannels.size!==count)fail();
 return rows;
}
export function unpackSearchIndex(data){
 if(data?.format!=='compact-search-v1'){
  if(data&&typeof data==='object'&&('row_string_encoding' in data||'row_strings' in data||own(data,'row_literal_encoding')||own(data,'row_literal_alphabet')||own(data,'row_pool_encoding')||own(data,'row_pool_prefixes')||own(data,'row_structure_encoding')||own(data,'row_shapes')||own(data,'vocabulary_prefixes')||own(data,'vocabulary_alphabet')||[ALPHABET,ALPHABET_COLUMNS].includes(data.vocabulary_encoding)||membershipKeys.some(key=>own(data,key))))throw Error('Invalid pooled row strings');
  return data;
 }
 if(decoded.has(data))return decoded.get(data);
 const source=data;data=restoreRowStrings(data);
 const words=vocabulary(data),binary=data.term_encoding==='sorted-delta-varint-base64',inverted=data.term_encoding===INVERTED;
 if(data.term_encoding!==undefined&&!['sorted-delta','sorted-delta-varint-base64',INVERTED].includes(data.term_encoding))throw Error('Invalid search terms');
 if(!inverted&&membershipKeys.some(key=>own(data,key)))throw Error('Invalid inverted search terms');
 const expand=indices=>{
  if(binary)indices=varints(indices,words.length);
  if(!Array.isArray(indices))throw Error('Invalid search terms');
  let previous=0;
  return indices.map((delta,position)=>{
   if(!Number.isInteger(delta)||delta<0)throw Error('Invalid search terms');
   if(binary&&position>0&&delta===0)throw Error('Invalid search terms');
   const index=binary||data.term_encoding==='sorted-delta'?previous+delta:delta;previous=index;
   if(index>=words.length)throw Error('Invalid search terms');
   return words[index];
  }).join(' ');
 };
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||data[field].length>2000)throw Error('Invalid search records');
 const rows=inverted?invertTerms(data,words,field):data[field].map(row=>{
  const terms=row.search_terms;
  const searchText=Array.isArray(terms)||typeof terms==='string'?expand(terms):Object.fromEntries(Object.entries(terms||{}).map(([language,ids])=>[language,expand(ids)]));
  const {search_terms,...record}=row;return {...record,search_text:searchText};
 });
 const {terms,vocabulary_encoding,vocabulary_alphabet,vocabulary_prefixes,term_channel_count,term_membership_ids,term_membership_classes,...rest}=data;
 // Preserve the legacy unpacked record/header API; storage codecs are private
 // to this loader. Both old numeric arrays and the new byte strings decode here.
 if(binary||inverted)rest.term_encoding='sorted-delta';
 const result={...rest,format:'unpacked-search-v1',[field]:rows};decoded.set(source,result);return result;
}
export function searchDetailURL(key){
 if(typeof key!=='string'||! /^[a-f0-9]{64}$/.test(key))throw Error('Invalid search detail key');
 return new URL('./details/'+key+'.json',import.meta.url);
}
export function loadSearchDetail(key){
 const url=searchDetailURL(key);
 if(!pending.has(key))pending.set(key,fetch(url,{credentials:'omit'}).then(response=>{
  if(!response.ok)throw Error('Search detail unavailable');return response.json();
 }).then(data=>{if(!data||typeof data!=='object'||Array.isArray(data))throw Error('Invalid search detail');return data;}).catch(error=>{pending.delete(key);throw error;}));
 return pending.get(key);
}
