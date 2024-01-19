#To Do List
#1/10/24
#Suzanna M, Lam M

#Intialize
print("""Welcome to the grocery list. 
          You can add an item (1), 
          View the list (2), 
          Mark a task as done (3), 
          Remove an item (4),
          Clears the list(5)
          Alphabetize the list (6)
         Counts the items on the list(7) 
          And Quit (8)""")
grocery=[]

#Function
#Option 1: Allows user to add something on to the list
def add():
    item1=input("What do you want to add: ")
    grocery.append(item1)
#Option 2: Allows user to see their list
def view():
    print(grocery)
#Option 3: Allows user to mark an item as done with an X
def mark():
    ans=input("select a item from the list to mark as done: ")
    i=grocery.index(ans)
    grocery[i]=ans+" X"
#Option 4: Allows user to remove a specific item from the list
def remove():
    thing2=input("What item do you want to remove: ")
    i=grocery.index(thing2)
    grocery.pop(i)
#Option 5 : Allows users to Clear the entire list of notes. 
def clear():
    grocery.clear()
    print("Your list has been cleared")

#Option 6 : Implement the ability to sort the list in alphabetical order.
def sort():
    grocery.sort()
    print("Your list has been sorted")

#Option 7 : Provide an option that counts and displays the total number of notes currently in the list.
def count():
    num = len(groceryList)
    print("You have " + num + " groceries on your list")
#Option 8 : Exits program
def exit():
    print("Goodbye.")
    quit()
#Asks user for an input and then runs the opperation to that coresponding number
def groceryList():
    user=int(input("Which option: "))
    if (user==1):
        add()
    elif (user==2):
        view()
    elif (user==3):
        mark()
    elif (user==4):
        remove()
    elif(user==5):
        clear()
    elif(user==6):
        sort()
    elif(user==7):
        count()
    elif(user==8):
        exit()
    else:
        print("Please enter a number from 1-8")
        groceryList()
    groceryList()

#Main
groceryList()
