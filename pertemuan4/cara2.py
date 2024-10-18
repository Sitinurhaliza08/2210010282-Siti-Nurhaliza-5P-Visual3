# QtGui QTCore QtWidgets
# ============== Cara 2 ==============================

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()