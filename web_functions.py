FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and returns the list of to-do items."""
    with open(filepath, 'r') as f:
        t = f.readlines()
    return t

def write_todos(t, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as f:
        f.writelines(t)


if __name__ == "__main__":
    print("This is the functions code")
    print(get_todos())