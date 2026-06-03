import json
class BusManager: 
    def load_routes(self, filepath:str)->list:
     try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data["routes"]
        
     except FileNotFoundError:
         raise FileNotFoundError("file not found check the routers you want again")

    def get_route(self, routes:list, route_id:str)->dict:
       for route in routes:
         if route["route_id"].upper() == route_id.upper():
          return route
       return None
    
    def available_seats(self, routes: list, reservations: list, route_id: str, date: str) -> int:
       print(f"Checking available seats for route {route_id} on {date}")
       r=self.get_route(routes, route_id)
       print(r)
       if r is None:
          raise ValueError("route not found check the route_id you want again")
       booked=sum(1 for r in reservations 
        if r["route_id"].upper() == route_id.upper() and r["date"] == date)
       return r["capacity"]-booked
    



    def display_routes(self, routes: list, reservations: list, date: str) -> None:
       
       print ("Route ID  | From       | To   | Departure | Capacity | Booked | Available")
       print ("----------|------------|------|-----------|----------|--------|----------")
       for r in routes:
          booked=0
          for s in reservations:
            if s["route_id"]==r["route_id"] and s["date"]==date:
             booked=booked+1
          available_seat=r["capacity"]-booked
          print (f"{r['route_id']:<10}|" f"{r['from']:<12}|" f"{r['to']:<6}|" f"{r['departure']:<11}|"  f"{r['capacity']:<10}|"  f"{booked:<8}|" f"{available_seat:<10}" )

  








            

            
          



