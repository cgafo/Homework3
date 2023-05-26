import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
b = r.text
a_z = " abcdefghijklmnopqrstuvwxyz"
vow = "aeiou"
secret_message = ""
for line in b.splitlines():
    count_of_vow = 0
    for letter in line:
        if letter in vow:
            count_of_vow += 1
    secret_message += a_z[count_of_vow]

print(f"The message that is hidden in this text is: {secret_message}")


