lloyd = {'name': 'Lloyd','homework': [90.0,97.0,75.0,92.0],'quizzes': [88.0,40.0,94.0],'tests': [75.0,90.0]}
alice = {'name': 'Alice','homework': [100.0, 92.0, 98.0, 100.0],'quizzes': [82.0, 83.0, 91.0],'tests': [89.0, 97.0]}
tyler = {'name': 'Tyler','homework': [0.0, 87.0, 75.0, 22.0],'quizzes': [0.0, 75.0, 78.0],'tests': [100.0, 100.0]}
students = [ lloyd, alice, tyler]

for i in students:
    print(f"Student's name: {i['name']}")
    print(f"Student's homework marks: {i['homework']}")
    print(f"Student's quizzes marks: {i['quizzes']}")
    print(f"Student's test's marks: {i['tests']}")
    print('')

def average(numbers):
    total = float(sum(numbers))/len(numbers)
    return total

def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    score = tests*0.60 + quizzes*0.30 + homework*0.10
    return score

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


print("Lloyd's grade :", end= " ")
print(get_letter_grade(get_average(lloyd)))

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)    

print("Class average: ", get_class_average(students))
print("Class average graade: ", get_letter_grade(get_class_average(students)))
