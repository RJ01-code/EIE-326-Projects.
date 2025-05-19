
# GPA scale based on letter grades
grade_points = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'F': 0
}

def compute_gpa():
    total_weighted_points = 0
    total_credit_units = 0

    print("Enter grade and credit unit for each of the 6 courses.")

    for i in range(1, 7):
        while True:
            grade = input(f"Course {i} grade (A, B, C, D, F): ").upper()
            if grade in grade_points:
                break
            else:
                print("Invalid grade. Please enter A, B, C, D, or F.")

        while True:
            try:
                credit = int(input(f"Course {i} credit unit: "))
                if credit > 0:
                    break
                else:
                    print("Credit unit must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        total_weighted_points += grade_points[grade] * credit
        total_credit_units += credit

    gpa = total_weighted_points / total_credit_units
    print(f"\nYour GPA is: {gpa:.2f} (on a 5.0 scale)")

if __name__ == "__main__":
    compute_gpa()
