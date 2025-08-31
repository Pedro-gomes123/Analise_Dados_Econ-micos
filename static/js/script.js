// Arquivo: static/js/script.js

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. SELEÇÃO DOS NOVOS ELEMENTOS ---
    const cards = document.querySelectorAll('.card');
    const numDiasInput = document.getElementById('numDiasInput');
    const presetButtons = document.querySelectorAll('.preset-buttons button');
    const chartMessage = document.getElementById('chart-message');
    const ctx = document.getElementById('meuGrafico').getContext('2d');
    
    let graficoAtivo = null;
    let ativoSelecionado = null; // Guarda qual ativo está selecionado no momento

    // --- 2. FUNÇÃO PARA DESENHAR O GRÁFICO (continua a mesma) ---
    function desenharGrafico(dados, nomeAtivo) {
        if (graficoAtivo) {
            graficoAtivo.destroy();
        }

        // Mostra o canvas e esconde a mensagem
        ctx.canvas.style.display = 'block';
        chartMessage.classList.add('hidden');

        const labels = dados.map(item => new Date(item.data).toLocaleDateString('pt-BR', { timeZone: 'UTC' }));
        const valores = dados.map(item => item[nomeAtivo]);

        graficoAtivo = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: `Valor do ${nomeAtivo.toUpperCase()}`,
                    data: valores,
                    borderColor: '#4db6ac',
                    backgroundColor: 'rgba(77, 182, 172, 0.2)',
                    fill: true,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { 
                    y: { 
                        beginAtZero: false,
                        ticks: { color: '#e0e0e0' },
                        grid: { color: '#333' }
                    },
                    x: {
                        ticks: { color: '#e0e0e0' },
                        grid: { color: '#333' }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: '#e0e0e0'
                        }
                    }
                }
            }
        });
    }

    // --- 3. FUNÇÃO PARA BUSCAR OS DADOS (continua quase a mesma) ---
    async function buscarEDesenhar() {
        // Só continua se um ativo foi selecionado E o input tem um valor válido
        if (!ativoSelecionado || !numDiasInput.value) {
            return;
        }

        const numDias = parseInt(numDiasInput.value, 10);
        if (isNaN(numDias) || numDias <= 0) {
            alert("Por favor, insira um número de dias válido.");
            return;
        }
        
        console.log(`Buscando dados para ${ativoSelecionado} nos últimos ${numDias} dias...`);
        chartMessage.textContent = `Buscando dados para ${ativoSelecionado.toUpperCase()}...`;
        chartMessage.classList.remove('hidden');
        ctx.canvas.style.display = 'none';

        try {
            const response = await fetch(`/api/dados/${ativoSelecionado}/${numDias}`);
            if (!response.ok) { throw new Error('A resposta da API não foi OK'); }
            const dados = await response.json();

            if (dados && dados.length > 0) {
                desenharGrafico(dados, ativoSelecionado);
            } else {
                chartMessage.textContent = `Nenhum dado encontrado para ${ativoSelecionado.toUpperCase()} no período selecionado.`;
                if (graficoAtivo) { graficoAtivo.destroy(); }
            }
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
            chartMessage.textContent = "Ocorreu um erro ao buscar os dados. Tente novamente.";
        }
    }

    // --- 4. NOVA LÓGICA DE INTERATIVIDADE ---

    // O que acontece quando um CARD é clicado
    cards.forEach(card => {
        card.addEventListener('click', () => {
            // Remove a seleção de todos os outros cards
            cards.forEach(c => c.classList.remove('selected'));
            // Adiciona a seleção apenas no card clicado
            card.classList.add('selected');
            // Guarda o nome do ativo que foi selecionado
            ativoSelecionado = card.dataset.ativo;
            // Dispara a busca de dados imediatamente
            buscarEDesenhar();
        });
    });

    // O que acontece quando um BOTÃO DE PERÍODO é clicado
    presetButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Pega o número de dias do botão (ex: 30)
            const dias = button.dataset.days;
            // Coloca esse número no campo de input
            numDiasInput.value = dias;
            // Dispara a busca de dados
            buscarEDesenhar();
        });
    });

    // O que acontece quando o usuário APERTA ENTER no campo de input
    numDiasInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            // Dispara a busca de dados
            buscarEDesenhar();
        }
    });

});