"""
NUMEROS DE DEVOLCUOIN
"""
def perfumes():
    """

    :return:
    """
    turno = 1
    while True:
        yield turno
        turno += 1


def farmacia():
    """

    :return:
    """
    turno = 1
    while True:
        yield turno
        turno += 1


def cosmeticos():
    """

    :return:
    """
    turno = 1
    while True:
        yield turno
        turno += 1


turnocosmeticos = cosmeticos()
turnoPerfumes = perfumes()
turnofarmacia = farmacia()


