from dados import eventos
from dados import participantes 

def importar_eventos():
    return eventos.eventos

def importar_participantes():
    return participantes.participantes

if __name__ == "__main__":
    eventos_importados = importar_eventos()
    participantes_importados = importar_participantes()
    print(f"{len(eventos_importados)} eventos importados")
    print(f"{len(participantes_importados)} participantes importados")