import csv 
class ReservationManager: 
  def load_reservations(self,filepath:str)-> list:
    try:
        with open(filepath,"r") as file:
           return list(csv.DictReader(file))
    except FileNotFoundError:
       return []    
     
  def save_reservations(self,reservations:list,filepath:str)->None :
     fieldnames=["res_id", "student_name", "student_id", "route_id", "date"] 
   #open csv file 
     with open(filepath,"w",newline="") as file:
        csvFile = csv.DictWriter(file,fieldnames=fieldnames)
        csvFile.writeheader()
        csvFile.writerows(reservations)

     print("reversation saved")   
  def cancel(self,reservations:list,res_id:str)->list:
    found = False 
    for r in reservations:
       if r ["res_id"]==res_id:
          found =True

    if found == False:
          raise ValueError("reservations not found")  
    updated = [r for r in reservations if r["res_id"]!=res_id]
    print("reversation canceled")
    return updated
  
  def get_by_route(self,reservations:list,route_id:str)->list:
     return [r for r in reservations if r["route_id"]==route_id]
  
      
  def book(self,reservations:list,routes:list 
           ,student_name:str,student_id:str,route_id:str,date:str,bus_manager)->list:
       route = bus_manager.get_route(routes,route_id)
       if route is None :
          raise ValueError("route not found ")
       
       for r in reservations:
          if r["student_id"]==student_id and r["route_id"] == route_id and r["date"] == date:  
             raise ValueError("student already has a reservation for this route on this date")
       available = bus_manager.available_seats(routes,reservations,route_id,date)
       if available<=0:
          raise ValueError("Bus is full")
       new_id = f"RES{len(reservations) + 1:03d}"

       new_reservation = {"res_id":new_id,
                          "student_name":student_name,
                          "student_id":student_id,"route_id":route_id,
                           "date":date                          
                          }
       reservations.append(new_reservation)
       print(f"Reservation confirmed:{new_id} — {student_id} on {route_id} for {date}")
       return reservations