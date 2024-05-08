class StudentDatabase:
    def __init__(self):
        self.students = []

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to Student Database System")
        print("---------------------------------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Quit")

    def add_student(self):
        print("-------------------------")
        print("Add New Student")
        print("-------------------------")
        student = {}
        student['student_id'] = input("Enter Student ID: ")
        student['name'] = input("Enter Name: ")
        student['age'] = input("Enter Age: ")
        student['grade'] = input("Enter Grade: ")
        self.students.append(student)
        print("Student added successfully")

    def view_students(self):
        print("--- Student Records ---")
        for student in self.students:
            print("Student ID:", student['student_id'])
            print("Name:", student['name'])
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            print("-------------------------")

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student['student_id'] == student_id:
                print("Student Found:")
                print("Student ID:", student['student_id'])
                print("Name:", student['name'])
                print("Age:", student['age'])
                print("Grade:", student['grade'])
                return
        print("Student not found.")

    def update_student_information(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student['student_id'] == student_id:
                print("Update Student Information")
                student['name'] = input("Enter Name: ")
                student['age'] = input("Enter Age: ")
                student['grade'] = input("Enter Grade: ")
                print("Student information updated successfully")
                return
        print("Student not found.")

# Create an instance of the StudentDatabase
student_database = StudentDatabase()

# Main loop for menu selection
while True:
    student_database.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        student_database.add_student()
    elif choice == '2':
        student_database.view_students()
    elif choice == '3':
        student_database.search_student()
    elif choice == '4':
        student_database.update_student_information()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
