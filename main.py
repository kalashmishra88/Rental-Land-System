import read
import write
import operation

LAND_DATA_FILE = 'land.txt'

def display_lands(lands): #Displaying the details of the land
    print("\nAvailable Lands:")
    print("Kitta Number | City/District | Land Direction |     Area      |    Price     | Duration | Availability  ")
    print("--------------+---------------+----------------+---------------+--------------+----------+---------------")
    for land in lands:
        print("%14s|%15s|%16s|%15s|%14s|%10s|%15s" % (land['kitta_number'], land['city'], land['direction'], str(land['anna']) + ' anna', 'NPR ' + str(land['price']), str(land['duration']) + ' months', land['status']))

def validate_name(name):  #Validating the customer's name
    if not name:
        return False
    for char in name:
        if not (char.isalpha() or char == ' '):
            return False
    if len(name) > 30:
        return False
    return True

def get_customer_name():  #Getting the customer's name
    while True:
        customer_name = input("Enter your name: ")
        if validate_name(customer_name):
            return customer_name
        else:
            print("\n**********************************************************")
            print("Enter a name without special characters or numbers!")
            print("**********************************************************\n")

def main():
    try:
        customer_name = get_customer_name()  #Creating a welcome messsage banner
        print("\n***********************************************************************************************")
        print('''                 __________________________________________________________________________________________
                |                                                                                          |
                |                               WELCOME TO TECHNOPROPERTYNEPAL VENTURES                    |           
                |                                                                                          |
                |                                        Teku, Kathmandu                                   |
                |__________________________________________________________________________________________|
                |                                                                                          |
                |  PLEASE SELECT A CATEGORY AS (1/2/3/4) ACCORDING TO YOUR CHOICE:                         |
                |                                                                                          |
                |  1. SHOW ITEMS                                                                           |
                |  2. RENT LAND                                                                            |
                |  3. RETURN LAND                                                                          |
                |  4. EXIT SHOP                                                                            |
                |__________________________________________________________________________________________|
                     ''')
        lands = []
        while True:
            choice = input("Enter your choice: ")  #Giving choice to the customer
            if choice:
                try:
                    choice = int(choice)
                    if choice == 1:
                        land_data = read.read_land_data(LAND_DATA_FILE)
                        lands = read.parse_land_data(land_data)
                        display_lands(lands)
                    elif choice == 2:
                        if not lands:
                            land_data = read.read_land_data(LAND_DATA_FILE)
                            lands = read.parse_land_data(land_data)
                        kitta_number = input("Enter the kitta number of the land to rent: ")
                        if any(land['kitta_number'] == kitta_number and land['status'] == 'Available' for land in lands):
                            rent_duration = int(input("Enter the duration of rent (months): "))
                            lands, transaction_data = operation.rent_land(lands, kitta_number, customer_name, rent_duration)
                            if transaction_data:
                                invoice_file = "invoice_rent_" + kitta_number + "_" + customer_name + ".txt"
                                write.generate_invoice(invoice_file, transaction_data)
                                print("Invoice generated: " + invoice_file)
                        else:
                            print("Invalid kitta number or land not available for rent.")
                    elif choice == 3:
                        if not lands:
                            land_data = read.read_land_data(LAND_DATA_FILE)
                            lands = read.parse_land_data(land_data)
                        kitta_number = input("Enter the kitta number of the land to return: ")
                        return_duration = int(input("Enter the duration of rent (months): "))
                        lands, transaction_data = operation.return_land(lands, kitta_number, customer_name, return_duration)
                        if transaction_data:  #Generating invoice
                            invoice_file = "invoice_return_" + kitta_number + "_" + customer_name + ".txt"
                            write.generate_invoice(invoice_file, transaction_data)
                            print("Invoice generated: " + invoice_file)
                    elif choice == 4:  #Displaying Thank You message
                        print("******************************************************************************************************")
                        print("                                  Come Back Soon Mr./Mrs. " + customer_name + " !                     ")
                        print("******************************************************************************************************")
                        break
                    else:
                        print("Invalid choice! Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid option! Please enter a valid option.")
            else:
                print("Invalid choice! Please enter a non-empty value.")
            if lands:
                write.write_land_data(LAND_DATA_FILE, lands)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
