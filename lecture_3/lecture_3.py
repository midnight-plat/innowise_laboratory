import math
import typing

from typing import List, Dict, Union, Any, Optional

# Global collection for students' data
#  [{"name": "Alice", "grades": [95, 88]}, ...]
students: List[Dict[str, Union[str, List[int]]]] = []

# Main menu
def display_menu():

    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")



def get_average_grade(grades: List[int]) -> Union[float, str]:

    if not grades:
        return "N/A"
    try:
        return round(sum(grades) / len(grades), 1)
    except ZeroDivisionError:
        return "N/A"


def add_new_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("this field cannot be empty")
        return

    # Checking the existing of students
    if any(s['name'].lower() == name.lower() for s in students):
        print(f" Student '{name}' already exist")
        return

    # Adding new dict for student
    new_student = {"name": name, "grades": []}
    students.append(new_student)
    print(f" Student '{name}' added")


def add_grades_for_student():
    #Option 2  - add grades for students
    name_to_find = input("Enter student name: ").strip()

    found_student: Optional[Dict[str, Any]] = next(
        (s for s in students if s['name'].lower() == name_to_find.lower()),
        None
    )

    if found_student is None:
        print(f" Student '{name_to_find}' not found")
        return

    print(f"Adding grades for {found_student['name']}. Enter 'done' to finish")
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == 'done':
            break

        if not grade_input:
            continue

        try:
            grade = int(grade_input)

            # checking grades input
            if 0 <= grade <= 100:
                found_student['grades'].append(grade)
                print(f"Grade {grade} added")
            else:
                print("Invalid input. Grade must be between 0 and 100")

        except ValueError:
            # Print an error for exceptions
            print(" Invalid input. Please enter a valid integer number or 'done'")


def show_report():
    #Option 3
    if not students:
        print("No students added")
        return

    print("\n--- Report ---")

    all_averages: List[float] = []

    for student in students:
        grades = student['grades']

        # Call def for average grade
        average = get_average_grade(grades)

        print(f"{student['name']}'s average grade is {average}.")

        if isinstance(average, float) or isinstance(average, int):
            all_averages.append(average)

    print("-" * 33)

    # summary
    if not all_averages:
        print(" No grades added to any student")
    else:
        max_avg = max(all_averages)
        min_avg = min(all_averages)
        overall_avg = round(sum(all_averages) / len(all_averages), 1)

        print(f"Max Average: {max_avg}")
        print(f"Min Average: {min_avg}")
        print(f"Overall Average: {overall_avg}")
    print("-" * 30)


def find_top_performer():
    # option 4
    if not students:
        print("No students added ")
        return

    students_with_grades = [s for s in students if s['grades']]

    if not students_with_grades:
        print("No student has any grades recorded")
        return


    # Lambda-function gets dict (s) and return average grade of student
    top_student = max(
        students_with_grades,
        key=lambda s: get_average_grade(s['grades'])
    )

    top_grade = get_average_grade(top_student['grades'])

    print(f"The student with the highest average is {top_student['name']} with a grade of {top_grade}")


def main():
    while True:
        display_menu()

        try:
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                add_new_student()
            elif choice == '2':
                add_grades_for_student()
            elif choice == '3':
                show_report()
            elif choice == '4':
                find_top_performer()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5")

        except Exception as e:
            # Common block for main loop
            print(f"Unexpected error: {e}. Try again.")


# Point of starting program
if __name__ == "__main__":
    main()