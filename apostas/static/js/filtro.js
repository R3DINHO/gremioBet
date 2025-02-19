function filtrar(botaoSelecionado){
    let botoes = document.querySelectorAll('.filtro-list button');
    let selected = "";
    
    // Itera sobre os botões e remove todas as classes
    botoes.forEach(function(botao) {
        botao.classList.remove(...botao.classList);  // Remove todas as classes do botão
    });

    botaoSelecionado.classList.add('filtroSelecionado');
    let idBotao = botaoSelecionado.id ;
    selected = idBotao;

    if (selected == "nenhum"){
        document.getElementById("misto").style.display = "block";
        document.getElementById("feminino").style.display = "block";
    } else if (selected == "mistoButton"){
        document.getElementById("misto").style.display = "block";
        document.getElementById("feminino").style.display = "none";
    } else if (selected == "femininoButton"){
        document.getElementById("misto").style.display = "none";
        document.getElementById("feminino").style.display = "block";
    }

}