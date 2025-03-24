import json

def f(years, course, average_grade):
    count = 0

    # Open and load the JSON data from the file
    with open("data.json", "r") as file:
        data = json.load(file)

    # Iterate over each student in the data
    for student in data:
        age = student['age']
        courses = student['studies']['courses']

        # If the student meets the age requirement
        if age >= years:
            # Search for the specified course
            for course_data in courses:
                if course_data['name'] == course:
                    # Calculate the average grade for the course
                    grades = course_data['grades']
                    avg_grade = sum(grades) / len(grades)

                    # Check if the student's average grade meets the requirement
                    if avg_grade >= average_grade:
                        count += 1
                    break  # No need to check further courses for this student

    return count

print(f(21, "statistics", 4) )