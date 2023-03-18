import functions
import PySimpleGUI as SG

label = SG.Text("Enter a new task:")
input_box = SG.InputText(tooltip="Enter Task", key='to_do')
add_button = SG.Button("Add")
show_button = SG.Button("Show")
edit_button = SG.Button("Edit")
comp_button = SG.Button("Complete")
exit_button = SG.Button("Exit")
list_box = SG.Listbox(values=functions.get_To_Do(), key='items',
 enable_events=True, size=[45,10])

layout1 = [[label],
  [input_box, add_button],
  [list_box, edit_button],
  [show_button],
  [comp_button],
  [exit_button],]

window = SG.Window("My To-Do App", layout= layout1, font=('Calibri', 16))

while True:
    event, values = window.read()

    match event:
        case "Add":
            To_Do = functions.get_To_Do()
            new = values['to_do'] + '\n'
            To_Do.append(new)
            functions.store_To_Do(To_Do)
            window['items'].update(values=To_Do)
            # window['to_do']

        case "Edit":
            item = values['items'][0]
            replace = values['to_do']
            To_Do = functions.get_To_Do()
            index = To_Do.index(item)
            To_Do[index] = replace + '\n'
            functions.store_To_Do(To_Do)
            window['items'].update(values=To_Do)

        case "Complete":
            item = values['items'][0]
            To_Do = functions.get_To_Do()
            index = To_Do.index(item)
            To_Do.pop(index)
            functions.store_To_Do(To_Do)
            window['items'].update(values=To_Do)

        case "Exit":
            break
        
        case SG.WIN_CLOSED:
            break


window.close()
