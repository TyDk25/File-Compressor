import PySimpleGUI as gi
from zip_creator import make_archive

label1 = gi.Text("Select files to compress:")
input1 = gi.Input()
choose_button1 = gi.FilesBrowse("Choose", key ="files")

label2 = gi.Text("Select destination folder:")
input2 = gi.Input()
choose_button2 = gi.FolderBrowse("Choose", key="folder")

label3 = gi.Text(key="output")

compress_button = gi.Button("Compress")

window = gi.Window("File Compressor",
layout=[[label1, input1, choose_button1],
[label2,input2,choose_button2],
[compress_button, label3]])

while True:
    event, values =   window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed")


window.close()