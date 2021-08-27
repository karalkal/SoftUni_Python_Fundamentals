how_many = int(input())
for _ in range(how_many):
    text_to_decode = input()

    name_starts_at = text_to_decode.index("@") + 1
    name_ends_at = text_to_decode.index("|")
    age_starts_at = text_to_decode.index("#") + 1
    age_ends_at = text_to_decode.index("*")
    name = text_to_decode[name_starts_at:name_ends_at]
    age = text_to_decode[age_starts_at:age_ends_at]

    print(f"{name} is {age} years old.")