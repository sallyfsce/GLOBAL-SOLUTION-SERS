# Sistema de Monitoramento de Missão Espacial

> **Global Solution | FIAP — Ciência da Computação | Soluções em Energias Renováveis e Sustentáveis**

---

## Sobre o Projeto

O **Mission Control** é um sistema de monitoramento desenvolvido em Python para controle operacional da missão espacial experimental **USG Ishimura**. A cada execução, o sistema simula e analisa em tempo real os dados dos módulos energéticos da nave — painéis solares fotovoltaicos, baterias e comunicação —, gerando alertas automáticos e ações automatizadas diante de situações críticas.

A solução aplica conceitos de **energia renovável solar**, **eficiência energética**, **sustentabilidade** e **automação** no contexto da exploração espacial contemporânea.

---

## Como Executar

Pré-requisito: Python 3.10 ou superior.

Cada execução gera dados diferentes — os valores dos são simulados aleatoriamente a cada vez.

---

## Módulos Monitorados

| Módulo | ID | O que mede |
|--------|----|-----------|
| Painel Solar 1 | PS-01 | Potência gerada (W), eficiência (%) e temperatura (°C) |
| Painel Solar 2 | PS-02 | Potência gerada (W), eficiência (%) e temperatura (°C) |
| Bateria 1 | BAT-01 | Carga (%), tensão (V) e temperatura (°C) |
| Bateria 2 | BAT-02 | Carga (%), tensão (V) e temperatura (°C) |
| Comunicação | COM-01 | Força do sinal (%), pacotes enviados e perdidos |

---

## Regras de Alerta

### Painéis Solares
| Condição | Nível |
|----------|-------|
| Temperatura > 80 °C | CRÍTICO |
| Temperatura entre 65 °C e 80 °C | AVISO |
| Potência < 50 W | CRÍTICO |
| Eficiência < 60% | AVISO |

### Baterias
| Condição | Nível |
|----------|-------|
| Carga < 15% | CRÍTICO |
| Carga entre 15% e 30% | AVISO |

### Comunicação
| Condição | Nível |
|----------|-------|
| Sinal ausente (desconectado) | CRÍTICO |
| Sinal < 40% | AVISO |
| Perda de pacotes > 10% | AVISO |

---

## Score de Saúde Geral

Ao final de cada execução o sistema calcula um score de 0 a 100 que resume a saúde geral da nave:

```
Score = (média de eficiência dos painéis × 35%)
      + (média de carga das baterias   × 40%)
      + (média de sinal de comunicação × 25%)
      - penalidades por alertas (CRÍTICO = -20 pts, AVISO = -5 pts)
```

| Score | Indicador |
|-------|-----------|
| ≥ 70 | Sistema saudável |
| 40 – 69 | Atenção necessária |
| < 40 | Estado crítico |

---

## Funções Implementadas

| Função | Descrição |
|--------|-----------|
| `gerar_painel()` | Simula os dados de um painel solar |
| `gerar_bateria()` | Simula os dados de uma bateria |
| `gerar_comunicacao()` | Simula os dados do módulo de comunicação |
| `checar_painel()` | Analisa e gera alertas do painel |
| `checar_bateria()` | Analisa e gera alertas da bateria |
| `checar_comunicacao()` | Analisa e gera alertas da comunicação |
| `gerar_todos_alertas()` | Consolida todos os alertas da execução |
| `calcular_saude()` | Calcula o score de saúde geral da nave |
| `barra()` | Gera barra de progresso textual `[###---]` |
| `exibir_cabecalho()` | Exibe cabeçalho com nome da missão e horário |
| `exibir_paineis()` | Exibe dados dos painéis solares |
| `exibir_baterias()` | Exibe dados das baterias |
| `exibir_comunicacao()` | Exibe dados do módulo de comunicação |
| `exibir_alertas()` | Exibe alertas e ações automatizadas |
| `exibir_saude()` | Exibe score e status de sustentabilidade |
| `executar()` | Função principal — orquestra toda a execução |

---

## Conceitos de Energia Aplicados

| Conceito | Onde é aplicado |
|----------|----------------|
| Energia solar fotovoltaica | Painéis PS-01 e PS-02 com cálculo de potência e eficiência |
| Eficiência energética | Score de saúde pondera eficiência dos painéis (peso 35%) |
| Gestão de baterias | Monitoramento de carga, tensão e temperatura |
| Sustentabilidade | Indicador de autossuficiência energética (> 200 W gerados) |
| Redundância | Ativação automática de painel/antena de backup em falhas |
| MPPT | Ajuste de orientação sugerido como resposta a baixa eficiência |

---

## Exemplo de Saída

```
==========================================================
  USG ISHIMURA -- EXP-01
  2026-06-07 05:12:26
==========================================================

PAINEIS SOLARES
----------------------------------------------------------
  PS-01
    Potencia  :   97.52 W
    Eficiencia: [###############-----]  76.2%
    Temp.     : +17.39 C  |  Status: NOMINAL

  PS-02
    Potencia  :   99.50 W
    Eficiencia: [##################--]  91.4%
    Temp.     : +8.66 C  |  Status: NOMINAL

BATERIAS
----------------------------------------------------------
  BAT-01
    Carga  : [#####---------------]  25.2%  |  Tensao: 23.51 V
    Temp.  : +31.55 C  |  Status: NOMINAL

  BAT-02
    Carga  : [#################---]  86.5%  |  Tensao: 27.19 V
    Temp.  : +20.27 C  |  Status: NOMINAL

COMUNICACAO
----------------------------------------------------------
  COM-01
    Sinal    : [#############-------]  69.0%  |  CONECTADO
    Pacotes  : 293 enviados, 15 perdidos (5.1%)
    Status   : NOMINAL

ALERTAS
----------------------------------------------------------
  (i) [AVISO] BAT-01
      Evento : Bateria baixa: 25.22%
      Acao   : Reducao de consumo: aquecedores em 50%.

SAUDE GERAL DA MISSAO
----------------------------------------------------------
  Score   : 63.9/100  [############--------]  63.9%
  Energia : 197.02 W gerados neste ciclo
  Status  : Abaixo do ideal
==========================================================
```

---

## Integrantes

| Nome | RM |
|------|----|
| Aneliza Rondina Bonafé - RM: 572977 |
| Rafaella Ferreira de Moraes - RM: 571030 |
---

## Vídeo

[▶ Assistir no YouTube](https://youtube.com/SEU_LINK_AQUI)
