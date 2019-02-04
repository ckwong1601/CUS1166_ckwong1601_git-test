print("Python Playground")

# basic print statements
print("\nPlaying around with print statements.")

#password = input("Please give me your password: ")
#print(f"{password} has been transferred to a secure database.")

a = 20.098
b = "red"
c = False
print(f"Variable a = {a} and is a(n) {type(a)}. Types do not have to be declared.")
a = None
print(f"I changed variable a = {a} to the type {type(a)}.")
print(f"This statement can be used with a variable b = {b}.")
print(f"type(variable) returns the variable type. That statement is {not c}.")

# built-in classes
print("\n-\nSandbox of python classes.")

#lists
l = [x*x for x in range(10,20) if x % 2 == 0] # use l[start:stop:step] to get a sublist
print(f"Lists store data such as {l[2]}. They can be any type such as {type(l[2])}.")
fancy_list = [l, ["Snek", 3.141596, False, None]]
print("It's quite easy to print out lists %s!" % fancy_list)
print(f"Let's be fancier: {fancy_list[1][0::2]}.")

# tuples
tuple_example = (5, "twenty", 9.66667)
print("Tuples are immutable. They can have %s or %s items, but not %s." % tuple_example)

# dictionaries
dictionary_example = dict()
if not dictionary_example:
    print("Dictionaries are like maps, but this one is empty.")
dictionary_example = {
    "New York" : 90,
    "Chicago" : 60,
    "Mountain View" : 30
}
print("The ping to Chicago is %s." % dictionary_example["Chicago"])

# sets
set_example = set()
set_example.add(3)
set_example.add(3)
set_example.add(20)
set_example.add(5)
set_example.remove(20)
print(f"Sets are unordered and have no identical elements. This one has {len(set_example)} elements.")

print(f"\n-\nNow to fancier things.")

# conditionals
happy = "This is a happy sentence."
if len(happy) > 10:
    print(happy)
elif len(happy) < 5:
    print("This is a sad sentence.")
else:
    print("This sentence is feeling ok.")

#loops
for i in range(3):
    print(l[i])
for key_val, map_val in enumerate(l):
    print(f"{key_val} - {map_val}")

# test function
def is_empty(list_to_check):
    if len(list_to_check) is 0:
        return True
    else:
        return False

print(is_empty(l))


