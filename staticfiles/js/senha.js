let passwordInputs = document.querySelectorAll('.password-container input');

passwordInputs.forEach(function(input) {
    // Bloquear o evento de copiar (Ctrl+C)
    input.addEventListener('copy', function(event) {
        event.preventDefault(); // Impede a ação de copiar
    });

    // Bloquear o evento de colar (Ctrl+V)
    input.addEventListener('paste', function(event) {
        event.preventDefault(); // Impede a ação de colar
    });
});
