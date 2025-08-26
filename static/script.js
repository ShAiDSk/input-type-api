async function checkInput() {
  const input = document.getElementById("userInput").value;
  if (!input) {
    document.getElementById("result").innerHTML = "⚠️ Please enter a value.";
    return;
  }

  const response = await fetch("/api/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input: input })
  });

  const data = await response.json();
  document.getElementById("result").innerHTML =
    `✅ Input: <span class="text-blue-400">${data.input}</span><br>
     📌 Detected Type: <span class="text-green-400">${data.type}</span>`;
}
