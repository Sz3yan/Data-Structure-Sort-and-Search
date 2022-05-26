# Background
# The  purpose  of  the  system  is  to  allow  a  renowned  hotel  to  manage  the  Staycation  booking  
# records for the packages they offered. They can display and update staycation booking records 
# from the system. User can perform searching and sorting of records. You would need to apply 
# knowledge from the practical sessions to complete this assignment. 

# bonus feature
# |-- room management
# |-- customer can book
# |-- give rewards to customers based on their bookings
# |-- customer can cancel their booking

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

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, new_name):
        self.__customer_name = new_name

    def get_number_of_pax(self):
        return self.__number_of_pax

    def get_package_cost_per_pax(self):
        return self.__package_cost_per_pax
    
    def __str__(self):
        return f"{self.get_package_name()} | {self.get_customer_name()} | {self.get_number_of_pax()} | {self.get_package_cost_per_pax()}"

def generate():
    global records

    print("Staycation Booking Records" + "\n")

    records = []
    for i in range(10):
        records.append(Booking(f"The {names.get_last_name()} Adventure", names.get_full_name(), random.randint(1,5), random.randint(500,1500)))

def show_records():
    table = []
    for x in records:
        table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax()]
        table.append(table_data)

    print(tabulate(table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)"]) + "\n")

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
    menu_list.append(["8. Exit"])

    # for easier management
    for_choice = [int(menu_list[i][0].split(".")[0]) for i in range(len(menu_list))]

    time.sleep(1) # to make the output a little more readable
    print(tabulate(menu_list, headers=["Menu", "Description"]) + "\n")

    ask = int(input("Enter your choice: "))
    if ask not in for_choice:
        print("Invalid choice. Please try again")
        menu()

    choice()

def choice():
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
        new_name = input("Enter new customer name: ")
        linear_search(records, search_name, new_name)
        menu()

    elif ask == 6:
        print("Search record by Package Name using Binary Search and update record" + "\n")
        binary_search()
        menu()

    elif ask == 7:
        print("List records range from $X to $Y. e.g $100-200" + "\n")
        wot_range = input("Enter the range (e.g 100-200): $")
        filered_record = []

        # implement error handling
        for x in records:
            if int(wot_range.split("-")[0]) <= x.get_package_cost_per_pax() <= int(wot_range.split("-")[1]):
                filered_record.append(x)

        insertion_sort(filered_record)

        filtered_table = []
        for x in filered_record:
            table_data = [x.get_package_name(), x.get_customer_name(), x.get_number_of_pax(), x.get_package_cost_per_pax()]
            filtered_table.append(table_data)

        print(tabulate(filtered_table, headers=["Package Name", "Customer Name", "Number of Pax", "Package Cost Per Pax ($)"]) + "\n")
        menu()

    # implement bonous feature => something that value add to the system

    elif ask == 8:
        print("Exit")
