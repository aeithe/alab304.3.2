my_string = "You learn more from failure than from success."

new_string = my_string[0] + my_string[3] + my_string[-1]

print(new_string)

print(new_string.replace(".", "!"))

new_str= "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"
lower_str = new_str.lower()
print(lower_str)

new_str = new_str.upper();
print(new_str)


new_str= "There are no traffic jams along the extra mile."
print(new_str.startswith("Z"))
print(new_str.startswith("t"))


print(new_str.index("j"))


a = new_str.count("t")
b = new_str.count("o")
print("The letter 't' appears {} times and the letter 'o' appears {} times.".format(a,b))

print(f"The letter 't' appears {a} times and the letter 'o' appears {b} times.")