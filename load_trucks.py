import csv

from hash_table import HashTable

storage = HashTable()  # Create an instance of HashTable class
truck1_list = []  # packages list for truck 1
truck2_list = []  # packages list for truck 2
truck3_list = []  # packages list for truck 3


with open('../wgups_melissa_aybar_c950/Data/Packages.csv', 'r') as file:
    reader = list(csv.reader(file, delimiter=','))
    for row in reader:
        package_id = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        requirements = row[5]
        weight = row[6]
        notes = row[7]
        start_time = ''
        location = ''
        status = 'At hub'
        value = [package_id, location, street, city, state, zip_code, requirements, weight, notes, start_time, status]

        if 'EOD' not in value[6]:
            if 'Delayed on flight---will not arrive to depot until 9:05 am' in value[8] or '3365 S 900 W' in value[2]:
                truck2_list.append(value)
            elif '3365 S 900 W' in value[2]:
                truck2_list.append(value)
            else:
                truck1_list.append(value)

        elif ('EOD' in value[6]) and ('none' not in value[8]):
            if 'Wrong address listed' in value[8]:
                truck3_list.append(value)
            elif '84103' in value[5]:
                truck3_list.append(value)
            else:
                truck2_list.append(value)

        elif ('EOD' in value[6]) and ('none' in value[8]):
            if '177 W Price Ave' in value[2] or '2010 W 500 S' in value[2] or '1330 2100 S' in value[2] or ('3575 W Valley Central Station bus Loop' in value[2]) or ('3148 S 1100 W' in value[2]):
                truck1_list.append(value)

            else:
                if ('84103' in value[5]) or ('84111' in value[5]) or ('84117' in value[5]) or ('84119' in value[5]):
                    if '300 State St' in value[2]:
                            truck3_list.append(value)
                    else:truck2_list.append(value)

                else:
                    truck3_list.append(value)

        # Insert value into the hash table

        storage.insert(package_id, value)


    def get_truck1_list():
        return truck1_list

    # Get packets list assigned to truck 2  :> O(1)
    def get_truck2_list():
        return truck2_list

    # Get packets list assigned to truck 3  :> O(1)
    def get_truck3_list():
        return truck3_list

    # Get full list of packages :> O(1)
    def get_hash_table():
        return storage



