const today = new Date();
const mmdd = today.toISOString().slice(5, 10);

async function loadMemory() {
  const res = await fetch('data/memory.json');
  const memories = await res.json();
  const match = memories.find(mem => mem.date === mmdd);
  

  const memoryBox = document.getElementById("memory-box");
  
  if (match) {
    memoryBox.innerHTML = `
      <h3>${match.year}: ${match.text}</h3>
      <img src="images/${match.image}" width="300" />
    `;
  } else {
    memoryBox.innerText = "No memory found for today";
  }
}


if (document.getElementById("memory-box")) {
  loadMemory();
}