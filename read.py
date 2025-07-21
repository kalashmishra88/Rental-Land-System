def read_land_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_land_data(land_data):
    lands = []
    for line in land_data:
        fields = line.split(',') #All of the land details
        land = {
            'kitta_number': fields[0].replace(' ', ''),
            'city': fields[1].replace(' ', ''),
            'direction': fields[2].replace(' ', ''),
            'anna': int(fields[3].replace(' ', '')),
            'price': int(fields[4].replace(' ', '')),
            'status': fields[5].replace(' ', ''),
            'duration': int(fields[6].replace(' ', '')) if len(fields) > 6 else 0
        }
        lands.append(land)
    return lands
