import PySimpleGUI as sg
sg.theme("darkgreen4"),
sg.theme_text_color("#E3cf57"),
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DIKELAS", font=("Arial", 25))],
                           [sg.Text("NPM    : 2210010282")],
                           [sg.Text("Nama   : Siti Nurhaliza")],
                           [sg.Text("Kelas  : 5P Reguler Banjarmasin")],
                           [sg.Text("Matkul : Pemprograman Visual 3")],
                           ],
                   size=(400,200), 
                   font=("Times", 12))
window()
window.close()

# Dibuat Oleh :
# Nama : Siti Nurhaliza
# NPM : 2210010282
# Kelas : 5P Reguler Pagi Banjarmasin