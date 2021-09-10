from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_attendances = 0
max_bonus = 0

for student in range(1, students_count + 1):
    attendances = int(input())

    total_bonus = attendances / lectures_count * (5 + additional_bonus)
    if attendances > max_attendances:
        max_attendances = attendances
        max_bonus = total_bonus
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
