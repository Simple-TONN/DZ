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

def check_people(doc):
    find = False
    pasp = input("Please, insert document number: ")
    for docs in doc:
        if docs['number'] == pasp:
            out = docs['name']
            find = True
        if not find:
            out = ("document nof found")
    return out




def find_shelf(shelf):
    find = False
    pasp = input("Please, insert document number: ")
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




def check_shelf(shelf, name):
    if name in shelf.keys():
        return True
    else:
        return False




def add_shelf(shelf):
    name_shelf = input("Please, inter shelf name: ")
    if check_shelf(shelf,name_shelf):
        out = 'name shelf alregy exist'
    else:
        out = 'Key added'
        shelf[name_shelf] = []
    return out




def show_shelf():
    print(directories)




def add_document(shelf,doc):
    dict_temp={}
    type_document = input("Please, insert document type: ")
    number_document = input("Please, insert document number: ")
    name_document = input("Please, insert document name: ")
    name_shelf =  input("Please, inter shelf name: ")
    if check_shelf(shelf,name_shelf):
        shelf[name_shelf].append(name_document)
        dict_temp['type']=type_document
        dict_temp['number']=number_document
        dict_temp['name']=name_document
        doc.append(dict_temp)
        out = "Document was added"
    else:
        out = "Shelf not found, data not save"
    return out




def delete_document(shelf,doc):
    global documents

############ For Shelf
    number_document = input("Please, insert document number: ")
    for shelfs_key, shelfs_value in shelf.items():
        if number_document in shelfs_value:
            print(shelfs_value.pop(shelfs_value.index(number_document)))
            search_shelf_status = True
            break
        else:
            search_shelf_status = False
    if search_shelf_status:
        print("doc on shelf was delete")
    else:
        print('doc on shelf  not found')

##### For  documents
    for docs in doc:
        if docs['number'] == number_document:

            search_doc_status = True
            break
        else:
            search_doc_status = False
    if search_doc_status:
        new_doc = []
        for docs1 in doc:
            if docs1['number'] != number_document:
                new_doc.append(docs1)
        print("document found")

    else:
        print('document not found')

    documents = new_doc










def core(commanda):
    if commanda == "p":
        print(check_people(documents))
    elif commanda == "s":
        print(find_shelf(directories))
    elif commanda == "l":
        show_documents(documents)
    elif commanda == "a":
        print(add_document(directories,documents))
    elif commanda == "d":
        print("delete")
        delete_document(directories, documents)
    elif commanda == "as":
        print(add_shelf(directories))

    elif commanda == "ss":
        show_shelf()






command = input("Please insert command: ")
while command != 'e':
    core(command)
    command = input("Please insert command: ")
else:
    print("done")

