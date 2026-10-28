'use strict';
const langButton=document.getElementById('lang');
const menuButton=document.getElementById('menu-toggle');
const nav=document.getElementById('navigation');
let language='en';
function updateCount(){const visible=[...document.querySelectorAll('.project-card')].filter(c=>!c.hidden).length;document.getElementById('work-count').textContent=language==='ar'?(visible===1?'عمل واحد معروض':`${visible} أعمال معروضة`):`${visible} work sample${visible===1?'':'s'} shown`;}
function setLanguage(lang){language=lang;document.documentElement.lang=lang;document.documentElement.dir=lang==='ar'?'rtl':'ltr';document.querySelectorAll('[data-ar]').forEach(el=>{el.innerHTML=el.dataset[lang]});langButton.textContent=lang==='ar'?'English':'العربية';langButton.setAttribute('aria-label',lang==='ar'?'Switch to English':'التبديل إلى العربية');menuButton.setAttribute('aria-label',lang==='ar'?'قائمة التنقل':'Navigation menu');document.title='محمود الشربيني | Mahmoud Elsherbiny – Finance & Accounting';updateCount();try{localStorage.setItem('melsherbiny-language',lang)}catch(e){}}
langButton.addEventListener('click',()=>setLanguage(language==='ar'?'en':'ar'));
function closeMenu(){nav.classList.remove('open');menuButton.setAttribute('aria-expanded','false');}
menuButton.addEventListener('click',()=>{const open=nav.classList.toggle('open');menuButton.setAttribute('aria-expanded',String(open));});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menuButton.focus();}});
document.addEventListener('click',e=>{if(!e.target.closest('.top'))closeMenu();});
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));document.querySelectorAll('.project-card').forEach(c=>{c.hidden=b.dataset.filter!=='all'&&!c.dataset.category.split(' ').includes(b.dataset.filter);});updateCount();}));
const links=[...nav.querySelectorAll('a')];
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){links.forEach(a=>a.setAttribute('aria-current',String(a.hash==='#'+e.target.id)));}});},{rootMargin:'-15% 0px -65% 0px',threshold:0});
links.forEach(a=>{const el=document.querySelector(a.hash);if(el)observer.observe(el);});
document.getElementById('top').addEventListener('click',()=>window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}));
setLanguage('en');
// Deep links open the associated case so visitors can share a specific achievement.
function revealLinkedCase(){const id=location.hash.slice(1);if(!id.startsWith('case-'))return;const card=document.getElementById(id);if(card){const details=card.querySelector('details');if(details)details.open=true;}}
window.addEventListener('hashchange',revealLinkedCase);revealLinkedCase();
