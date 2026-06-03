## 2. Project Description



## 3. Libraries Used

| Library | Version | How it was used |
|---|---|---|
| json | built-in | Load and save bus routes |
| csv | built-in | Load and save student reservations |
| matplotlib | write version here | Create occupancy and reservation charts |

## 4. Module Descriptions

### bus_manager.py


### reservation_manager.py
The bus reservation system module. It loads reservations from a csv, saves updated reservations, add new reservation, cancel existing reservation, and filter the reservations according to routes The key method here is the book() method as it check whether the route exist, it also prevents duplicate reservation and if there is enough seats it will then create the new reservation.

### visualizer.py
This module makes charts for the bus reservation system. It displays a bar chart showing booked and available seats for each route on a specific date. It also shows a pie chart that outlines total reservations broken down by route, so users can easily see all the info at a glance.

### main.py
This file run the whole project. It loads routes and reservations, shows bus availability, creates a test reservation, saves the update, and displays the charts.

## 5. Test Cases

### Test: available_seats()

**Input:** Route R01 with capacity 30 and existing reservations on 2026-05-15  
**Expected Output:** Available seats are calculated correctly.  
**Actual Output:** The method returned the correct number of available seats.

### Test: Successful Booking
I tested the booking method by adding a new reservation for asma bzoor 

**Input:** student name :Asma bzoor 
student id :202210754
Route id :R01
date : 2026-06-03  
**Expected Output:** the system should add the new reservation if the route exists and seats are available  
**Actual Output:** Reservation confirmed successfully.

### Test: Duplicate Booking
i tested the booking method by trying to reserve the same route for the same student again 
**Input:** student id : 202210754
route id :R01
date: 2026-06-03 
**Expected Output:** ValueError: the system should not add the same route again 
**Actual Output:** ValueError was raised successfully.

### Test: Cancel Reservation

**Input:** RES001   
**Expected Output:** The reservation with id RES001 should be removed   
**Actual Output:** reservation removed successfully .

### Test: Full main.py Run

**Input:** Run `python main.py`  
**Expected Output:** The program runs without errors and displays both charts.  
**Actual Output:** Write actual result here after testing.

## 6. Screenshots

### Occupancy Chart
<img width="1251" height="824" alt="WhatsApp Image 2026-06-03 at 9 11 47 PM" src="https://github.com/user-attachments/assets/08745f4e-9166-4f80-baaa-c696d4d1d0a6" />


### Route Pie Chart
<img width="882" height="844" alt="WhatsApp Image 2026-06-03 at 9 12 05 PM" src="https://github.com/user-attachments/assets/e7e5e96d-54b6-4ca0-99e7-a5592ce4e2d8" />


### Terminal Output
<img width="1142" height="429" alt="WhatsApp Image 2026-06-03 at 9 47 59 PM" src="https://github.com/user-attachments/assets/605886d3-35dc-4560-97b1-280de6c0a59c" />


## 7. Individual Contributions

| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| Lona Yahya | 202210668 | bus_manager.py, create_sample_data.py | write count | @username |
| Asma Bzoor | 202210754 | reservation_manager.py, requirements.txt |  6| @assma122 |
| Jana Soghier | 202210337 | visualizer.py, main.py | write count | @username |

## 8. Challenges & What You Learned

### Lona Yahya
Write Lona challenge here.

### Asma Bzoor
The difficult task here was booking validation. The students must not be allowed to book the same route on the same date more than one time and before a student could book an available seats are checked. To check if a student book a route on a date more than once, the reservations list is checked, and before reservation is allowed seat available is also checked using the available_seats() of BusManager method.

### Jana Soghier
Handling system integration and data visualization was super tough. Merging the bus management, reservation systems, and data generation modules meant meticulously organizing `main.py` for seamless data flow. Building `visualizer.py` involved handling raw reservation logs to calculate route popularity and bus occupancy rates dynamically. 
## 9. How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create sample data
```bash
python create_sample_data.py
```

### Run the app
```bash
python main.py
```
