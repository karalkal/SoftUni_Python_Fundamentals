original = [int(x) for x in input().split(", ")]
a_s = [x for x in original if 0 < x <= 10]
b_s = [x for x in original if 10 < x <= 20]
c_s = [x for x in original if 20 < x <= 30]
d_s = [x for x in original if 30 < x <= 40]
e_s = [x for x in original if 40 < x <= 50]

print(a_s)
print(b_s)
print(c_s)
print(d_s)
print(e_s)
