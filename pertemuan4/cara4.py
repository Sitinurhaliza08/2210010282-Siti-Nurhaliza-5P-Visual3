# ============== Cara 4 (recommended, lebih hemat memori)  ========

from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()