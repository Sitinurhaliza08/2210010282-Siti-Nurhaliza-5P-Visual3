import PySimpleGUI as sg
sg.theme("DarkGreen4"),
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010282")],
                           [sg.Text("Nama   : Siti Nurhaliza")],
                           [sg.Text("Kelas  : 5P Reguler Banjarmasin")],
                           [sg.Text("Matkul : Pemprograman Visual 3")],
                           ],
                   size=(400,200))
window()
window.close()

# Dibuat Oleh :
# Nama : Siti Nurhaliza
# NPM : 2210010282
# Kelas : 5P Reguler Pagi Banjarmasin