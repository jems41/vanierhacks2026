const res = await fetch("http://ctf26.vanierhacks.net/ALSS/cpu1");
const data = await res.json();

console.log(data);