
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

# verification de données :
def verif():
    if w.l1.text() == "":
        QMessageBox.information(w, "Erreur", "Vérifier la saisie")
    ch = w.l1.text()
    comb = w.c1.currentText()
    comb2 = w.c2.currentText()
    for i in range(0, len(ch)):
        if ch[i] >= comb:
            QMessageBox.information(w, "Erreur", "Vérifier la saisie")
    if comb == comb2:
        QMessageBox.information(w, "Erreur", "Changer l'une des bases ! Les bases sont les mêmes")        
        
# convertion de n importe quelle base en decimal

def conv_b_10(ch, b):
    s = 0
    p = 1
    for i in range(len(ch)-1, -1, -1):
        if "0" <= ch[i] <= "9":
            s = s + int(ch[i]) * p
        else:
            s = s + (ord(ch[i].upper()) - 55) * p
        p = p * b
    return s

# convertion de decimal en n importe quelle base

def conv_10_b(n, b):
    ch = ""
    while n > 0:
        r = n % b
        if r < 10:
            ch = str(r) + ch
        else:
            ch = chr(r + 55) + ch
        n = n // b
    return ch

# fonction d'emulation des modules

def play(test):
    w.list.clear()
    ch = w.l1.text()
    b = int(w.c1.currentText())
    k = conv_b_10(ch, b)
    j = conv_10_b(k, int(w.c2.currentText()))
    l1=str(ch)+" en base "+str(w.c2.currentText())+" = "+str(w.l1.text())
    if int(w.l1.text())==0:
        w.list.addItem(l1)
    else :
        l=str(ch)+" en base "+str(w.c2.currentText())+" = "+str(j)
        w.list.addItem(l)


# fermeture de programme

def fermer():
    w.close()
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.conv.clicked.connect(play)
w.f.clicked.connect(fermer)
w.v.clicked.connect(verif)
app.exec_()