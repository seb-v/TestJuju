

def suisJeTobol(nom):
    if nom.lower() == "julien":
        return "oui"
    else:
        return "non"

def checkTobolitude(nom):
    print(nom + " est-il tobol ? " + suisJeTobol(nom))
print("Salut les tobols")

checkTobolitude("Julien")
checkTobolitude("Nelson")



