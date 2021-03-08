documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def check_people(doc, pasp):

        find = False
        for docs in doc:
            if docs['number']==pasp:
                out = docs['name']
                find = True
            if not find:
                out = ("document nof found")
        return out





def find_shelf(shelf, pasp):
    find = False
    for shelfs_key, shelfs_value in shelf.items():
        if pasp in shelfs_value:
            out = shelfs_key
            find = True
        if not find:
            out = ("document nof found")
    return out



def show_documents(doc):
    for docs in doc:
        print(f"{docs['type']} {docs['number']} {docs['name']}")

def add_shelf(directories, name):

    if name in directories.keys():
        print('key found')
    else:
        print('Key added')
        directories[name]=[]


def show_shelf():
    print(directories)


def add_document():



def core(commanda):
    if commanda=="p":
        pasp = input("Please, insert document number: ")
        print(check_people(documents, pasp))
        status_exit = False
        while not status_exit:
            check_exit = input('Would you like continue check? Please tip "Yes or No"')
            if check_exit == "No":
                status_exit = True
            elif check_exit == "Yes":
                pasp = input("Please, insert document number: ")
                print(check_people(documents, pasp))
            else:
                print("Incorrect command")

    elif commanda=="s":
        print("shelf")
        pasp = input("Please, insert document number: ")
        print(find_shelf(directories, pasp))
        status_exit = False
        while not status_exit:
            check_exit = input('Would you like continue check? Please tip "Yes or No"')
            if check_exit == "No":
                status_exit = True
            elif check_exit == "Yes":
                pasp = input("Please, insert document number: ")
                print(find_shelf(directories, pasp))
            else:
                print("Incorrect command")
    elif commanda == "l":
        print("list")
        show_documents(documents)
    elif commanda=="as":
        print("add")
        name_shelf = input("Please, inter shelf name: ")
        print(add_shelf(directories, name_shelf))
        status_exit = False
        while not status_exit:
            check_exit = input('Would you like continue check? Please tip "Yes or No"')
            if check_exit == "No":
                status_exit = True
            elif check_exit == "Yes":
                name_shelf = input("Please, inter shelf name: ")
                print(add_shelf(directories, name_shelf))
            else:
                print("Incorrect command")

    elif commanda=="i":
        print("insert")
    elif commanda=="d":
        print("delete")
    elif commanda == "ss":
        show_shelf()





command =  input("Please insert command: ")

while command != 'e':
    core(command)
    command = input("Please insert command: ")
else:
    print("done")
