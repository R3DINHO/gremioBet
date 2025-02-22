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


// Seleciona todos os inputs do tipo radio
const radioButtons = document.querySelectorAll('input[type="radio"]');

// Para cada botão de rádio
radioButtons.forEach(radio => {
    // Adiciona um event listener para quando o radio for alterado
    radio.addEventListener('change', function() {
        // Remove a borda de todos os containers de imagem
        const imageContainers = document.querySelectorAll('.image-container');
        imageContainers.forEach(container => {
            container.style.border = '2px solid transparent'; // Borda invisível
        });

        // Adiciona a borda no contêiner de imagem selecionado
        const selectedLabel = this.closest('label');
        const selectedContainer = selectedLabel.querySelector('.image-container');
        selectedContainer.style.border = '2px solid #e46e00'; // Cor da borda
    });
});

