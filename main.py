user_prompt = "Type add or show: "
todos = []

while True:
    user_action = input(user_prompt)
    match user_action:
        case 'add':
            todo = input('Enter todo: ')
            todos.append(todo)
        case 'show':
            print(todos)    
    

