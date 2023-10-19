
#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print ("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todo = todo + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1

            new_todo = input("Enter the new to do item: ")

            todos = functions.get_todos()

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("The Command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            todos_to_remove = todos[number].strip('\n')

            todos.pop(number)

            functions.write_todos(todos)
            message = f"Todo {todos_to_remove} was removed from the list"

            print(message)
        except IndexError:
            print("There is no such item with this number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")
