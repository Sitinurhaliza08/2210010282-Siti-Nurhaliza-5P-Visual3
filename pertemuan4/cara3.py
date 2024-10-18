# QtGui QTCore QtWidgets
# ============== Cara 3 ==============================

from PyQt5 import QtWidgets as qtw

app = qtw.QApplication([])
window = qtw.QPushButton("MyButton")
window.show()
app.exec_()