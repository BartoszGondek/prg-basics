###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14 and points < 18:
        grade = 'Good'
    elif points >=10 and points < 14:
        grade = 'Satisfactory'
    elif points < 10:    
        grade = 'Fail'
    return grade

test_result = int(input('Enter your test result in points: '))
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')