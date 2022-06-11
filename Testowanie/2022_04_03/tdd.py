def oceny(punkty):
    if punkty < 0 or punkty > 50:
        return "Punkty poza skalą."
    elif punkty <= 24:
        return "ndst"
    elif punkty <= 27:
        return "dop"
    elif punkty <= 37:
        return "dst"
    elif punkty <= 46:
        return "db"
    else:
        return "bdb"

    map()