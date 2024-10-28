import random

def gerar_historia():
    perso = ["um fazendeiro", "um cantor", "um maluco", "um magico", "um astronauta", "uma detetive", "um dragão", "um cientista", "um robô"]
    acoes = ["encontrou um mistério", "descobriu um portal secreto", "salvou o dia", "fez uma invenção maluca", "perdeu algo importante"]
    locais = ["na Lua", "em uma ilha deserta", "no fundo do oceano", "em uma cidade futurista", "no meio da floresta"]

    perso = random.choice(perso)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"Era uma vez {perso} que {acao} {local}."
    return historia

print(gerar_historia())
