student = {}

student["jmeno"] = input("Zadej jmeno studenta: ")
student["vek"] = int(input("Zadej vek studenta: "))
student["znamky"] = [
    int(input("Zadej prvni znamku: ")),
    int(input("Zadej druhou znamku: ")),
    int(input("Zadej treti znamku: ")),
]

prumer = sum(student["znamky"]) / len(student["znamky"])

if prumer < 2:
    print("Vyborny student.")
elif prumer < 4:
    print("Prumerny student.")
else:
    print("Spatny student.")

print(student)