students = {
    1:"pavan",
    2:"sai",
    3:"chandra",

    4:"sai",

    5:"pavan",
    6:"chandra",

    4:"kalyan",
}

print(f"type:{type(students)}")
print(students)

print(f"length:{len(students)}\n")

print(f"keys:{list(students.keys())}")
print(f"values:{list(students.values())}")
print(f"items:{list(students.items())}\n")

# contains
print(f"1 in students:{1 in students}")
print(f"10 in students:{10 in students}\n")

print(f"1:{students[1]}")