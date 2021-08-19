courses_with_students = {}
user_input = input()
while ":" in user_input:
    user_input = [x for x in user_input.split(":")]
    for i in range(0, len(user_input) // 3):
        name, stud_id, course = user_input[0], user_input[1], "_".join((user_input[2]).split(" "))
        if course in courses_with_students:
            courses_with_students[course] += f"\n{name} - {stud_id}"
        else:
            courses_with_students[course] = f"{name} - {stud_id}"
    user_input = input()

check_for = user_input
# print(*courses_with_students.values(), sep="\n")
# print(courses_with_students)
result = {x: y for (x, y) in courses_with_students.items() if x == check_for}
print(*result.values(), sep="\n")
