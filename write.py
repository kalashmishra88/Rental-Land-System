def write_land_data(file_path, lands):
    with open(file_path, 'w') as file:
        for land in lands:  #All of the land details
            file.write(','.join([
                land['kitta_number'],
                land['city'],
                land['direction'],
                str(land['anna']),
                str(land['price']),
                land['status'],
                str(land['duration'])
            ]) + '\n')

def generate_invoice(file_name, transaction_data):
    with open(file_name, 'w') as file:
        for key, value in transaction_data.items():
            file.write(key + ": " + value + '\n')
