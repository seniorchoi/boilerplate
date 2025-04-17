// Fill prompt textarea with example
function fillPrompt(text) {
    document.getElementById('prompt').value = text;
}

// Copy email to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('Email copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

// Handle form submission with loading state
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#ai-tool-form');
    if (form) {
        form.addEventListener('submit', () => {
            const button = form.querySelector('button[type="submit"]');
            button.disabled = true;
            button.innerText = 'Drafting...';
        });
    }
});