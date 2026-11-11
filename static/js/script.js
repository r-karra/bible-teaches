document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatHistory = document.querySelector('.chat-history');

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value;
        if (userMessage.trim() !== '') {
            appendMessage('user', userMessage);
            userInput.value = '';
            // Here you would typically send the message to the backend
            // and receive a response from the Gemini AI
            // For now, we'll just simulate a response.
            setTimeout(() => {
                appendMessage('bot', 'This is a simulated response from Gemini.');
            }, 1000);
        }
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = message;
        chatHistory.appendChild(messageElement);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
});
