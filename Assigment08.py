# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# PShoup,11.27.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PShoup,11.27.2019,Modified code to complete assignment 8
    """
    def __init__(self, product_name: str, product_price: float):
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Do not enter numbers for a product name")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Only enter numbers for product price")

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PShoup,11.27.2019,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was an error in opening the file")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error in saving the file")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def print_menu_items():
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] -")).strip()
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        print("Current items are:")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")

    @staticmethod
    def input_product_data():
        try:
            name = str(input("What is the product name? -").strip())
            price = float(input("What is the price? - ").strip())
            print()
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        IO.print_menu_items()
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            IO.print_current_list_items(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            lstOfProductObjects.append(IO.input_product_data())
            continue
        elif strChoice.strip() == '3':
            FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error in accessing the program")
    print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #
