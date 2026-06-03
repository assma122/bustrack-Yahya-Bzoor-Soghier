## 2. Project Description

The BusTrack app helps with booking and tracking bus rides for students. It deals with route info, reservations, and empty seats. Users can upload route details using a JSON file and track reservations through a CSV file. Also, it figures out how many open seats there are and shows route information. This tool is central to the "AAUP Bus Tracking and Reservation system" our  senior project ,it handles data management and reservations. Plus, it offers some analysis and visuals on the reservation stats. It uses json and csv for handling data, and matplotlib to create charts showing bus occupancy and route breakdowns.

## 3. Libraries Used

| Library | Version | How it was used |
|---|---|---|
| json | built-in | Load and save bus routes |
| csv | built-in | Load and save student reservations |
| matplotlib | 3.10.9 | Create occupancy and reservation charts |

## 4. Module Descriptions

### bus_manager.py
This module manges of all bus route data and keeps track of seat availability.It loads route information from a JSON file and uses route IDs as unique identifiers to fetch info.It calculates available seats too and displays routes in a formatted table. This shows all the routes based on reservations and the chosen date.


### reservation_manager.py
The bus reservation system module. It loads reservations from a CSV file, saves updated reservations, adds new reservations, cancels existing reservations, and filters the reservations according to routes. The key method here is the book() method because it checks whether the route exists, prevents duplicate reservations, checks if there are enough seats, and then creates the new reservation.

### visualizer.py
This module makes charts for the bus reservation system. It displays a bar chart showing booked and available seats for each route on a specific date. It also shows a pie chart that outlines total reservations broken down by route, so users can easily see all the info at a glance.

### main.py
This file runs the whole project. It loads routes and reservations, shows bus availability, creates a test reservation, saves the update, and displays the charts.

## 5. Test Cases

### Test: available_seats()

**Input:** Route R01 with capacity 30 and existing reservations on 2026-05-15  
**Expected Output:** Available seats are calculated correctly.  
**Actual Output:** The method returned the correct number of available seats.

### Test: Successful Booking
I tested the booking method by adding a new reservation for Asma Bzoor.

**Input:**  
Student name: Asma Bzoor  
Student ID: 202210754  
Route ID: R01  
Date: 2026-06-03  

**Expected Output:**  
The system should add the new reservation if the route exists and seats are available.

**Actual Output:**  
Reservation confirmed successfully.

### Test: Duplicate Booking
I tested the booking method by trying to reserve the same route for the same student again.

**Input:**  
Student ID: 202210754  
Route ID: R01  
Date: 2026-06-03  

**Expected Output:**  
ValueError: the system should not add the same route again.

**Actual Output:**  
ValueError was raised successfully.

### Test: Cancel Reservation

**Input:**  
RES001  

**Expected Output:**  
The reservation with ID RES001 should be removed.

**Actual Output:**  
Reservation removed successfully.

### Test: Full main.py Run

**Input:** Run `python main.py`  
**Expected Output:** The program runs without errors and displays both charts.  
**Actual Output:** Write actual result here after testing.

## 6. Screenshots

### Occupancy Chart
<img width="1251" height="824" alt="Occupancy Chart" src="https://github.com/user-attachments/assets/08745f4e-9166-4f80-baaa-c696d4d1d0a6" />

### Route Pie Chart
<img width="882" height="844" alt="Route Pie Chart" src="https://github.com/user-attachments/assets/e7e5e96d-54b6-4ca0-99e7-a5592ce4e2d8" />

### Terminal Output
<img width="1142" height="429" alt="Terminal Output" src="https://github.com/user-attachments/assets/605886d3-35dc-4560-97b1-280de6c0a59c" />

## 7. Individual Contributions

| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| Lona Yahya | 202210668 | bus_manager.py, create_sample_data.py | 5| @LunaYahya|
| Asma Bzoor | 202210754 | reservation_manager.py, requirements.txt | 9 | @assma122 |
| Jana Soghier | 202210337 | visualizer.py, main.py | 2 | @janasoghir |

## 8. Challenges & What You Learned

### Lona Yahya
I faced a challenge  where seat bookings weren't calculating right for each route because the counter wasn't resetting within the loop. So, I fixed it by resetting the booked variable for each route and properly filtering reservations based on route_id and date

### Asma Bzoor
The difficult task here was booking validation. The students must not be allowed to book the same route on the same date more than one time, and before a student can book, the available seats must be checked. To check if a student booked a route on a date more than once, the reservations list is checked. Before reservation is allowed, seat availability is also checked using the available_seats() method from BusManager.

### Jana Soghier
Handling system integration and data visualization was super tough. Merging the bus management, reservation systems, and data generation modules meant organizing `main.py` for smooth data flow. Building `visualizer.py` involved handling raw reservation logs to calculate route popularity and bus occupancy rates dynamically.

## 9. How to Run

### Install dependencies
```bash
pip install -r requirements.txt
