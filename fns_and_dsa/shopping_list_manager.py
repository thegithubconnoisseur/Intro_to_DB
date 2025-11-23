

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
        choice = input("Enter your choice: ")

        if  choice == '1':
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
        elif choice == '2':
            search_item = input("What item would your like to remove: ")
            if search_item in shopping_list:
                shopping_list.remove(search_item)
            else:
                print("This item is not on the list")
        elif choice == '3':
            for items in shopping_list:
                print(items)
        elif choice == '4' :
            print("Goodbye")
            break
        else:
            print("Invalid choice. Pleas try again.")



if __name__ == '__main__':
    main()