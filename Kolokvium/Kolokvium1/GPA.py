grade_to_points = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

grades_input = input("Enter your grades like (e.g. A B C): ")
grades_list = grades_input.split()

points = []
for g in grades_list:
    if g in grade_to_points:
        points.append(grade_to_points[g])
    else:
        print(f"Invalid grade '{g}' will be ignored.")
if not points:
    print("No valid grades entered.")
else:
    gpa = sum(points) / len(points)
    
    if gpa >= 3.5:
        rating = "Excellent"
    elif gpa >= 2.5:
        rating = "Good"
    elif gpa >= 2.0:
        rating = "Average"
    else:
        rating = "Needs Improvement"
    
    print(f"Your GPA is {gpa:.2f}. Rating: {rating}")

