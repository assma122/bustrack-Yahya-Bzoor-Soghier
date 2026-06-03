
import matplotlib.pyplot as plt


class Visualizer:

    def occupancy_chart(self, routes: list, reservations: list, date: str):
        route_ids = []
        booked = []
        available = []

        for route in routes:
            route_id = route["route_id"]
            route_ids.append(route_id)

            booked_count = 0
            for reservation in reservations:
                if reservation["route_id"] == route_id and reservation["date"] == date:
                    booked_count += 1

            booked.append(booked_count)
            available.append(route["capacity"] - booked_count)

        x = range(len(route_ids))
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar([i - width / 2 for i in x], booked, width, label="Booked", color="tomato")
        ax.bar([i + width / 2 for i in x], available, width, label="Available", color="steelblue")

        ax.set_title(f"Bus Occupancy — {date}", fontsize=14, fontweight='bold')
        ax.set_xlabel("Route ID", fontsize=12)
        ax.set_ylabel("Number of Seats", fontsize=12)
        ax.set_xticks(list(x))
        ax.set_xticklabels(route_ids)
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.show()

    def route_pie_chart(self, reservations: list):
        counts = {}

        for reservation in reservations:
            route_id = reservation["route_id"]
            counts[route_id] = counts.get(route_id, 0) + 1

        fig, ax = plt.subplots(figsize=(7, 7))

        ax.pie(
            counts.values(),
            labels=counts.keys(),
            autopct="%1.1f%%",
            startangle=140,
            colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
        )

        ax.set_title("Reservations by Route", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()