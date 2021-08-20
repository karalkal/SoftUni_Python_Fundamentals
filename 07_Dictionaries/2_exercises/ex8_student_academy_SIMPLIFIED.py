num_of_students = int(input())
all_marks = {}
for gr in range(num_of_students):
    student_name, grade = input(), float(input())
    if student_name not in all_marks.keys():
        all_marks[student_name] = [grade]
    else:
        all_marks[student_name] += [grade]

# print(all_marks)
average_all = {k: sum(v) / len(v) for (k, v) in all_marks.items() if sum(v) / len(v) >= 4.5}
# print(average_all)
sorted_average = dict(sorted(average_all.items(), key=lambda x: x[1], reverse=True))
# print(sorted_average)
for k, v in sorted_average.items():
    print(k, " -> ", f"{v:.2f}", sep="")