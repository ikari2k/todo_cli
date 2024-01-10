<<<<<<< HEAD
user_prompt = "Type add or show or exit: "
=======
user_prompt = "Type add or show: "
>>>>>>> 318403aa32d87d331a3a363ff7673e26406731f1
todos = []

while True:
    user_action = input(user_prompt)
<<<<<<< HEAD
    user_action = user_action.strip()
=======
>>>>>>> 318403aa32d87d331a3a363ff7673e26406731f1
    match user_action:
        case 'add':
            todo = input('Enter todo: ')
            todos.append(todo)
        case 'show':
<<<<<<< HEAD
            for item in todos:
                print(item)
        case 'exit':
            break

print('Bye!')    
=======
            print(todos)    
>>>>>>> 318403aa32d87d331a3a363ff7673e26406731f1
    

