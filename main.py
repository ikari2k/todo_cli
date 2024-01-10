user_prompt = "Type add or show or edit or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print('Unknown command!')

print('Bye!')    
    

