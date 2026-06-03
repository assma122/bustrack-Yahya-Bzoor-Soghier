from bus_manager import BusManager
from reservation_manager import ReservationManager
from visualizer import Visualizer


def main():
    ROUTES_FILE = "routes.json"
    RESERVATIONS_FILE = "reservations.csv"
    TARGET_DATE = "2026-05-15"

    bm = BusManager()
    rm = ReservationManager()
    viz = Visualizer()

    print("[1/4] Loading data...")
    routes = bm.load_routes(ROUTES_FILE)
    reservations = rm.load_reservations(RESERVATIONS_FILE)

    print(f"      Routes loaded       : {len(routes)}")
    print(f"      Reservations loaded : {len(reservations)}\n")

    print(f"[2/4] Bus availability for {TARGET_DATE}:")
    bm.display_routes(routes, reservations, TARGET_DATE)

    print("\n[3/4] Making a test reservation...")
    try:
        reservations = rm.book(
            reservations,
            routes,
            student_name="Jana Soghier",
            student_id="202210337",
            route_id="R01",
            date=TARGET_DATE,
            bus_manager=bm
        )
        rm.save_reservations(reservations, RESERVATIONS_FILE)
    except ValueError as e:
        print(f"      Booking failed: {e}")

    print("\n[4/4] Displaying charts...")
    viz.occupancy_chart(routes, reservations, TARGET_DATE)
    viz.route_pie_chart(reservations)

    print("\nDone!")


if __name__ == "__main__":
    main()