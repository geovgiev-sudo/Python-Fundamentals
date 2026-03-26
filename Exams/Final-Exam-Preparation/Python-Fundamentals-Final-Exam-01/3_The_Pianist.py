n = int(input())
pieces = {}
for i in range(n):
    oeuvre, kompozitor, tonalnost = input().split("|")
    pieces[oeuvre] = [kompozitor, tonalnost]

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    action = command[0]
    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in pieces.items():
    composer = info[0]
    key = info[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
