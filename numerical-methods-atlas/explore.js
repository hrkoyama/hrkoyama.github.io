// Open the field selected by a preserved bookmark; every panel also works
// through its native details/summary control without JavaScript.
function revealField() {
 let id;
 try { id=decodeURIComponent(location.hash.slice(1)); } catch { return; }
 const panel=document.getElementById(id);
 if(panel?.matches('details[data-static-area]'))panel.open=true;
}
revealField();
window.addEventListener('hashchange',revealField);
