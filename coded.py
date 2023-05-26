text = "these are not the droids we are looking for"

a_z = " abcdefghijklmnopqrstuvwxyz"
vow = "aeiou"

output = ""
for letter in text:
    count_of_vow = a_z.find(letter)
    line = ("a" * count_of_vow) + "ncysgqwycxmzpsfhryvbgtnncbbztzzqmwsfqwrtypsdfghklmnbvcxz"
    output += line + "\n"

print(output)