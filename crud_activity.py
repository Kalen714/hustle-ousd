list = []
def create (recipe):
    list.append(recipe)
    print(recipe)
def read_index (index):
    if index > len(list):
        return list[index]
    else:
        return "invalid index"
def update(index,recipe):
    if index > len(list):
        old = list[index]
        list[index] = recipe
    else:
        print("wrong index")
def destroy(read_index):
    print(read_index)
def list_all_recipes(cookbook):
 print("Index is out of range.")
 def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            def read(index)
            print("Index is out of range.")
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
