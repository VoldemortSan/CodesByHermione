class ScheduleSystem:
    def __init__(self):
        self.airline_schedule = []
        self.cargo_schedule = []

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to Airline and Cargo Schedule System")
        print("---------------------------------------")
        print("1. Add Airline Schedule")
        print("2. View Airline Schedules")
        print("3. Add Cargo Schedule")
        print("4. View Cargo Schedules")
        print("5. Quit")

    def add_airline_schedule(self):
        print("-------------------------")
        print("Add New Airline Schedule")
        print("-------------------------")
        flight_number = input("Enter Flight Number: ")
        departure = input("Enter Departure Location: ")
        destination = input("Enter Destination Location: ")
        departure_time = input("Enter Departure Time: ")
        arrival_time = input("Enter Arrival Time: ")
        self.airline_schedule.append({
            'Flight Number': flight_number,
            'Departure': departure,
            'Destination': destination,
            'Departure Time': departure_time,
            'Arrival Time': arrival_time
        })
        print("Airline schedule added successfully")

    def view_airline_schedules(self):
        print("--- Airline Schedules ---")
        for schedule in self.airline_schedule:
            print("Flight Number:", schedule['Flight Number'])
            print("Departure:", schedule['Departure'])
            print("Destination:", schedule['Destination'])
            print("Departure Time:", schedule['Departure Time'])
            print("Arrival Time:", schedule['Arrival Time'])
            print("-------------------------")

    def add_cargo_schedule(self):
        print("-------------------------")
        print("Add New Cargo Schedule")
        print("-------------------------")
        shipment_id = input("Enter Shipment ID: ")
        origin = input("Enter Origin Location: ")
        destination = input("Enter Destination Location: ")
        departure_time = input("Enter Departure Time: ")
        arrival_time = input("Enter Arrival Time: ")
        self.cargo_schedule.append({
            'Shipment ID': shipment_id,
            'Origin': origin,
            'Destination': destination,
            'Departure Time': departure_time,
            'Arrival Time': arrival_time
        })
        print("Cargo schedule added successfully")

    def view_cargo_schedules(self):
        print("--- Cargo Schedules ---")
        for schedule in self.cargo_schedule:
            print("Shipment ID:", schedule['Shipment ID'])
            print("Origin:", schedule['Origin'])
            print("Destination:", schedule['Destination'])
            print("Departure Time:", schedule['Departure Time'])
            print("Arrival Time:", schedule['Arrival Time'])
            print("-------------------------")


schedule_system = ScheduleSystem()

while True:
    schedule_system.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        schedule_system.add_airline_schedule()
    elif choice == '2':
        schedule_system.view_airline_schedules()
    elif choice == '3':
        schedule_system.add_cargo_schedule()
    elif choice == '4':
        schedule_system.view_cargo_schedules()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
