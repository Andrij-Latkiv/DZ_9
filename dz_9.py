CONTACTS = {}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except TypeError:
            return "Give me name and phone please"
        except ValueError:
            return "Give me name and phone please"   
        except IndexError:
            return "Enter user name"
    return inner


def hello_user():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    CONTACTS[name] = phone
    return f'User {name} added contact {phone}'

@input_error
def change_phone(name, phone):
    CONTACTS[name] = phone
    return f'{name} have a new phone: {phone}'

@input_error
def show_phone(name):
    return f'User {name} showing phone {CONTACTS[name]}'


def show():
    
    result = ''
    for name, phone in CONTACTS.items():
        result += f'\n name: {name}  phone: {phone}'
    
    return result


def unknown_command(command):
    return f'Not command {command}'



exit_command = ['good_bye', 'close', 'exit']


commands = {
    'hello': hello_user,
    'add': add_contact,
    'change': change_phone,
    'phone': show_phone,
    'show_all': show,
    
    }



def main():

    while True:

        command, *data = input('Please enter [name] , [phone] :  ').strip().split(' ', 1)

        
        if command in exit_command:
            print('Good bye!')
            break

        elif commands.get(command):
            handler = commands.get(command)
            if data:
                data = data[0].split(',')

            result = handler(*data)
        

        else:
            result = unknown_command(command)


        print(result)




if __name__ == '__main__':
    main()
