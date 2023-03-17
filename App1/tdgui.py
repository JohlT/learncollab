import functions
import PySimpleGUI as SG

label = SG.Text("Enter a new task:")
input_box = SG.InputText(tooltip="Enter Task")
add_button = SG.Button("Add")
show_button = SG.Button("Show")
edit_button = SG.Button("Edit")
comp_button = SG.Button("Complete")
exit_button = SG.Button("Exit")

window = SG.Window("My To-Do App", layout=[[label, input_box], [add_button],[show_button],[edit_button],[comp_button],[exit_button]])
window.read()
window.close()