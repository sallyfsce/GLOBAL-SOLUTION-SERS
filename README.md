# 🛸 SOLAR SENTINEL — Sistema de Monitoramento de Missão Espacial

> **Global Solution | FIAP — Ciência da Computação | Soluções em Energias Renováveis e Sustentáveis**

---

## 📌 Sobre o Projeto

O **SOLAR SENTINEL** é um sistema de monitoramento inteligente desenvolvido em Python para controle operacional de uma missão espacial experimental. O sistema simula e analisa em tempo real dados dos módulos energéticos da nave — painéis solares fotovoltaicos, baterias de íon-lítio e comunicação —, gerando alertas automáticos e tomando decisões básicas diante de situações críticas.

A solução aplica diretamente conceitos de **energia renovável solar**, **eficiência energética**, **sustentabilidade** e **automação inteligente** no contexto da exploração espacial moderna.

---

## 🎯 Objetivos Atendidos

| Requisito | Implementação |
|-----------|--------------|
| Monitoramento de dados simulados | `SimuladorMissao` gera dados realistas de temperatura, potência, carga de bateria e qualidade de sinal |
| Geração de alertas | `MotorAlertas` classifica eventos em INFO / AVISO / CRÍTICO com mensagens específicas |
| Tomada de decisão básica | Ações automatizadas (ex: ativar painel redundante, modo emergência, ajuste de antena) |
| Visualização dos dados | Dashboard colorido no terminal com barras de progresso e indicadores de status |

---

## 🏗️ Arquitetura do Sistema

```
space_monitor/
├── monitor.py        # Sistema principal (simulador + motor de alertas + dashboard)
├── tests.py          # Testes unitários (12 casos de teste)
├── logs/
│   └── missao.log    # Histórico de eventos (gerado em execução)
└── reports/
    └── ultimo_relatorio.json  # Relatório JSON do último ciclo
```

### Módulos principais

```
SimuladorMissao          →  gera dados simulados realistas por ciclo
    └── gerar_painel()   →  PainelSolar (potência, eficiência, temperatura, orientação)
    └── gerar_bateria()  →  Bateria (carga, tensão, temperatura, ciclos)
    └── gerar_comunicacao() → ModuloComunicacao (sinal, frequência, pacotes)

MotorAlertas             →  analisa dados e dispara alertas
    └── analisar()       →  retorna lista de Alerta com ação automatizada

calcular_saude_geral()   →  score 0–100 ponderado (IA introdutória)
avaliar_status()         →  NOMINAL / ALERTA / CRÍTICO / OFFLINE por módulo
```

---

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.10 ou superior
- Sem dependências externas (apenas biblioteca padrão)

### Instalação

```bash
git clone https://github.com/SEU_USUARIO/solar-sentinel.git
cd solar-sentinel
```

### Execução básica (5 ciclos, intervalo de 2 segundos)

```bash
python monitor.py
```

### Execução personalizada

```bash
# 10 ciclos com intervalo de 3 segundos entre cada um
python monitor.py --ciclos 10 --intervalo 3.0

# Ciclo único (ideal para demonstração rápida)
python monitor.py --ciclos 1 --intervalo 0
```

### Testes unitários

```bash
python tests.py
```

---

## 📊 Exemplo de Saída

```
════════════════════════════════════════════════════════════════
  🛸  SOLAR SENTINEL — EXP-01
  Ciclo #0001  |  2025-06-04 14:23:11
════════════════════════════════════════════════════════════════

☀  PAINÉIS SOLARES
──────────────────────────────────────────────────────────────
  PS-01
    Potência  :  127.45 W  |  Eficiência : ████████████░░░░░░░░  83.2%
    Temp.     :  +38.21 °C  |  Orientação : 92.4°
    Status    : NOMINAL

🔋  BATERIAS
  BAT-01
    Carga     : ██████████░░░░░░░░░░  51.3%  |  Tensão: 25.08 V
    Status    : NOMINAL

⚠  ALERTAS E AÇÕES AUTOMATIZADAS
  ℹ [INFO] TODOS
    Evento : Todos os sistemas operam normalmente.
    Ação   : Nenhuma ação necessária.

📊  SAÚDE GERAL DA MISSÃO
  Score de Saúde : 74.2/100  ████████████████░░░░  74.2%
  Energia Total  : 245.18 W gerados neste ciclo
  Sustentabilidade: ✅ Autossuficiente
```

---

## 🔋 Conceitos de Energia Aplicados

| Conceito | Onde é aplicado |
|----------|----------------|
| **Energia solar fotovoltaica** | Painéis PS-01 e PS-02 com cálculo de potência e eficiência |
| **Eficiência energética** | Score de saúde pondera eficiência dos painéis (peso 35%) |
| **Gestão de baterias** | Monitoramento de SoC (State of Charge), tensão e ciclos de vida |
| **Sustentabilidade** | Indicador de autossuficiência energética (>200 W gerados) |
| **Redundância** | Ativação automática de painel/antena de backup em falhas |
| **MPPT** | Ajuste de orientação mencionado como resposta a baixa eficiência |

---

## 🤖 Inteligência Artificial Introdutória

O sistema aplica lógica de IA básica através de:

1. **Sistema especialista baseado em regras** — limiares configuráveis em `LIMIARES` para classificação de eventos
2. **Função de pontuação ponderada** — `calcular_saude_geral()` combina múltiplas métricas com pesos diferentes
3. **Tomada de decisão automatizada** — respostas predefinidas para cada categoria de evento crítico
4. **Histórico acumulativo** — `MotorAlertas.historico` armazena todos os eventos para análise posterior

---

## 🧪 Cobertura de Testes

```
Ran 12 tests in 0.003s — OK ✅

✔ test_painel_nominal_sem_alerta_critico
✔ test_painel_superaquecimento_gera_alerta_critico
✔ test_painel_potencia_baixa_gera_alerta_critico
✔ test_painel_eficiencia_baixa_gera_aviso
✔ test_bateria_critica_gera_alerta
✔ test_bateria_baixa_gera_aviso
✔ test_comunicacao_desconectada_gera_critico
✔ test_comunicacao_sinal_fraco_gera_aviso
✔ test_sistema_saudavel_score_alto
✔ test_sistema_critico_score_baixo
✔ test_simulador_gera_dados_validos
✔ test_historico_alertas_acumulado
```

---

## 👥 Integrantes do Grupo

| Nome | RM |
|------|----|
| Nome Completo 1 | RM000000 |
| Nome Completo 2 | RM000000 |
| Nome Completo 3 | RM000000 |

---

## 🎥 Vídeo de Demonstração

[▶ Assistir no YouTube](https://youtube.com/SEU_LINK_AQUI)

---

## 📄 Licença

Projeto acadêmico desenvolvido para a Global Solution FIAP 2025.
