user_entry = input()
courses = {}
while user_entry != "end":
    user_entry = user_entry.split(" : ")
    course_name, student_name = user_entry
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name] += [student_name]

    user_entry = input()
# print(courses)
sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
# print(sorted_courses)
sorted_courses2 = {k: sorted(v) for (k, v) in sorted_courses.items()}
# print(sorted_courses2)

for k, v in sorted_courses2.items():
    print(k + ": " + f"{len(v)}")
    for student in range(0, len(v)):
        print("-- " + v[student])