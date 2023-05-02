USERS = {}


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner


def hello_user(_):
    return "How can I help you?"


def exit(_):
    print('Good bye!')
    return

def unknown_command(_):
    return "unknown command"

@input_error
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f"User {name} added!"

@input_error
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"У {name} тепер телефон: {phone} Старий номер: {old_phone}"
    

def show_all(_):
    result = ''
    for name, phone in USERS.items():
        result += f'name: {name} phone: {phone}\n'
    return result


def show_phone(args):
    name = args
    
    phone_to_show = str(USERS[name[0]])
    
    return f'name: {(name[0]).title()} phone: {phone_to_show}'

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'show all': show_all,
    'exit': exit,
    'good bye': exit,
    'close': exit,
    'phone': show_phone,

}


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lstrip()

    try:
        handler  = HANDLERS[command.lower()]
    except KeyError:
        if args:
            command  = command + " " + args[0]
            args = args[1:]
        handler = HANDLERS.get(command.lower(), unknown_command)
    return handler, args



def main():
    while True:
        user_input = input('Please enter command and args: ')
        handler, *args = parse_input(user_input)
        result = handler(*args)
        if not result:
           
            break

        print(result)


if __name__ == '__main__':
    main()



