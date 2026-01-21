async function send() {
  const msg = document.getElementById("msg").value;
  const output = document.getElementById("out");

  try {
    const res = await fetch(
      "https://emotion-adaptive-backend.onrender.com/analyze",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
      }
    );

    if (!res.ok) {
      throw new Error("Server error: " + res.status);
    }

    const data = await res.json();
    output.innerText = JSON.stringify(data, null, 2);

  } catch (err) {
    output.innerText = "❌ Error: " + err.message;
    console.error(err);
  }
}
