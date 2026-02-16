# animals = list(input().split(", "))
#
# if animals[-1] == "wolf":
#     print("Please go away and stop eating my sheep")
# else:
#     if "wolf" in animals:
#         animals.reverse()
#         for index, value in enumerate(animals):
#             if value == "wolf":
#                 print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")


list_words = input().split(", ")
word_to_be_find = "wolf"

if list_words[-1] == word_to_be_find:
    print(f"Please go away and stop eating my sheep")
else:
    wolf_index = list_words.index(word_to_be_find)
    sheep_to_be_eaten = len(list_words) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_to_be_eaten}! You are about to be eaten by a wolf!")


#
#
# words = input().split(", ")
# sheep_count = 0
#
# for animal in reversed(words):
#     if animal == "wolf":
#         if sheep_count == 0:
#             print("Please go away and stop eating my sheep")
#         else:
#             print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
#         break
#     elif animal == "sheep":
#         sheep_count += 1
#
#
#

# sheep_or_wolf = input().split(", ")
# my_list = sheep_or_wolf[::-1]
# for idx, word in enumerate(my_list):
#     if word == "wolf" and idx == 0:
#         print("Please go away and stop eating my sheep")
#         break
#     elif word == "wolf":
#         print(f"Oi! Sheep number {idx}! You are about to be eaten by a wolf!")



# animals = input().split(", ")
# wolf_index = animals.index("wolf")
#
# if wolf_index == len(animals) - 1:
#     print("Please go away and stop eating my sheep")
# else:
#     sheep_number = len(animals) - wolf_index -1
#     print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")

#
#




