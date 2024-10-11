import PySimpleGUI as sg
susunan = [[sg.VPush()],
    [sg.Text("Uniska MAAB", font=("Helvetica", 24))],
    [sg.Text("BANJARMASIN", font=("Courier", 18))],
    [sg.VPush()]],
window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   element_justification= "center",
                   size=(430, 200))

window.read()
window.close()

# Dibuat Oleh :
# Nama : Siti Nurhaliza
# NPM : 2210010282
# Kelas : 5P Reguler Pagi Banjarmasin