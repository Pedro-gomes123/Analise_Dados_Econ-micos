// Arquivo: static/js/script.js

// Espera o HTML carregar completamente antes de rodar o JavaScript
document.addEventListener('DOMContentLoaded', () => {

    // --- 1. SELEÇÃO DOS ELEMENTOS ---
    // Pega todos os elementos que têm a classe 'card'
    const cards = document.querySelectorAll('.card');
    // Pega o elemento <canvas> onde o gráfico será desenhado
    const ctx = document.getElementById('meuGrafico').getContext('2d');
    
    // Variável para guardar nosso gráfico, para que possamos destruí-lo antes de desenhar um novo
    let graficoAtivo = null;

    // --- 2. FUNÇÃO PARA DESENHAR O GRÁFICO ---
    // Esta função recebe os dados e o nome do ativo e usa a biblioteca Chart.js para desenhar
    function desenharGrafico(dados, nomeAtivo) {
        // Se já existe um gráfico na tela, destrua-o primeiro
        if (graficoAtivo) {
            graficoAtivo.destroy();
        }

        // Pega os dados para o eixo X (datas) e eixo Y (valores)
        const labels = dados.map(item => new Date(item.data).toLocaleDateString('pt-BR'));
        const valores = dados.map(item => item[nomeAtivo]);

        // Cria o novo gráfico
        graficoAtivo = new Chart(ctx, {
            type: 'line', // Tipo de gráfico (linha)
            data: {
                labels: labels,
                datasets: [{
                    label: `Valor do ${nomeAtivo.toUpperCase()}`,
                    data: valores,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    }

    // --- 3. FUNÇÃO PARA BUSCAR OS DADOS E CHAMAR O DESENHO ---
    // Esta função é "async" porque ela precisa esperar a resposta da nossa API Python
    async function buscarEDesenhar(nomeAtivo, numDias) {
        console.log(`Buscando dados para ${nomeAtivo} nos últimos ${numDias} dias...`);
        
        try {
            // "Liga" para a nossa API em Python
            const response = await fetch(`/api/dados/${nomeAtivo}/${numDias}`);
            if (!response.ok) {
                throw new Error('A resposta da API não foi OK');
            }
            const dados = await response.json(); // Pega os dados em formato JSON

            console.log("Dados recebidos:", dados);

            if (dados && dados.length > 0) {
                // Se recebemos dados, chama a função para desenhar o gráfico
                desenharGrafico(dados, nomeAtivo);
            } else {
                console.log("Nenhum dado retornado pela API.");
                // Opcional: Limpar o gráfico se não houver dados
                if (graficoAtivo) {
                    graficoAtivo.destroy();
                }
            }
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
        }
    }

    // --- 4. ADICIONANDO O "OUVINTE DE CLIQUE" NOS CARDS ---
    // Passa por cada card que encontramos no HTML
    cards.forEach(card => {
        // Adiciona um evento que dispara quando o card é clicado
        card.addEventListener('click', () => {
            const nomeAtivo = card.dataset.ativo; // Pega o nome do ativo (ex: 'selic') do atributo 'data-ativo'
            
            // Pergunta ao usuário o número de dias
            const diasStr = prompt("Por quantos dias para trás você deseja visualizar?", "30");
            
            // Se o usuário não cancelar e digitar algo, continua
            if (diasStr) {
                const numDias = parseInt(diasStr, 10);
                // Verifica se o que ele digitou é um número válido
                if (!isNaN(numDias) && numDias > 0) {
                    buscarEDesenhar(nomeAtivo, numDias);
                } else {
                    alert("Por favor, digite um número válido de dias.");
                }
            }
        });
    });

});