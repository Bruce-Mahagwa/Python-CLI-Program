from functions import fetch_todos, write_todos
import time
prompt = "Type add or show or edit or done or exit: "
now = time.strftime("%d-%B-%Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input(prompt).strip()
    if "add" in user_action:
        todo = user_action.split(" ", 1)
        if todo[0] != "add":
            print("Please use the correct command")
            continue
        if len(todo) < 2:
            print("Please add a todo")
            continue
        else:
            todo = todo[1]
        todos = fetch_todos("todos.txt")
        if f"{todo}\n" in todos:
            print("Do not repeat items")
            continue
        todos.append(f"{todo}\n")
        write_todos("todos.txt", todos)
    elif "show" in user_action or "display" in user_action:
        todos = fetch_todos("todos.txt")
        if not len(todos):
            print("NO TODOS. ADD ONE")
            continue
        else:
            for index, i in enumerate(todos):
                output = f"{index}:)"
                i = i.replace("\n", "")
                print(output, i)
    elif "edit" in user_action or "ammend" in user_action:
        response = user_action.split(" ", 2)
        if len(response) < 3:
            print("Please add the new edited todo with the index to be edited")
            continue
        if response[0] != "edit" and response[0] != "ammend":
            print("Please use the correct command")
            continue
        else:
            try:
                index = int(response[1])
                response = response[2]
                if index >= 0:
                    try:
                        todos = fetch_todos("todos.txt")
                        todo = todos[index].strip("\n")
                        editPrompt = f"Edit {todo} to: {response}? Type Yes or No: "
                        confirmation = input(editPrompt)
                        if confirmation == "Yes":
                            todos[index] = f"{response}\n"
                            write_todos("todos.txt", todos)
                        else:
                            continue
                    except IndexError:
                        range_index = len(todos) - 1
                        if range_index < 0:
                            range_index = 0
                        print(f"The index is out of range. The range is from 0 to {range_index}")
                        continue
                else:
                    print("Please input an index from the range 0 to number of todos - 1")
            except ValueError:
                print("Please type a digit")
                continue
    elif "done" in user_action:
        response = user_action.split(" ", 1)
        if len(response) < 2:
            print("Please add the index to be deleted")
            continue
        if response[0] != "done":
            print("Please use the correct commands")
        try:
            index = int(response[1])
            if index >= 0:
                try:
                    todos = fetch_todos("todos.txt")
                    todo = todos[index].strip("\n")
                    removePrompt = f"Remove {todo}? Type Yes or No? "
                    deleteTodo = input(removePrompt)
                    if deleteTodo:
                        if deleteTodo == 'Yes':
                            todos.pop(index)
                            write_todos("todos.txt", todos)
                        else:
                            continue
                    else:
                        continue
                except IndexError:
                    print(f"The index is out of range. The range is from 0 to {len(todos) - 1}")
                    continue
        except ValueError:
            print("Please input a number for the index variable")
    elif "exit" in user_action:
        break
    else:
        print("Hey, we do not support this option")
print("Bye for now")
