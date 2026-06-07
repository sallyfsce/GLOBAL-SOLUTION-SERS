"""
USG ISHIMURA — Sistema de Monitoramento Espacial
Global Solution | FIAP — Ciência da Computação
Soluções em Energias Renováveis e Sustentáveis
"""

import random
import datetime


#  Limiares de alerta

TEMP_CRITICA    = 80.0  # °C
TEMP_ALERTA     = 65.0  # °C
BATERIA_CRITICA = 15.0  # %
BATERIA_ALERTA  = 30.0  # %
POTENCIA_MINIMA = 50.0  # W
SINAL_MINIMO    = 40.0  # %



#  Geração de dados simulados

def gerar_painel(nome: str, evento_critico: bool = False) -> dict:
    potencia    = random.uniform(80, 150)
    eficiencia  = random.uniform(55, 92)
    temperatura = random.uniform(-10, 75)

    if evento_critico and nome == "PS-01":
        potencia   = random.uniform(10, 40)
        eficiencia = random.uniform(20, 45)

    return {
        "nome":        nome,
        "potencia":    round(potencia, 2),
        "eficiencia":  round(eficiencia, 2),
        "temperatura": round(temperatura, 2),
    }


def gerar_bateria(nome: str, evento_critico: bool = False) -> dict:
    carga = random.uniform(10, 95)

    if evento_critico and nome == "BAT-01":
        carga = random.uniform(5, 18)

    tensao = round(22.0 + (carga / 100) * 6.0, 2)

    return {
        "nome":        nome,
        "carga":       round(carga, 2),
        "tensao":      tensao,
        "temperatura": round(random.uniform(-15, 55), 2),
    }


def gerar_comunicacao(nome: str, evento_critico: bool = False) -> dict:
    sinal    = random.uniform(30, 98)
    enviados = random.randint(100, 500)
    perdidos = int(enviados * random.uniform(0, 0.15))

    if evento_critico:
        sinal = random.uniform(10, 35)

    return {
        "nome":      nome,
        "sinal":     round(sinal, 2),
        "enviados":  enviados,
        "perdidos":  perdidos,
        "conectado": sinal > 20,
    }



#  Geração de alertas

def checar_painel(painel: dict) -> list:
    alertas = []
    n = painel["nome"]

    if painel["temperatura"] > TEMP_CRITICA:
        alertas.append({
            "nivel":   "CRITICO",
            "modulo":  n,
            "mensagem": f"Superaquecimento: {painel['temperatura']} C",
            "acao":    "Painel inclinado 90 graus para reduzir absorção solar.",
        })
    elif painel["temperatura"] > TEMP_ALERTA:
        alertas.append({
            "nivel":   "AVISO",
            "modulo":  n,
            "mensagem": f"Temperatura elevada: {painel['temperatura']} C",
            "acao":    "Monitoramento intensificado.",
        })

    if painel["potencia"] < POTENCIA_MINIMA:
        alertas.append({
            "nivel":   "CRÍTICO",
            "modulo":  n,
            "mensagem": f"Potencia baixa: {painel['potencia']} W",
            "acao":    "Painel redundante PS-03 ativado automaticamente.",
        })

    if painel["eficiencia"] < 60:
        alertas.append({
            "nivel":   "AVISO",
            "modulo":  n,
            "mensagem": f"Eficiência baixa: {painel['eficiencia']}%",
            "acao":    "Ajuste de orientação iniciado (MPPT).",
        })

    return alertas


def checar_bateria(bateria: dict) -> list:
    alertas = []
    n = bateria["nome"]

    if bateria["carga"] < BATERIA_CRITICA:
        alertas.append({
            "nivel":   "CRÍTICO",
            "modulo":  n,
            "mensagem": f"Carga critica: {bateria['carga']}%",
            "acao":    "Modo emergência: sistemas não-essenciais OFFLINE.",
        })
    elif bateria["carga"] < BATERIA_ALERTA:
        alertas.append({
            "nivel":   "AVISO",
            "modulo":  n,
            "mensagem": f"Bateria baixa: {bateria['carga']}%",
            "acao":    "Redução de consumo: aquecedores em 50%.",
        })

    return alertas


def checar_comunicacao(com: dict) -> list:
    alertas = []
    n = com["nome"]

    if not com["conectado"]:
        alertas.append({
            "nivel":   "CRÍTICO",
            "modulo":  n,
            "mensagem": "Perda total de sinal.",
            "acao":    "Antena secundária ativada. Protocolo de emergência iniciado.",
        })
    elif com["sinal"] < SINAL_MINIMO:
        alertas.append({
            "nivel":   "AVISO",
            "modulo":  n,
            "mensagem": f"Sinal fraco: {com['sinal']}%",
            "acao":    "Reorientação de antena em progresso.",
        })

    taxa_perda = (com["perdidos"] / max(com["enviados"], 1)) * 100
    if taxa_perda > 10:
        alertas.append({
            "nivel":   "AVISO",
            "modulo":  n,
            "mensagem": f"Perda de pacotes: {taxa_perda:.1f}%",
            "acao":    "Compressão de dados ativada.",
        })

    return alertas


def gerar_todos_alertas(paineis: list, baterias: list, comunicacao: list) -> list:
    alertas = []

    for p in paineis:
        alertas += checar_painel(p)

    for b in baterias:
        alertas += checar_bateria(b)

    for c in comunicacao:
        alertas += checar_comunicacao(c)

    if not alertas:
        alertas.append({
            "nivel":   "OK",
            "modulo":  "TODOS",
            "mensagem": "Todos os sistemas operam normalmente.",
            "acao":    "Nenhuma ação necessaria.",
        })

    return alertas



#  Score de saude geral

def calcular_saude(paineis: list, baterias: list, comunicacao: list, alertas: list) -> float:
    media_eficiencia = sum(p["eficiencia"] for p in paineis)    / len(paineis)
    media_bateria    = sum(b["carga"]      for b in baterias)   / len(baterias)
    media_sinal      = sum(c["sinal"]      for c in comunicacao) / len(comunicacao)

    penalidade = float(sum(
        20 if a["nivel"] == "CRITICO" else 5
        for a in alertas
        if a["nivel"] not in ("OK", "INFO")
    ))

    score = media_eficiencia * 0.35 + media_bateria * 0.40 + media_sinal * 0.25
    return max(0.0, min(100.0, score - penalidade))



#  Exibicao no terminal

def barra(valor: float, largura: int = 20) -> str:
    preenchido = int((valor / 100) * largura)
    blocos = "[" + "#" * preenchido + "-" * (largura - preenchido) + "]"
    return f"{blocos} {valor:5.1f}%"


def exibir_cabecalho():
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 58)
    print("  USG ISHIMURA -- EXP-01")
    print(f"  {agora}")
    print("=" * 58)


def exibir_paineis(paineis: list, alertas: list):
    print("\nPAINEIS SOLARES")
    print("-" * 58)
    for p in paineis:
        tem_critico = any(a["modulo"] == p["nome"] and a["nivel"] == "CRITICO" for a in alertas)
        status = "CRITICO" if tem_critico else "NOMINAL"
        print(f"  {p['nome']}")
        print(f"    Potência  : {p['potencia']:7.2f} W")
        print(f"    Eficiência: {barra(p['eficiencia'])}")
        print(f"    Temp.     : {p['temperatura']:+.2f} C  |  Status: {status}")
        print()


def exibir_baterias(baterias: list, alertas: list):
    print("BATERIAS")
    print("-" * 58)
    for b in baterias:
        tem_critico = any(a["modulo"] == b["nome"] and a["nivel"] == "CRITICO" for a in alertas)
        status = "CRITICO" if tem_critico else "NOMINAL"
        print(f"  {b['nome']}")
        print(f"    Carga  : {barra(b['carga'])}  |  Tensao: {b['tensao']} V")
        print(f"    Temp.  : {b['temperatura']:+.2f} C  |  Status: {status}")
        print()


def exibir_comunicacao(comunicacao: list, alertas: list):
    print("COMUNICACAO")
    print("-" * 58)
    for c in comunicacao:
        tem_critico = any(a["modulo"] == c["nome"] and a["nivel"] == "CRITICO" for a in alertas)
        status    = "CRÍTICO"     if tem_critico  else "NOMINAL"
        conectado = "CONECTADO"   if c["conectado"] else "OFFLINE"
        taxa = (c["perdidos"] / max(c["enviados"], 1)) * 100
        print(f"  {c['nome']}")
        print(f"    Sinal    : {barra(c['sinal'])}  |  {conectado}")
        print(f"    Pacotes  : {c['enviados']} enviados, {c['perdidos']} perdidos ({taxa:.1f}%)")
        print(f"    Status   : {status}")
        print()


def exibir_alertas(alertas: list):
    print("ALERTAS")
    print("-" * 58)
    for a in alertas:
        icone = "(!)" if a["nivel"] == "CRITICO" else "(i)"
        print(f"  {icone} [{a['nivel']}] {a['modulo']}")
        print(f"      Evento : {a['mensagem']}")
        print(f"      Acao   : {a['acao']}")
        print()


def exibir_saude(score: float, energia_total: float):
    suficiente = "Autossuficiente" if energia_total > 200 else "Abaixo do ideal"
    print("SAUDE GERAL DA MISSÃO")
    print("-" * 58)
    print(f"  Score   : {score:.1f}/100  {barra(score)}")
    print(f"  Energia : {energia_total:.2f} W gerados neste ciclo")
    print(f"  Status  : {suficiente}")
    print("=" * 58)


# Execução

def executar():
    evento_critico = random.random() < 0.10

    paineis     = [gerar_painel("PS-01", evento_critico), gerar_painel("PS-02")]
    baterias    = [gerar_bateria("BAT-01", evento_critico), gerar_bateria("BAT-02")]
    comunicacao = [gerar_comunicacao("COM-01", evento_critico)]

    alertas       = gerar_todos_alertas(paineis, baterias, comunicacao)
    energia_total = sum(p["potencia"] for p in paineis)
    saude         = calcular_saude(paineis, baterias, comunicacao, alertas)

    exibir_cabecalho()
    exibir_paineis(paineis, alertas)
    exibir_baterias(baterias, alertas)
    exibir_comunicacao(comunicacao, alertas)
    exibir_alertas(alertas)
    exibir_saude(saude, energia_total)


if __name__ == "__main__":
    executar()