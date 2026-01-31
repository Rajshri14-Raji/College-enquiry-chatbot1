function addMessage(text, className) {
    const chat = document.getElementById("chat-area");
    const msg = document.createElement("div");
    msg.className = "message " + className;
    msg.innerText = text;
    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    addMessage("👤 " + message, "user");
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("🤖 " + data.reply, "bot");
    });
}

function sendQuick(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}

/* ✅ ADD THIS AT THE VERY BOTTOM (OUTSIDE FUNCTIONS) */
document.getElementById("user-input").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
function showSection(sectionId) {
    const container = document.getElementById("info-section");
    const sections = document.querySelectorAll(".info-content");

    // Show container
    container.style.display = "block";

    // Hide all sections
    sections.forEach(sec => sec.style.display = "none");

    // Show selected section
    document.getElementById(sectionId).style.display = "block";

    // Scroll to section smoothly
    container.scrollIntoView({ behavior: "smooth" });
}
