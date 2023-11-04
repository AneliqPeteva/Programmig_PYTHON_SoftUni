force_book = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for value in force_book.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for user in users:
            print(f"! {user}")
