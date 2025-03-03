let oddSelecionada = 0;

function apostaRapida(button) {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("apostaRapida-container").style.display = "flex";

    let id = button.id; 
    let dadosPartida = document.getElementById("dadosPartida");

    oddSelecionada = getButtonNumber(button); 
    document.getElementById("exibirOdd").innerText = `Odd: ${oddSelecionada}x`;

    let partidaSelecionada = document.querySelector(`.partida[data-id="${id}"]`);

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

    opcaoAposta(button);
    atualizarRetorno();    

}

function getButtonNumber(button) {
    let clone = button.cloneNode(true);
    clone.querySelectorAll("span").forEach(span => span.remove());
    return parseFloat(clone.textContent.trim()) || 0;
}

function opcaoAposta(button) {
    let opcaoAposta = document.getElementById("opcaoAposta");

    if (button.classList.contains("oddsEmpate")) {
        opcaoAposta.innerText = `em um EMPATE nessa partida`;
    } else if (button.classList.contains("oddsCasa") || button.classList.contains("oddsFora")) {
        if (button.classList.length >= 3) {
            let equipe = Array.from(button.classList).slice(2).join(" ");
            opcaoAposta.innerText = `na Vitória de ${equipe}`;
        }
    } else if (button.classList.contains("oddsAmbasMarcamSim")) {
        opcaoAposta.innerText = `que AMBAS as equipes marcam`;
    } else if (button.classList.contains("oddsAmbasMarcamNao")) {
        opcaoAposta.innerText = `que NO MÁXIMO uma equipe marca`;
    } else if (button.classList.contains("oddsMaisGols")) {
        opcaoAposta.innerText = `que sairão MAIS de 3.5 gols na partida`;
    } else if (button.classList.contains("oddsMenosGols")) {
        opcaoAposta.innerText = `que sairão MENOS de 3.5 gols na partida`;
    }
}

document.getElementById("valorApostado").addEventListener("input", atualizarRetorno);

function atualizarRetorno() {
    let valor = parseFloat(document.getElementById("valorApostado").value) || 0;
    let retorno = (oddSelecionada * valor);
    document.getElementById("retornoEsperado").innerText = `₲ ${retorno}`;
}

function fecharApostaRapida() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("apostaRapida-container").style.display = "none";
}
