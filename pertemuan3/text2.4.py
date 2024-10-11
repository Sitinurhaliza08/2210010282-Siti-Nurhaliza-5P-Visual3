import PySimpleGUI as sg
sg.theme("DarkGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24), text_color=("#FFFFFF"))],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",font=("Courier",18,"italic","bold","underline"))],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]],
                   size=(430,200),
                   font=("Times", 18))
window()
window.close()

# Dibuat Oleh :
# Nama : Siti Nurhaliza
# NPM : 2210010282
# Kelas : 5P Reguler Pagi Banjarmasin