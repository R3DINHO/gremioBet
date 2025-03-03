function apostaRapida(button) {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("apostaRapida-container").style.display = "block";

    let id = button.id; 
    let dadosPartida = document.getElementById("dadosPartida");
    let oddSelecionada = parseInt(button.innerText.trim()); // Valor da odd
    let spanRetornoEsperado = document.getElementById("retornoEsperado");

    // Obtém a partida selecionada com base no ID do botão
    let partidaSelecionada = document.querySelector(`.partida[data-id="${id}"]`);

    // Se a partida selecionada existir, preenche os dados da partida
    if (partidaSelecionada) {
        dadosPartida.innerHTML = `
            <div class="dataPartida">
                <div class="dia">
                    <p>${partidaSelecionada.dataset.dia}</p>
                    <p>${partidaSelecionada.dataset.data}</p>
                </div>
                <div class="hora">
                    <p>${partidaSelecionada.dataset.hora}</p>
                </div>
            </div>
            <div class="times">
                <div class="time">
                    <i class="fa-solid fa-shirt" style="color: ${partidaSelecionada.dataset.corCasa};"></i>
                    <p>${partidaSelecionada.dataset.timeCasa}</p>
                </div>
                <div class="time">
                    <i class="fa-solid fa-shirt" style="color: ${partidaSelecionada.dataset.corFora};"></i>
                    <p>${partidaSelecionada.dataset.timeFora}</p>
                </div>
            </div>
        `;
    }

    // Calcula o retorno esperado com base na odd e no valor apostado
    let valorApostado = pegarValor(); // Chama a função para pegar o valor apostado
    if (!isNaN(oddSelecionada) && !isNaN(valorApostado)) {
        spanRetornoEsperado.innerText = `${oddSelecionada * valorApostado}`; // Exibe o retorno esperado
    } else {
        spanRetornoEsperado.innerText = "Valor inválido!";
    }
}

function pegarValor() {
    let valor = document.getElementById("valorApostado").value.trim(); // Obtém o valor apostado
    let numero = parseInt(valor, 10);  // Converte para inteiro
    return isNaN(numero) ? 0 : numero; // Retorna 0 caso o valor seja inválido
}

function fecharApostaRapida() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("apostaRapida-container").style.display = "none";
}
