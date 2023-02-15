import distances
import load_trucks

# truck lists
truck_one_list = []
truck_two_list = []
truck_three_list = []

# truck distance storage
truck_one_distance = []
truck_two_distance = []
truck_three_distance = []

# start time for trucks
truck_one_start = ['8:00:00']
truck_two_start = ['9:10:00']
truck_three_start = ['11:00:00']

total_distance_tr1 = 0
total_distance_tr2 = 0
total_distance_tr3 = 0


# truck one
# set delivery start time to packets of truck 1   :> O(n)

def set_delivery_time(truck_num):
    truck_type = None
    list_type = None
    distance = None

    if truck_num == 1:
        truck_type = load_trucks.get_truck1_list()
        list_type = truck_one_list
        distance = truck_one_distance
    elif truck_num == 2:
        truck_type = load_trucks.get_truck2_list()
        list_type = truck_two_list
        distance = truck_two_distance
    elif truck_num == 3:
        truck_type = load_trucks.get_truck3_list()
        list_type = truck_three_list
        distance = truck_three_distance

    for index, value in enumerate(truck_type):
        truck_type[index][9] = truck_one_start[0]
        list_type.append(truck_type[index])

    # Compare first truck addresses to full address list  O(n^2)
    for index, outer in enumerate(list_type):
        for inner in distances.get_address():
            if outer[2] == inner[2]:
                distance.append(outer[0])
                list_type[index][1] = inner[0]

    # Call greedy  algorithm to sort packages for first truck
    distances.find_fastest_route(list_type, 1, 0)

    # Calculate  O(n)
    # 1.Total distance of the First truck
    # 2.distance of each packages


def get_distance_traveled(truck_num, total_distance):
    distance = None
    sorted_truck = None
    list_type = None

    if truck_num == 1:
        distance = distances.get_first_tr_sort_index()
        sorted_truck = distances.get_first_tr_sort_list()
        list_type = truck_one_list
    elif truck_num == 2:
        distance = distances.get_second_tr_sort_index()
        sorted_truck = distances.get_second_tr_sort_list()
        list_type = truck_two_list
    elif truck_num == 3:
        distance = distances.get_third_tr_sort_index()
        sorted_truck = distances.get_third_tr_sort_list()
        list_type = truck_three_list

    for index in range(len(distance)):
        try:
            total_distance = distances.get_distance(int(distance[index]),
                                                    int(distance[index + 1]),
                                                    total_distance)
            deliver_package = distances.get_time(
                distances.get_current_distance(int(distance[index]),
                                               int(distance[index + 1])),
                truck_one_start)
            sorted_truck[index][10] = (str(deliver_package))
            load_trucks.get_hash_table().update(int(sorted_truck[index][0]), list_type)

        except IndexError:
            pass


# Get the total distance of all 40 packages :> O(1)
def get_total_distance():
    set_delivery_time(1)
    set_delivery_time(2)
    set_delivery_time(3)
    get_distance_traveled(1, total_distance_tr1)
    get_distance_traveled(2, total_distance_tr2)
    get_distance_traveled(3, total_distance_tr3)
    return total_distance_tr1 + total_distance_tr2 + total_distance_tr3


'''
 
    def sort_distances(self):
        current_location = self.get_location()
        miles = []
        for package in self.storage:
            start = location_storage.search(f'{current_location}')
            end = location_storage.search(f'{package}')
            this_distance = distances.get_distance(start, end, 0)
            miles.append(this_distance)

        miles.sort()
        return miles
        
        
            def drive_to_next_location(self):
        distance_list = self.sort_distances()
        lowest = 10000
        for miles in distance_list:
            for package in self.storage:
                current_location = self.get_location()
                start = location_storage.search(f'{current_location}')
                end = location_storage.search(f'{package}')
                this_distance = distances.get_distance(int(start), int(end), 0)
                if this_distance == miles:
                    lowest = this_distance
                    self.set_location(package)
                    self.set_miles(self.get_miles() + lowest)
                    self.unload_truck(package)
    

'''
