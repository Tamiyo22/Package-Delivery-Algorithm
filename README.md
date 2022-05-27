# package_delivery
Nearest neighbor algorithm solution for package delivery using python


## Introduction
In this project I was asked to assist the Western Governors University Parcel Service (WGUPS)
with their need to determine an efficient route and delivery distribution for their Daily Local
Deliveries (DLD). The constraints of this project were to deliver 40 packages using efficient
mileage throughout the Salt Lake City area in Utah with a total of two drivers and three trucks.
Each package has notes, deadlines and an address. Each truck can hold 16 packages at a time.
Each delivery needs to be updated in the WGUPS system to ensure that a supervisor can address
any problems that may arise, and track data to adjust for future growth and demand.


## Algorithm Identification
For this task I chose the “Nearest Neighbor Algorithm” as my initial approach to find the best
route, which is heuristic, and is greedy in nature. “A greedy algorithm is an algorithm that, when
presented with a list of options, chooses the option that is optimal at that point in time. The
choice of option does not consider additional subsequent options and may or may not lead to an
optimal solution.” ( Lysecky, R., & Vahid, F.) “A heuristic algorithm is an algorithm that quickly
determines a near optimal or approximate solution.” ( Lysecky, R., & Vahid, F.)
What makes this solution a Nearest Neighbor algorithm is that it makes the most optimal choice
at each stage. At each location, the methods I created will sort through all of the packages on a
truck and find the nearest remaining destination location using a lower bound check of the miles
for each package on board the truck. With the consistent and reliable number of steps, I found
this to be the best method to help with WGUPS’s delivery needs. The greedy nature of this
algorithm ensures that each step will be taken, and each package will be delivered.
The basic travel decisions of each truck are listed below and can be broken into three steps:
1) We sort the packages by mileage to their destination, and return the mileage to the nearest
destination.
2) We match that mileage to the package inside the truck storage and deliver that package.
3) That package location becomes the new current location.
Repeat until there are no longer any packages in the truck storage. By definition this is a heuristic
greedy algorithm since we are sorting at each location to find the nearest location without any
planning or forethought. We are not considering the best route overall, only the best route at each
stop.

## Logic Comments

• Step 1: We sort the packages and find the mileage of the nearest package and return it.
![image](https://user-images.githubusercontent.com/30645979/170785560-e59643ce-068d-4b01-90e2-25ef030b5426.png)

• Step 2  We match that mileage to the package inside the truck storage and deliver that package.
![image](https://user-images.githubusercontent.com/30645979/170785610-a242cb5f-5acb-4438-989c-c4cac50135cf.png)


• Step 3  That package’s location becomes the new current location.
  For this step we need to refer back to the second half of the “Match the lowest miles to package
  method”
 ![image](https://user-images.githubusercontent.com/30645979/170785644-9ed619c4-1cb5-4ce3-86ff-531a40e43380.png)


  
##  Development Environment
Processor: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz 2.59 GHz
Installed RAM: 16.0 GB (15.8 GB usable)
System type: 64-bit operating system, x64-based processor
Integrated Development Environment (IDE): PyCharm 2021.3
Python Version: 3.9


## Space-Time and Big-O

![image](https://user-images.githubusercontent.com/30645979/170783760-89c4a8e9-3cf2-4f55-8fcb-f17232fb7be7.png)

![image](https://user-images.githubusercontent.com/30645979/170784202-4dca6466-9e7d-486c-97c6-07624a2dccff.png)
![image](https://user-images.githubusercontent.com/30645979/170783812-32443433-d377-4a42-849e-fa9d4762c414.png)

![image](https://user-images.githubusercontent.com/30645979/170783965-9e62b466-b28b-44e6-9960-fc948ea402a5.png)

![image](https://user-images.githubusercontent.com/30645979/170784001-0029d613-5703-4742-ac5c-ce7236c4b7cd.png)

![image](https://user-images.githubusercontent.com/30645979/170784065-be5c4462-34a3-4fae-8c4f-15fc41f5bdca.png)

![image](https://user-images.githubusercontent.com/30645979/170784317-e14cf424-ae32-45c5-bcb4-3339548157d7.png)

![image](https://user-images.githubusercontent.com/30645979/170784384-390342af-8fd2-40c3-96cc-6836bc078b2d.png)

![image](https://user-images.githubusercontent.com/30645979/170784407-8b3cf408-b1b9-4886-8b7a-9dec31f40120.png)
![image](https://user-images.githubusercontent.com/30645979/170784457-6cf1f5f6-9e62-4c58-84b2-3575dd9c7079.png)

![image](https://user-images.githubusercontent.com/30645979/170784487-ae35ff3b-20be-4eca-8714-afef4f462035.png)

![image](https://user-images.githubusercontent.com/30645979/170784528-a7d30d0a-dc52-424a-8b59-b64197ff3c71.png)


## Scalability and Adaptability

The hash table class was built using linked lists which grow dynamically. With a list foundation
we are allowed access to Python’s built-in methods such as append, which allows an element to
be appended to the end of a list, and remove, which will remove any item from the list. List items
are changeable, ordered, and allow for duplicate values, making them the perfect flexible
structure that can adapt and scale with business demand.



## Software Efficiency and Maintainability

A Nearest Neighbor algorithm ensures that each step will be taken and each package will be
delivered with a max time complexity of O(N^2) and O(N) space. With the consistent and
reliable number of steps, and no backtracking thanks to using a breadth-first search traversal, I
found this to be the best method to help with WGUPS’s delivery needs at this time. This efficient
algorithm combined with the self-adjusting chaining hash table built using scalable and adaptable
linked lists provides not only a consistent algorithm, but a maintainable one, since the hash table
can make adjustments for growth, and the algorithm guarantees delivery.
Though the Nearest Neighbor was considered suboptimal in similar situations and can sometimes
miss shorter routes when given larger maps to work with, this algorithm is easy and intuitive to
implement. It also executes quickly, and our drivers completed their day by 12:53 p.m., with a
total mileage of 104.4 miles. As time goes on, this document and code comments will help new
hires be able to implement the same software as more hubs are opened throughout the state and
even the country.

## Self-Adjusting Data Structures
The hash table class is built with a linked list of lists that adjusts with growth. Since the hash
uses a chaining technique, collisions are avoided, and since linked lists are the foundation,
adjustable growth is guaranteed. However, as the linked lists grow, the value of N will grow, but
this can be worked with by increasing the size of the hash table.

## Data Structure
I used a chaining hash table with linear probing as the self-adjusting data structure.

## Explanation of Data Structure
The chaining hash table class was built using linked lists which grow dynamically. With a list
foundation we are allowed access to Python’s built-in methods such as append, which allows an
element to be appended to the end of a list, and remove, which will remove any item from the
list. List items are changeable, ordered, and allow for duplicate values, making them the perfect
flexible structure that can adapt and scale.



## Interface

![image](https://user-images.githubusercontent.com/30645979/170785490-ec6d547b-760e-47c2-aa1e-8ca5f59a630e.png)


## Status Check 9:00am
![image](https://user-images.githubusercontent.com/30645979/170785191-06eac384-d3d2-4f25-b727-d6278b4dfac5.png)
![image](https://user-images.githubusercontent.com/30645979/170785224-79f47814-362f-4e58-b811-83ff140ce895.png)
![image](https://user-images.githubusercontent.com/30645979/170785438-28541c98-4c92-45c1-a36e-935c63691b92.png)




## Status Check 10:00am
![image](https://user-images.githubusercontent.com/30645979/170785992-35750c01-38ca-42be-a86a-2f11d957d1c1.png)
![image](https://user-images.githubusercontent.com/30645979/170786153-3f141ae3-3be0-4aa1-bee9-49a7acf88448.png)
![image](https://user-images.githubusercontent.com/30645979/170786189-8a42d34a-55b9-4158-8286-55cd70d7901d.png)



## Status Check 1:00pm
![image](https://user-images.githubusercontent.com/30645979/170786364-d5c4785a-0863-4613-ba58-532cc759e9a8.png)
![image](https://user-images.githubusercontent.com/30645979/170786393-cb98c9e7-e23c-4dff-94f5-05ada5347e6d.png)
![image](https://user-images.githubusercontent.com/30645979/170786427-cae81267-d0dd-4938-b18b-355a4dee8052.png)



## Other possible Algorithms
1) Dijkstra Shortest Path
2) Christofides Algorithm

## Algorithm Differences
### Dijkstra Shortest Path:
Though this algorithm finds the shortest distance, it finds the shortest
from the starting point to all other points. It does not find the minimum distance as we go,
like Nearest Neighbor does. It will not target each stop, and the truck would have had to
keep returning home, wasting time and miles.

### Christofides Algorithm: 
Though this algorithm holds the record for the best approximation
ratio for metric space, for this algorithm to work, the distances between each location would
have to be symmetric. Though the Nearest Neighbor Algorithm is considered more of a
naïve approach in comparison, I felt that the Christofides Algorithm would be better served
as an assistant to a travel plan and not the main plan.



## Different Approach
If I were to do this project again, I would like to try the Farthest Insertion Algorithm. The
Nearest Neighbor Algorithm works fine if the trucks have another destination hub by its last
package; however, having to circle back to the main hub makes the algorithm less simple and
causes an unnecessary circle.
With the Farthest Insertion Algorithm we would deliver our farthest package first and move
inward. The packages would still have to be sorted, but instead of using a linked list, I would use
a stack to push and pop packages on and off of the truck which I believe might be a cleaner
approach to delivery. Even though the Nearest Neighbor Algorithm and the Farthest Insertion
Algorithm both have a time complexity of O(N^2) and a space complexity of O(N), the Farthest
Insertion Algorithm would ensure that the packages that might have been late in a Nearest
Neighbor Algorithm are now on time, and would ensure that we end where we started from.

## Efficiency
The chaining hash table implementation is very efficient for key-value pair data. It is a
dictionary of sorts with a key value lookup. Below is a small demo example of a pet store,
showing how easy it makes inventory look up for the store.

![image](https://user-images.githubusercontent.com/30645979/170787753-bc069b7d-4936-4173-84a6-9855b91bcfad.png)

I implemented a hash table similarly in the project to access and manipulate the data for the
packages:

![image](https://user-images.githubusercontent.com/30645979/170787808-f5b595fc-a27e-42f5-a6b2-9f0404380aa7.png)

The implemented hash table uses linear probing for the functions. Each time a package is accessed for usage the 
worst-case scenario space-time complexity for linear probing is O(N), with N being the number of packages inside
the package storage hash table. Each time we increase the number of packages the time needed to perform look-up
functions grows linearly with it.

##  Other Data Structures

1) Stack
2) Graph


There are multiple ways a stack could have been implemented in this project, one of which is
shown below. The linked lists are great for inserting and removing at random locations; however,
since we already had our distances sorted, and are only adding and removing items from the
truck, a stack with its push and pop methods is much clearer to implement, and allow us much
more control with how memory is allocated and deallocated.
Stack Demo:

![image](https://user-images.githubusercontent.com/30645979/170788171-fb07b21e-35b7-4ec9-adbc-c744288197a5.png)

A graph opens doors to graph traversal, where we visit every vertex in the graph. The vertices in
the graph could be the package locations and would be very intuitive to understand since graphs
are used in many real world applications to represent networks. A graph with depth-first search
would allow us to properly utilize the trucks leaving the hub and coming back to the hub using
backtracking instead of just limiting ourselves to traversing linearly.
Graph Demo:

![image](https://user-images.githubusercontent.com/30645979/170788297-ba70b9db-d3c2-4c59-9388-af6644ccb6a3.png)





