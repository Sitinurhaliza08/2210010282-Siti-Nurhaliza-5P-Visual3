import PySimpleGUI as sg

susunan = [
    [sg.VPush(),
    sg.Text("Uniska MAAB", font=("Helvetica", 24)),
    sg.Push()],
    [sg.Push(),
    sg.Text("BANJARMASIN", font=("Courier", 18)),
    sg.Push()],
    [sg.VPush()]
]

window = sg.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

window.read()
window.close()

# Dibuat Oleh :
# Nama : Siti Nurhaliza
# NPM : 2210010282
# Kelas : 5P Reguler Pagi Banjarmasin