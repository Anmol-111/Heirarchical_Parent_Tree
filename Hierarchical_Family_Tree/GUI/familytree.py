import Bussiness_Entities.Entities as Bent
import Bussiness_Access_Layer as Bal
obj_ent=Bent.C_Family_Entities()
def display_menu():
    print("Menu:")
    print("1. Create new family tree.")
    print("2. Print the family tree.")
    print("3. Add new member to the family tree.")
    print("4. Remove member from the family tree.")
    print("5. Exit.")
def main():
    display_menu()
    choice = int(input("Enter the choice(1-5):"))
    if choice == 1:
        name= input("Enter the Root Name: ")
        obj_ent.set_root_name(name)
        age = int(input("Enter the age: "))
        obj_ent.set_root_age(age)
    elif choice == 2:
        pass
    elif choice == 3:
        name = input("Enter the Root Name: ")
        obj_ent.set_name(name)
        age = int(input("Enter the age: "))
        obj_ent.set_age(age)
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        print("Please enter the correct choice.")
if __name__ == "__main__":
    main()