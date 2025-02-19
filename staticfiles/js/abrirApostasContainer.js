function abrirApostaContainer(botao) {
    let apostasContainers = document.querySelectorAll("div.apostas-container");
    let idBotao = botao.id;
    let abrirApostaContainer = document.getElementById(idBotao + "-Container");

    apostasContainers.forEach(container => {
        container.style.display = "none";
    }); abrirApostaContainer.style.display = "flex";
}