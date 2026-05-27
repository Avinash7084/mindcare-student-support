async function sendMessage() {
    const input = document.getElementById('userMsg');
    const chat = document.getElementById('chat-window');
    const msg = input.value.trim();
    
    if (!msg) return;

    // 1. Display User Bubble
    chat.innerHTML += `<div class="chat-msg user-msg">${msg}</div>`;
    input.value = ''; // Clear input
    chat.scrollTop = chat.scrollHeight;

    // 2. Show "MindCare is typing..."
    const typingId = "typing-" + Date.now();
    chat.innerHTML += `<div id="${typingId}" class="typing-text"><em>MindCare is typing...</em></div>`;
    chat.scrollTop = chat.scrollHeight;

    try {
        const response = await fetch('/chatbot/', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json', 
                'X-CSRFToken': '{{ csrf_token }}' 
            },
            body: JSON.stringify({ message: msg })
        });
        
        const data = await response.json();

        // 3. Natural Delay (Simulating "thinking" time)
        // We delay the response by 1 second to feel human
        setTimeout(() => {
            const typingElem = document.getElementById(typingId);
            if (typingElem) typingElem.remove();

            chat.innerHTML += `<div class="chat-msg bot-msg">${data.response}</div>`;
            chat.scrollTop = chat.scrollHeight;
        }, 1000);

    } catch (error) {
        console.error("Error:", error);
        document.getElementById(typingId).innerHTML = "<em>Connection error. Please try again.</em>";
    }
}