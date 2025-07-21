import datetime

def validate_name(name):  #Validating the customer's name
    if not name:
        return False
    for char in name:
        if not (char.isalpha() or char == ' '):
            return False
    if len(name) > 30:
        return False
    return True

def rent_land(lands, kitta_number, customer_name, duration):  #Land rent details
    for land in lands:
        if land['kitta_number'] == kitta_number and land['status'] == 'Available':
            now = datetime.datetime.now()
            rent_time = now.strftime("%Y-%m-%d %H:%M:%S")
            total_amount = land['price'] * duration
            land['status'] = 'Not Available'
            land['duration'] = duration  #Setting the duration when rented
            
            transaction_data = {
                'Customer Name': customer_name,
                'Kitta Number': kitta_number,
                'City/District': land['city'],
                'Land Direction': land['direction'],
                'Area': str(land['anna']) + ' anna',
                'Rent Time': rent_time,
                'Duration': str(duration) + ' months',
                'Total Amount': 'NPR ' + str(total_amount)
            }
            
            print("\n--- Rental Details ---")
            for key, value in transaction_data.items():
                print(key + ": " + value)
            print("\nLand rented successfully!")
            return lands, transaction_data
    print("Invalid kitta number or land not available for rent.")
    return lands, None

def return_land(lands, kitta_number, customer_name, return_duration):  #Land return details
    for land in lands:
        if land['kitta_number'] == kitta_number and land['status'] == 'Not Available':
            now = datetime.datetime.now()
            return_time = now.strftime("%Y-%m-%d %H:%M:%S")
            expected_return_duration = land['duration']
            
            #Calculating fine if returning late
            fine = 0
            if return_duration > expected_return_duration:
                late_months = return_duration - expected_return_duration
                fine = late_months * (0.10 * land['price'])
            
            total_amount = land['price'] * return_duration + fine
            land['status'] = 'Available'
            
            transaction_data = {
                'Customer Name': customer_name,
                'Kitta Number': kitta_number,
                'City/District': land['city'],
                'Land Direction': land['direction'],
                'Return Time': return_time,
                'Duration': str(return_duration) + ' months',
                'Area': str(land['anna']) + ' anna',
                'Total Amount': 'NPR ' + str(total_amount),
                'Fine': 'NPR ' + str(fine) if fine > 0 else 'No fine'
            }
            
            print("\n--- Return Details ---")
            for key, value in transaction_data.items():
                print(key + ": " + value)
            print("\nLand returned successfully!")
            return lands, transaction_data
    print("Invalid kitta number or land is not rented currently.")
    return lands, None
