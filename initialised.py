# Background
# The  purpose  of  the  system  is  to  allow  a  renowned  hotel  to  manage  the  Staycation  booking  
# records for the packages they offered. They can display and update staycation booking records 
# from the system. User can perform searching and sorting of records. You would need to apply 
# knowledge from the practical sessions to complete this assignment. 

# bonus feature
# |-- room management
# |-- give rewards to customers based on their bookings

import random, names, time
from tabulate import tabulate
from algorithms import bubble_sort, selection_sort, insertion_sort, linear_search, binary_search

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

    print(tabulate(table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)", "Total ($)"]) + "\n")

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
    menu_list.append(["7. List records range from $X to $Y. e.g $100-200"])
    menu_list.append(["8. Add/Remove booking"])
    menu_list.append(["9. See Loyal Customers"])
    menu_list.append(["10. Exit"])

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
        print("List records range from $X to $Y. e.g $100-200" + "\n")
        try:
            wot_range = input("Enter the range (e.g 100-200): $")

            if "-" not in wot_range:
                print("Invalid input. Please try again")
                choice()

            lower_limit = int(wot_range.split("-")[0])
            upper_limit = int(wot_range.split("-")[1])

            # if user enters opposite, system will still be able to display the range accordinly
            if lower_limit > upper_limit:
                upper_limit, lower_limit = lower_limit, upper_limit

            filered_record = []

            for x in records:
                # do swap if the input is not in the format of $100-200
                if lower_limit <= x.get_package_cost_per_pax() <= upper_limit:
                    filered_record.append(x)

            insertion_sort(filered_record)

            filtered_table = []
            for x in filered_record:
                table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax()]
                filtered_table.append(table_data)

            print(tabulate(filtered_table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)"]) + "\n")
            menu()

        except ValueError:
            print("Invalid input. Please try again")
            choice()

    # can add and remove. but remove: need to sort first and fix. 
    elif ask == 8:
        print("Add/Remove booking" + "\n")

        add_or_remove = input("Enter 'a' to add a new booking or 'r' to remove a booking: ").upper()
        new_name = input("Enter your name: ")

        if add_or_remove == "A":
            records.append(Booking(f"The {names.get_last_name()} Adventure", new_name, random.randint(1,5), random.randint(500,1500)))
            print("Booking added")
            show_records()
            menu()

        elif add_or_remove == "R":
            if new_name in [i.get_customer_name() for i in records]:
                for i in records:
                    if new_name == i.get_customer_name():
                        records.remove(i)
                print("Booking removed")
                show_records()
                menu()
            
            else:
                print("Customer not found, please try again")
                choice()
        
    elif ask == 9:
        print("See Best" + "\n")


    elif ask == 10:
        print("Exit")
        exit()
