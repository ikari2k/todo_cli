import functions
import PySimpleGUI as sg
import time

sg.theme('Black')

label_time = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors='LightBlue2',
                       tooltip='Add todo', key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button(image_source='complete.png', mouseover_colors='LightBlue2',
                            tooltip='Complete todo', key='Complete')
exit_button = sg.Button('Exit')
update_label = sg.Text('', key='output',text_color='green')
error_label = sg.Text('', key='error',text_color='red')

window = sg.Window('My To-Do App', 
                   layout=[[label_time],
                           [label], 
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, update_label,error_label]], 
                   font=('Helvetica',16)) 

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    
    match event:
        case "Add":
            if(len(values['todo'])>0):
                todos = functions.get_todos()
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                window['error'].update(value='')
                window['output'].update(value='New todo added: ' + new_todo.strip())
            else:
                window['output'].update(value='')
                window['error'].update(value='You wanted to empty todo')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                window['error'].update(value='')
                window['output'].update(value='Todo: '+todo_to_edit.strip()+' was edited to ' + new_todo.strip())

            except IndexError:
                #sg.popup('Please select a todo first.',font=('Helvetica',16))
                window['output'].update(value='')
                window['error'].update(value='Please select a todo first.')
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                window['error'].update(value='')
                window['output'].update(value='Complete: ' + todo_to_complete.strip())
            except IndexError:
                #sg.popup('Please select a todo first.',font=('Helvetica',16))
                window['output'].update(value='')
                window['error'].update(value='Please select a todo first.')
        case "todos": #when user is selecting item from the list
            window['todo'].update(value = values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
