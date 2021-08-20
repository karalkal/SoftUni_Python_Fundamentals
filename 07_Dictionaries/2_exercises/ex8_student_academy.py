num_of_students = int(input())
dict_grades_separated = {}
for gr in range(num_of_students):
    student_name, grade = input(), input()
    if student_name not in dict_grades_separated.keys():
        dict_grades_separated[student_name] = grade
    else:
        dict_grades_separated[student_name] += " | " + grade
# print(dict_grades_separated)
dict_listed_grades = {}
for k, v in dict_grades_separated.items():
    dict_listed_grades[k] = [float(x) for x in v.split(" | ")]
# print(dict_listed_grades)
avg_good_grades = {k: sum(v) / len(v) for (k, v) in dict_listed_grades.items() if sum(v) / len(v) >= 4.5}
# print(avg_good_grades)
sorted_grades = dict(sorted(avg_good_grades.items(), key=lambda x: x[1], reverse=True))
# print(sorted_grades)
for k, v in sorted_grades.items():
    print(f"{k} -> {v:.2f}")
