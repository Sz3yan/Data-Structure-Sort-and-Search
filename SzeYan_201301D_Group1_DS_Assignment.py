# Background
# The  purpose  of  the  system  is  to  allow  a  renowned  hotel  to  manage  the  Staycation  booking  
# records for the packages they offered. They can display and update staycation booking records 
# from the system. User can perform searching and sorting of records. You would need to apply 
# knowledge from the practical sessions to complete this assignment. 

# bonus feature
# |-- AVL Tree

import random, names, time, os
from tabulate import tabulate
from SzeYan_201301D_Group1_Algorithm import bubble_sort, selection_sort, insertion_sort, linear_search, binary_search, TreeNode, AVL_Tree, insert_data, Search

class Booking:
    def __init__(self, package_name, customer_name, number_of_pax, package_cost_per_pax):
        self.__package_name = package_name
        self.__customer_name = customer_name
        self.__number_of_pax = number_of_pax
        self.__package_cost_per_pax = package_cost_per_pax

    def get_package_name(self):
        return self.__package_name

    def set_package_name(self, new_name):
        self.__package_name = new_name

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, new_name):
        self.__customer_name = new_name

    def get_number_of_pax(self):
        return self.__number_of_pax

    def get_package_cost_per_pax(self):
        return self.__package_cost_per_pax

    def total(self):
        return self.get_number_of_pax() * self.get_package_cost_per_pax()
    
    def __str__(self):
        return f"{self.get_package_name()} | {self.get_customer_name()} | {self.get_number_of_pax()} | {self.get_package_cost_per_pax()} | {self.total()}"

def generate():
    global records

    print("Staycation Booking Records" + "\n")

    records = []
    for i in range(10):
        records.append(Booking(f"The {names.get_last_name()} Adventure", names.get_full_name(), random.randint(1,5), random.randint(500,1500)))

def show_records():
    table = []
    for x in records:
        table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax(), x.total()]
        table.append(table_data)

    print(tabulate(table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)"]) + "\n")

    grand_total = 0
    for i in range(len(records)):
        grand_total += records[i].total()
    print(f"Grand total: ${grand_total}", "\n")

def menu():
    global ask
    
    menu_list = []

    menu_list.append(["1. Display all records"])
    menu_list.append(["2. Sort record by Customer Name using Bubble sort"])
    menu_list.append(["3. Sort record by Package Name using Selection sort"])
    menu_list.append(["4. Sort record by Package Cost using Insertion sort"])
    menu_list.append(["5. Search record by Customer Name using Linear Search and update record"])
    menu_list.append(["6. Search record by Package Name using Binary Search and update record"])
    menu_list.append(["7. Search record by Customer Name using AVL Tree"])
    menu_list.append(["8. List records range from $X to $Y. e.g $100-200"])
    menu_list.append(["9. Exit"])

    # for easier management
    for_choice = [int(menu_list[i][0].split(".")[0]) for i in range(len(menu_list))]

    time.sleep(1) # to make the output a little more readable
    print(tabulate(menu_list, headers=["Menu"]) + "\n")

    try:
        ask = int(input("Enter your choice: "))
        if ask not in for_choice:
            print("Invalid choice. Please try again")
            menu()

        choice()
    except ValueError:
        print("Invalid choice. Please try again")
        menu()

def choice():
    global ask

    if ask == 1:
        print("Display all records" + "\n")
        show_records()
        menu()

    elif ask == 2:
        print("Sort record by Customer Name using Bubble sort" + "\n")
        print("sorting...")
        bubble_sort(records)
        show_records()
        menu()

    elif ask == 3:
        print("Sort record by Package Name using Selection sort" + "\n")
        print("sorting...")
        selection_sort(records)
        show_records()
        menu()

    elif ask == 4:
        print("Sort record by Package Cost using Insertion sort" + "\n")
        print("sorting...")
        insertion_sort(records)
        show_records()
        menu()

    elif ask == 5:
        print("Search record by Customer Name using Linear Search and update record" + "\n")
        search_name = input("Enter customer name: ")

        if search_name not in [i.get_customer_name() for i in records]:
            print("Customer not found, please try again")
            choice()

        new_name = input("Enter new customer name: ")
        linear_search(records, search_name, new_name)
        show_records()
        menu()

    elif ask == 6:
        print("Search record by Package Name using Binary Search and update record" + "\n")
        
        selection_sort(records)
        search_Packagename = input("Enter Package name: ")

        if search_Packagename not in [i.get_package_name() for i in records]:
            print("Package not found, please try again")
            choice()

        new_Packagename = input("Enter new Package name: ")
        binary_search(records, search_Packagename, new_Packagename)
        show_records()
        menu()

    elif ask == 7:
        root = insert_data([i.get_customer_name() for i in records])
        search_name = input('Enter customer name: ')

        if search_name not in [i.get_customer_name() for i in records]:
            print("Customer not found, please try again")
            choice()

        if Search(root, search_name):
            print('"Customer found"')
            filered_record = []

            insertion_sort(filered_record)

            for x in records:
                if search_name == x.get_customer_name():
                    filered_record.append(x)

            filtered_table = []
            for x in filered_record:
                table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax(), x.total()]
                filtered_table.append(table_data)

            print(tabulate(filtered_table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)", "Total ($)"]) + "\n")

            menu()

    elif ask == 8:
        print("List records range from $X to $Y. e.g $100-200" + "\n")
        try:
            wot_range = input("Enter the range (e.g 100-200): $")

            if "-" not in wot_range:
                print("Invalid input. Please try again")
                choice()

            lower_limit = int(wot_range.split("-")[0])
            upper_limit = int(wot_range.split("-")[1])

            if lower_limit > upper_limit:
                upper_limit, lower_limit = lower_limit, upper_limit

            filered_record = []

            for x in records:
                if lower_limit <= x.get_package_cost_per_pax() <= upper_limit:
                    filered_record.append(x)

            insertion_sort(filered_record)

            filtered_table = []
            for x in filered_record:
                table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax(), x.total()]
                filtered_table.append(table_data)

            print(tabulate(filtered_table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)"]) + "\n")
            menu()

        except ValueError:
            print("Invalid input. Please try again")
            choice()
        
    elif ask == 9:
        print("Exit")
        exit()

if __name__ == "__main__":
    os.system("clear") # to clear the terminal on mac os
    os.system("cls") # to clear the terminal on windows
    generate()
    menu()
    choice()