toDoFile = open("toDoList.txt", "w")

toDoList = ""

toDoItem = input("Enter a to do list item: ")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + " \n"
    toDoItem = input("Enter a to do list item: ")

toDoFile.write(toDoList)
toDoFile.close()
