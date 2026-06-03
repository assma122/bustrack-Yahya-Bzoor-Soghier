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


### main.py


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
![Occupancy Chart](screenshots/occupancy_chart.png)

### Route Pie Chart
![Route Pie Chart](screenshots/route_pie_chart.png)

### Terminal Output
![Terminal Output](screenshots/terminal_output.png)

## 7. Individual Contributions

| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| Lona Yahya | 202210668 | bus_manager.py, create_sample_data.py | write count | @username |
| Asma Bzoor | 202210754 | reservation_manager.py, requirements.txt |  9| @assma122 |
| Jana Soghier | 202210337 | visualizer.py, main.py | write count | @username |

## 8. Challenges & What You Learned

### Lona Yahya
Write Lona challenge here.

### Asma Bzoor
The difficult task here was booking validation. The students must not be allowed to book the same route on the same date more than one time and before a student could book an available seats are checked. To check if a student book a route on a date more than once, the reservations list is checked, and before reservation is allowed seat available is also checked using the available_seats() of BusManager method.

### Jana Soghier

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
