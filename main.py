user_prompt = "Type add or show or edit or complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter todo: ') + "\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            index = number - 1 
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
            message = f"Todo \"{todo_to_remove}\" was removed fgrom the list."
            print(message)
        case 'exit':
            break
        case _:
            print('Unknown command!')

print('Bye!')
