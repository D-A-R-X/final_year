async function send() {
  const msg = document.getElementById("msg").value;
  const res = await fetch("https://emotion-adaptive-backend.onrender.com/analyze", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  document.getElementById("out").innerText = JSON.stringify(data, null, 2);
}
