birthdays = {'adam':'12 feb','ronak':'14 nov'}

while True:
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print (birthdays[name] + ' is the birthday of ' + name)
    else:
        print ('I do not have birthday information for ' + name)
        print ( 'What is their birthday?')
        bday= input ()
        birthdays [name] = bday
        print ('Birthday database updated.')
        
