async function send() {
  const input = document.getElementById("msg");
  const chatBox = document.getElementById("chat-box");
  const button = document.querySelector("button");

  const message = input.value.trim();
  if (!message) return;

  // User message
  chatBox.innerHTML += `
    <div class="message user">You: ${message}</div>
  `;
  chatBox.scrollTop = chatBox.scrollHeight;

  input.value = "";
  button.disabled = true;

  // Bot thinking
  const thinkingId = Date.now();
  chatBox.innerHTML += `
    <div class="message bot" id="${thinkingId}">Bot: thinking...</div>
  `;
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch(
      "https://emotion-adaptive-backend.onrender.com/analyze",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      }
    );

    const data = await res.json();

    document.getElementById(thinkingId).innerHTML = `
      <div class="bot">
        Bot: ${data.response}
        <div class="meta">
          Emotion: ${data.emotion} | Engagement: ${data.engagement}
        </div>
      </div>
    `;

  } catch (err) {
    document.getElementById(thinkingId).innerText =
      "❌ Error contacting server";
  }

  button.disabled = false;
}
