

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print('3. View List')
    print('4. Exit')



def main():
    shopping_list = []

    while True:
        display_menu()
        selection = int(input("Enter your choice: "))

        if selection == 1:
            new_item = input("Add a new item: ")
            shopping_list.append(new_item)
        elif selection == 2:
            search_item = input("What item would your like to remove: ")
            if search_item in shopping_list:
                shopping_list.remove(search_item)
            else:
                print("This item is not on the list")
        elif selection == 3:
            for items in shopping_list:
                print(items)
        elif selection == 4 :
            print("Goodbye")
            break
        else:
            print("Invalid choice. Pleas try again.")



if __name__ == '__main__':
    main()