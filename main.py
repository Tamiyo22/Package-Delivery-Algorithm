
import csv

import load_trucks
from hash_table import HashTable
from locations import Distances
from load_trucks import get_hash_table
from packages import get_total_distance
import datetime


''' 
WGU = Distances(0.0, 7.2, 3.8, 11.0, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7, 7.6, 2.0, 3.6, 6.5,
                1.9, 3.4, 2.4, 6.4, 2.4, 5.0, 3.6)
one = Distances(7.2,0.0)
two = Distances(3.8,7.1,0.0)
three = Distances(11.0,6.4,9.2,0.0)
four = Distances(2.2, 6.0, 4.4, 5.6, 0.0)
five = Distances(3.5,4.8,2.8,6.9,1.9,0.0)
six = Distances(10.9,1.6,8.6,8.6,7.9,6.3,0.0)
seven = Distances(8.6,2.8,6.3,4.0,5.1,4.3,4.0,0.0)
eight = Distances(7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.0)
nine = Distances(2.8,6.3,1.6,7.3,2.6,1.5,8.0,9.3,4.8,0.0)
ten = Distances(6.4,7.3,10.4,1.0,6.5,8.7,8.6,4.6,11.9,9.4,0.0)
eleven = Distances(3.2,5.3,3.0,6.4,1.5,0.8,6.9,4.8,4.7,1.1,7.3,0.0)
twelve = Distances(7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.6,5.1,12.0,4.7,0.0)
thirteen = Distances(5.2,3.0,6.5,3.9,3.2,3.9,4.2,1.6,7.6,4.6,4.9,3.5,7.3,0.0)
fourteen = Distances(4.4,4.6,5.6,4.3,2.4,3.0,8.0,3.3,7.8,3.7,5.2,2.6,7.8,1.3,0.0)
fifteen = Distances(3.7,4.5,5.8,4.4,2.7,3.8,5.8,3.4,6.6,4.0,5.4,2.9,6.6,1.5,0.6,0.0)
sixteen = Distances(7.6,7.4,5.7,7.2,1.4,5.7,7.2,3.1,7.2,6.7,8.1,6.3,7.2,4.0,6.4,5.6,0.0)
seventeen = Distances(2.0,6.0,4.1,5.3,0.5,1.9,7.7,5.1,5.9,2.3,6.2,1.2,5.9,3.2,2.4,1.6,7.1,0.0)
eighteen = Distances(3.6,5.0,3.6,6.0,1.7,1.1,6.6,4.6,5.4,1.8,6.9,1.0,5.4,3.0,2.2,1.7,6.1,1.6,0.0)
nineteen = Distances(6.5,4.8,4.3,10.6,6.5,3.5,3.2,6.7,1.0,4.1,11.5,3.7,1.0,6.9,6.8,6.4,7.2,4.9,4.4,0.0)
twenty = Distances(1.9,9.5,3.3,5.9,3.2,4.9,11.2,8.1,8.5,3.8,6.9,4.1,8.5,6.2,5.3,4.9,10.6,3.0,4.6,7.5,0.0)
twenty_one = Distances(3.4,10.9,5.0,7.4,5.2,6.9,12.7,10.4,10.3,5.8,8.3,6.2,10.3,8.2,7.4,6.9,12.0,5.0,6.6,9.3,2.0,0.0)
twenty_two = Distances(2.4,8.3,6.1,4.7,2.5,4.2,10.0,7.8,7.8,4.3,4.1,3.4,7.8,5.5,4.6,4.2,9.4,2.3,3.9,6.8,2.9,4.4,0.0)
twenty_three = Distances(6.4,6.9,9.7,0.6,6.0,9.0,8.2,4.2,11.5,7.8,0.4,6.9,11.5,4.4,4.8,5.6,7.5,5.5,6.5,11.4,6.4,7.9,4.5,0.0)
twenty_four = Distances(2.4,10.0,6.1,6.4,4.2,5.9,11.7,9.5,9.5,4.8,4.9,5.2,9.5,7.2,6.3,5.9,11.1,4.0,5.6,8.5,2.8,3.4,1.7,5.4,0.0)
twenty_five = Distances(5.0,4.4,2.8,10.1,5.4,3.5,5.1,6.2,2.8,3.2,11.0,3.7,2.8,6.4,6.5,5.7,6.2,5.1,4.3,1.8,6.0,7.9,6.8,10.6,7.0,0.0)
twenty_six = Distances(3.6, 13.0,7.4,10.1,5.5,7.2,14.2,10.7,14.1,6.0,6.8,6.4,14.1,10.5,8.8,8.4,13.6,5.2,6.9,13.1,4.1,4.7,3.1,7.8,1.3,8.3,0.0)

'''
'''  
myTestTruck = HashTable()
myTestTruck.insert(WGU.wgu,WGU.twenty)
myTestTruck.insert('one',WGU.one)
print(myTestTruck.search('one'))


print(WGU.twenty)
print(myTestTruck.table)


truck1 = []
truck1_list = ["1", "13", "14", "15", "16", "20", "29", "30", "31", "34", "37", "40"]
truck2 = []
truck2_list = ["2", "3", "6", "8", "10", "12", "18", "21", "23", "25", '27", "28', '32', '36', '38']
truck3 = []
truck3_list = ["4", "5", "7", "9", '11', '17', '19', '22', '24', '26', '33', '35', '39']
package_hash = HashTable()
keys = []


#storage = HashTable();

#truck1 = []
#truck1_list = ["1", "13", "14", "15", "16", "20", "29", "30", "31", "34", "37", "40"]
#truck2 = []
#truck2_list = ["2", "3", "6", "8", "10", "12", "18", "21", "23", "25", '27", "28', '32', '36', '38']

#storage.insert("dog","walk")
#rint(storage.table)
storage.insert("cat","sleep")
print(storage.table)
print(storage.search("cat"))



print(cvs_reader.get_hash_table().table)

'''
# reusable print  functions :> O(1)
def print_status(count):
    print(

        f'Package ID: {get_hash_table().search(str(count))[0]}', """    """
                                                                 f'Truck load time: {get_hash_table().search(str(count))[9]}',
        """    """
        f'Delivery status: {get_hash_table().search(str(count))[10]}'
    )


# reusable print  functions :> # O(1)
def print_pk_detail(count):
    print(
        '-' * 30, 'package information', '-' * 49, '\n'
                                                   f'Package ID: {get_hash_table().search(str(count))[0]}\n'
                                                   f'Street address: {get_hash_table().search(str(count))[2]}, '
                                                   f'{get_hash_table().search(str(count))[3]}, '
                                                   f'{get_hash_table().search(str(count))[4]}, '
                                                   f'{get_hash_table().search(str(count))[5]},\n'

                                                   f'Delivery deadline : {get_hash_table().search(str(count))[6]}\n'
                                                   f'Package weight: {get_hash_table().search(str(count))[7]} KG\n'
                                                   f'Special note: {get_hash_table().search(str(count))[8]}\n',
        '-' * 30, 'delivery status', '-' * 51,
    )


class Main:
    # welcome page Header
    print('*' * 100)
    print('----------------------------  WGUPS - Packet Tracking Console  ------------------------------------',
          sep='\n')
    print('*' * 100)

    # total delivery package for all 40 packets
    print('# Complete delivery of all 40 packets was completed at ', "{0:.2f}".format(get_total_distance(), 2),
          'miles.\n')

    # display today's date and time
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S\n")
    cur_date = now.strftime("%Y-%m-%d\n")
    print(""" #Today is          :""", cur_date, """#Current time      :""", cur_time)


    # initial user selection : report for  1 packet or all packets
    user_input = int(input("""
    TYPE 1 : To  lookup  ALL  package packages 
    TYPE 2 : To  lookup  an individual package\n  """))
    if user_input > 2 or user_input < 1:
        print("Invalid entry")
        exit()

    while user_input != 'quit':

        # user input : Timeframe to retrieve report
        input_time_raw = input('Enter a time to retrieve report (HH:MM:SS):\n')
        print('-' * 100)
        (hrs0, mins0, secs0) = input_time_raw.split(':')
        input_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))

        # Case if user selects Option #1
        # Get info for all packages at given time  O(n)
        if user_input == 1:
            try:
                for count in range(1, 41):

                    try:
                        # Time variables (T1 : start time, T2: delivery time )
                        t1_temp = get_hash_table().search(str(count))[9]
                        t2_temp = get_hash_table().search(str(count))[10]

                        (hrs1, mins1, secs1) = t1_temp.split(':')
                        (hrs2, mins2, secs2) = t2_temp.split(':')

                        T1 = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
                        T2 = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))

                    except ValueError:
                        pass

                    # Determine which packages have left the hub
                    if T1 >= input_time:
                        get_hash_table().search(str(count))[10] = 'At Hub'
                        get_hash_table().search(str(count))[9] = t1_temp
                        print_status(count)  # Print package's current info


                    # Determine which packages have left but have not been delivered
                    elif T1 <= input_time:
                        if input_time < T2:
                            get_hash_table().search(str(count))[10] = 'In transit'
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info

                        # Determine which packages have already been delivered
                        else:
                            get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info
                break


            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()



        # Case if user selects Option #2
        # Get info for a single package at a particular time -> O(n)
        # ------------------------------ CASE 2 : SINGLE PACKET REPORT ------------------------------------------------
        elif user_input == 2:
            try:
                # Time variables (T1 : start time, T2: delivery time )
                count = input('Enter a valid package ID: \n')
                t1_temp = get_hash_table().search(str(count))[9]
                t2_temp = get_hash_table().search(str(count))[10]

                (hrs, mins, secs) = t1_temp.split(':')
                (hrs, mins, secs) = t2_temp.split(':')

                T1 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                T2 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                print_pk_detail(count)  # prints specified packet's info

                # Determine which packages have left the hub
                if T1 >= input_time:

                    get_hash_table().search(str(count))[10] = 'At Hub'
                    get_hash_table().search(str(count))[9] = t1_temp

                    print_status(count)  # Print package's current delivery status

                # Determine which packages have left but have not been delivered
                elif T1 <= input_time:

                    if input_time < T2:
                        get_hash_table().search(str(count))[10] = 'In transit'
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

                    # Determine which packages have already been delivered
                    else:
                        get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

            except ValueError:
                print('Invalid entry')
                exit()


        # Case Error
        # Print Invalid Entry and quit the program
        else:
            print('Invalid entry!')
            exit()