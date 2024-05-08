appointments = []

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Appointment Booking System")
    print("---------------------------------------")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Search Appointment")
    print("4. Update Appointment")
    print("5. Cancel Appointment")
    print("6. Quit")

def book_appointment():
    print("-------------------------")
    print("Book Appointment")
    print("-------------------------")
    appointment = {}
    appointment['appointment_id'] = input("Enter Appointment ID: ")
    appointment['patient_name'] = input("Enter Patient Name: ")
    appointment['doctor_name'] = input("Enter Doctor Name: ")
    appointment['date'] = input("Enter Date: ")
    appointment['time'] = input("Enter Time: ")
    appointments.append(appointment)
    print("Appointment booked successfully")

def view_appointments():
    print("--- Appointment Records ---")
    for appointment in appointments:
        print("Appointment ID:", appointment['appointment_id'])
        print("Patient Name:", appointment['patient_name'])
        print("Doctor Name:", appointment['doctor_name'])
        print("Date:", appointment['date'])
        print("Time:", appointment['time'])
        print("-------------------------")

def search_appointment():
    appointment_id = input("Enter Appointment ID to search: ")
    for appointment in appointments:
        if appointment['appointment_id'] == appointment_id:
            print("Appointment Found:")
            print("Appointment ID:", appointment['appointment_id'])
            print("Patient Name:", appointment['patient_name'])
            print("Doctor Name:", appointment['doctor_name'])
            print("Date:", appointment['date'])
            print("Time:", appointment['time'])
            return
    print("Appointment not found.")

def update_appointment():
    appointment_id = input("Enter Appointment ID to update: ")
    for appointment in appointments:
        if appointment['appointment_id'] == appointment_id:
            print("Update Appointment Information")
            appointment['patient_name'] = input("Enter Patient Name: ")
            appointment['doctor_name'] = input("Enter Doctor Name: ")
            appointment['date'] = input("Enter Date: ")
            appointment['time'] = input("Enter Time: ")
            print("Appointment updated successfully")
            return
    print("Appointment not found.")

def cancel_appointment():
    appointment_id = input("Enter Appointment ID to cancel: ")
    for appointment in appointments:
        if appointment['appointment_id'] == appointment_id:
            appointments.remove(appointment)
            print("Appointment cancelled successfully")
            return
    print("Appointment not found.")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        book_appointment()
    elif choice == '2':
        view_appointments()
    elif choice == '3':
        search_appointment()
    elif choice == '4':
        update_appointment()
    elif choice == '5':
        cancel_appointment()
    elif choice == '6':
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
