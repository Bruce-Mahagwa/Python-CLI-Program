FILENAME = "todos.txt"

def fetch_todos(filename = FILENAME):
    with open(filename, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filename = FILENAME, todos_list=[]):
    with open(filename, "w") as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello from functions ")