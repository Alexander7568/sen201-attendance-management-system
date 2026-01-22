# Attendance Management System

attendance = []

while True:
    print("\n--- Attendance Menu ---")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        status = input("Enter status (Present/Absent): ")
        attendance.append((student_name, status))
        print("Attendance recorded successfully.")

    elif choice == "2":
        if not attendance:
            print("No attendance records found.")
        else:
            print("\nAttendance Records:")
            for record in attendance:
                print("Student:", record[0], "- Status:", record[1])

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
