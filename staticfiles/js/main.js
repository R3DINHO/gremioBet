// senha

let passwordInputs = document.querySelectorAll('.password-container input');

passwordInputs.forEach(function(input) {
    input.addEventListener('copy', function(event) {
        event.preventDefault(); 
    });

    input.addEventListener('paste', function(event) {
        event.preventDefault(); 
    });
});



// selecionar imagem de perfil
const radioButtons = document.querySelectorAll('input[type="radio"]');

radioButtons.forEach(radio => {
    radio.addEventListener('change', function() {
        const imageContainers = document.querySelectorAll('.image-container');
        imageContainers.forEach(container => {
            container.style.border = '2px solid transparent'; // Borda invisível
        });

        const selectedLabel = this.closest('label');
        const selectedContainer = selectedLabel.querySelector('.image-container');
        selectedContainer.style.border = '2px solid #e46e00'; // Cor da borda
    });
});

// menu Usuário

function menuUsuario(){
    let divMenu = document.getElementById("menuUsuarioAbsolute");
    
    if(!divMenu.classList.contains("visivel")){
        divMenu.classList.remove("invisivel")
        divMenu.classList.add("visivel")
    }
    else if(divMenu.classList.contains("visivel")){
        divMenu.classList.remove("visivel")
        divMenu.classList.add("invisivel")

    }

}