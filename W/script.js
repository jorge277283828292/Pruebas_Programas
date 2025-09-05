  // ===== Configuración de fecha =====
  const startDate = new Date('2024-06-05T00:00:00');
  const counterEl = document.getElementById('time');
  function updateCounter(){
    const now = new Date();
    const diff = now - startDate;
    const s = Math.floor(diff/1000)%60;
    const m = Math.floor(diff/60000)%60;
    const h = Math.floor(diff/3600000)%24;
    const d = Math.floor(diff/86400000);
    const y = Math.floor(d/365);
    const rd = d%365;
    const pad = n => String(n).padStart(2,'0');
    counterEl.textContent = `${y} años, ${rd} días, ${pad(h)}h ${pad(m)}m ${pad(s)}s`;
  }

  // ===== Cielo día/noche =====
  const starsEl = document.getElementById('stars');
  const sunEl = document.getElementById('sun');
  const moonEl = document.getElementById('moon');

  function populateStars(){
    starsEl.innerHTML='';
    for(let i=0;i<120;i++){
      const s=document.createElement('div'); s.className='star';
      s.style.left= (Math.random()*100)+'%';
      s.style.top= (Math.random()*100)+'%';
      starsEl.appendChild(s);
    }
  }
  function updateSky(){
    const hour = new Date().getHours();
    sunEl.style.display='none'; moonEl.style.display='none'; starsEl.style.display='none';
    if(hour>=6 && hour<18){
      document.body.classList.remove('night');
      sunEl.style.display='block';
    }else{
      document.body.classList.add('night');
      moonEl.style.display='block'; starsEl.style.display='block';
      if(!starsEl.childElementCount) populateStars();
    }
  }

  // ===== Frases al tocar (50% 💗 / 50% emoji aleatorio) =====
  const basePhrases = [
    "Te asmo mucho",
    "Mi terroncito de hormonas",
    "Mi amorsote",
    "Mi vida",
    "Danina JAJAJAJA",
    "Algún día te harás mi esposa",
    "Mi persona favorita en el universo"
  ];
  const altEmojis = ["❤️","💖","💕","💘","💓","💞","🌸","🐻","🌙","⭐","🐣","🐱"];
  const textColors = ["pink","red","violet","skyblue"];

  function randomPhrase(){
    let phrase = basePhrases[Math.floor(Math.random()*basePhrases.length)];
    if(Math.random()>0.5) phrase += " 💗";
    else phrase += " " + altEmojis[Math.floor(Math.random()*altEmojis.length)];
    return phrase;
  }
  function showPhrase(x,y){
    const el = document.createElement('div');
    el.className = 'heartText';
    el.style.left = x+'px'; el.style.top = y+'px';
    el.style.color = textColors[Math.floor(Math.random()*textColors.length)];
    el.textContent = randomPhrase();
    document.body.appendChild(el);
    setTimeout(()=>el.remove(), 2200);
  }
  document.addEventListener('click',(e)=>{
    if(e.target.id==='startBtn') return;
    showPhrase(e.clientX, e.clientY);
    // primer clic también sirve para desbloquear audio:
    if(audioCtx && audioCtx.state === 'suspended'){ audioCtx.resume(); }
  });

  // ===== Pétalos 🌸 en ráfagas (intensidad variable) =====
  function spawnPetal(){
    const p = document.createElement('div');
    p.className='petal';
    p.textContent='🌸';
    p.style.left = (Math.random()*100)+'vw';
    p.style.fontSize = (16 + Math.random()*10) + 'px';
    p.style.animationDuration = (6+Math.random()*4)+'s';
    document.body.appendChild(p);
    setTimeout(()=>p.remove(), 11000);
  }
  setInterval(()=>{
    // ráfaga variable: a veces 0, a veces muchos
    const amount = Math.floor(Math.random()*6); // 0..5
    for(let i=0;i<amount;i++) setTimeout(spawnPetal, i*120);
  }, 650);

  // ===== Música suave con WebAudio (pads + plucks) =====
  let audioCtx=null, masterGain, musicGain, started=false, padsTimer=null, pluckTimer=null;
  function initAudio(){
    if(started) return; started=true;
    audioCtx = new (window.AudioContext||window.webkitAudioContext)();
    masterGain = audioCtx.createGain(); masterGain.gain.value=0.45; masterGain.connect(audioCtx.destination);
    musicGain  = audioCtx.createGain();  musicGain.gain.value=0.28;  musicGain.connect(masterGain);
    startPads(); startPlucks();
  }
  function startPads(){
    const roots = [220, 174.61, 130.81, 196.00]; // A3, F3, C3, G3
    let i=0;
    function chord(root){
      const tones = [root, root*1.5, root*2]; // raíz, quinta, octava
      tones.forEach(f=>{
        const o = audioCtx.createOscillator(); o.type='triangle'; o.frequency.value=f;
        const g = audioCtx.createGain(); g.gain.value=0; o.connect(g); g.connect(musicGain); o.start();
        const t = audioCtx.currentTime;
        g.gain.linearRampToValueAtTime(0.0, t);
        g.gain.linearRampToValueAtTime(0.18, t+2);
        g.gain.linearRampToValueAtTime(0.0, t+12);
        setTimeout(()=>o.stop(), 13000);
      });
    }
    function tick(){ chord(roots[i%roots.length]); i++; }
    tick(); padsTimer = setInterval(tick, 12000);
  }
  function startPlucks(){
    const scale = [220,247,262,294,330,349];
    function pluck(){
      const f = scale[Math.floor(Math.random()*scale.length)] * (Math.random()<0.4?2:1);
      const o = audioCtx.createOscillator(); o.type='sine'; o.frequency.value=f;
      const g = audioCtx.createGain(); g.gain.value=0; const filt = audioCtx.createBiquadFilter(); filt.type='lowpass'; filt.frequency.value=1700;
      o.connect(g); g.connect(filt); filt.connect(musicGain); o.start();
      const t = audioCtx.currentTime;
      g.gain.linearRampToValueAtTime(0.0, t);
      g.gain.linearRampToValueAtTime(0.22, t+0.03);
      g.gain.exponentialRampToValueAtTime(0.001, t+0.8);
      setTimeout(()=>o.stop(), 1100);
    }
    pluck(); pluckTimer = setInterval(()=>{ if(Math.random()<0.6) pluck(); }, 900);
  }

  // Overlay de inicio (requerido por móviles)
  const startOverlay = document.getElementById('start');
  document.getElementById('startBtn').addEventListener('click', async ()=>{
    startOverlay.style.display='none';
    initAudio();
    try{ await audioCtx.resume(); }catch(_){}
  });

  // Kick
  updateCounter(); updateSky();
  setInterval(updateCounter, 1000);
  setInterval(updateSky, 60000);