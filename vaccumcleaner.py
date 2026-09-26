rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

current_room = "A"

print("Initial State:", rooms)
print("Vacuum is in Room", current_room)

while "Dirty" in rooms.values():

    if rooms[current_room] == "Dirty":
        print("Room", current_room, "is Dirty")
        print("Action: SUCK")
        rooms[current_room] = "Clean"

    else:
        print("Room", current_room, "is Clean")
        print("Action: MOVE")

        if current_room == "A":
            current_room = "B"
        else:
            current_room = "A"

print("Final State:", rooms)
print("Both rooms are Clean")