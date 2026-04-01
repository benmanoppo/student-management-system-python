# %%
# initial empty student list

students = []

# start the main loop for the menu
while True:
    print("\n--- Choose Command ---")
    print("1. Add Student") # add student's name and grade
    print("2. View Students' Details") # view student's name and grade
    print("3. Update Student's Grade") # Update student grade
    print("4. Delete Student") # Delete student
    print("5. Exit") # Exit
    
    choice = input("Enter your choice (1-5): ") # beginning of the prompt

    # adding student's name and grade (Choice no. 1)
    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter student grade (0-100): "))
        students.append([name, grade])
        print("Student added successfully.")

    # create prompt to show list of students (Choice no. 2)
    elif choice == "2":
        if len(students) == 0:
            print("No students in the system.")
        else:
            print("\nStudent List:")
            for student in students:
                name = student[0]
                grade = student[1]
                # entering grade's criteria
                if grade >= 85:
                    category = "HD (High Distinction)"
                elif grade >= 75:
                    category = "D (Distinction)"
                elif grade >= 65:
                    category = "C (Credit)"
                elif grade >= 50:
                    category = "P (Pass)"
                else:
                    category = "F (Fail)"

                print("Name:", name, "| Grade:", grade, "| Category:", category)

    # create prompt to update student's grade (Choice no. 3)
    elif choice == "3":
        update_name = input("Enter the student name to update grade: ") #insert student's name whose grade changed
        found = False
        for student in students:
            if student[0] == update_name:
                new_grade = int(input("Enter new grade: ")) #enter new grade
                student[1] = new_grade
                print("Grade updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    # create prompt to delete student's status (Choice no. 4)
    elif choice == "4":
        delete_name = input("Enter the student name to delete: ") #insert student's name to be deleted
        found = False
        for student in students:
            if student[0] == delete_name:
                students.remove(student)
                print("Student deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    # create prompt exiting activity (Choice no. 5)
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    # exit prompt
    else:
        print("Invalid choice. Please select from 1 to 5.")