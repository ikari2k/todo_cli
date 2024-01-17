def strength(password):
    password_strenght = []
    if len(password) > 8:
        password_strenght.append(True)
    else: 
        password_strenght.append(False)
        
    password_strenght.append(any(character.isdigit() for character in password))
    password_strenght.append(any(character.isupper() for character in password))
    
    isStrongPassword = all(password_strenght)
    print(password_strenght)

    if isStrongPassword:
        return print("Strong Password")
    else:
        return print("Weak Password")
    

strength('QDuUY9KvkL6L7efaP1')
strength('QDuU')
strength('Dsdsdsdsdsds')
strength('dsdwdsddsdsd')