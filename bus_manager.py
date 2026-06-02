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
    
