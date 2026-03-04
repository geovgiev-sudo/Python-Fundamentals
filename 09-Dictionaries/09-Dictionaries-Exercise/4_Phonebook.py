command = input()
phonebook = {}
while "-" in command:
    info = command.split("-")
    name = info[0]
    number = info[1]
    if name not in phonebook.keys():
        phonebook[name] = number
    phonebook[name] = number
    command = input()

n = int(command)

for i in range(n):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")


# phonebook = {}
# while True:
#     entry = input()
#     if "-" not in entry:
#         break
#     name, number = entry.split("-")
#     phonebook[name] = number
# number_of_searches = int(entry)
#
# for search in range(number_of_searches):
#     searched_name = input()
#     if searched_name in phonebook.keys():
#         number = phonebook[searched_name]
#         print(f"{searched_name} -> {number}")
#     else:
#         print(f"Contact {searched_name} does not exist.")