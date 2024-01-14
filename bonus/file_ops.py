'''
Initial files:
Name    Email   City
Mateusz mateusz@gmaiil.com Krakow
Paweł   pawel@gmail.com Tarnow

The output of the method:

list = [{'Name':'Mateusz, 'Email': 'mateusz@gmaiil.com', 'City': 'Krakow'},
        {'Name':'Paweł, 'Email': 'pawel@gmail.com', 'City': 'Tarnow'}]

'''
list = []
with open('bonus/my_list.txt', 'r') as file:
    
    #first line will put into a list as dictionary keys
    #['Name', 'Email', 'City']
    dictionary_keys = []
    dictionary_keys = file.readline().split()
    
    #let's create a list of the rest of the data
    data_list = file.readlines()
    
    #let's sanitize the list so that we get a list of list of data containing info from each row
    #[['Mateusz', 'mateusz@gmaiil.com', 'Krakow'], ['Paweł', 'pawel@gmail.com', 'Tarnow']]
    better_data_list = []
    for item in data_list:
        better_data_list.append(item.split())

    #let's combine two lists with zip method  that would create iterator of tuples and put it into a dictionary, for each element of better_data_list
    # append the result into final list
            
    for item in better_data_list:
        zipped = ()
        zipped = zip(dictionary_keys,item)
        list.append(dict(zipped))
print(list)
    