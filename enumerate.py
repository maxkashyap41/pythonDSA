list1 = ["eat", "sleep", "code", "repeat"]
string = "Onu Miyaan"

objct = enumerate(list1)

print("Return Type: ", type(objct))
print (list(enumerate(list1)))
print(list(enumerate(string)))

print("\n#######################################################################################################\n")

for val in enumerate(list1):
    print(val)

print("\n#######################################################################################################\n")

for i, val in enumerate(list1):
    print(i, val)