#LINKED LIST
#Declare
global data, ref, freeslot
def initialise(length):
    global data, ref, freepointer, head
    data= [0 for index in range(length)]
    ref= [index + 1 for index in range(length)]
    head = ref
    ref[-1] = None
    freepointer = 0

def printdata(length):
    global data, ref, freeslot
    for i in range(0,len(length)):
        print(f'{i} --- {data[i]} --- {ref[i]}') #Print the data in the list

def link(insertdata):
    global data, ref, freepointer, head
    #Take the next free slot, input data into it, look in the data list, find the position to insert next data
    newindex = freepointer
    ref = -1  # Initialize reference to -1
    currentpointer = head
    while currentpointer != -1 and insertdata > data[currentpointer]:
        ref = currentpointer
        currentpointer = data[currentpointer]
    if currentpointer == head:
        head = newindex
    else:
        data[ref] = newindex
        data[newindex] = currentpointer

    freepointer += 1


#Defining and printing Main program in a separate procedure
def main():
    while True:
        print("0. Initialise the list \n1. Print the data \n2. Quit ")
        choice = int(input("Enter the choice you would like to make: ")) #Asking user for the integer to indicate their choice.
        match choice:
            case 0:
                length = int(input("Enter the length of the list: "))
                initialise(length)
                print("Linked List is initialised. ")
            case 1:
                printdata(length)
            case 2:
                break
main()
