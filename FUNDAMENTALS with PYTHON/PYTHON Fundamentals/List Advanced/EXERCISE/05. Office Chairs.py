def ckeck_the_rooms(number_of_rooms):
    free_chairs = 0
    needed_chair = 0
    for current_room in range(1, counter_rooms + 1):
        information = input().split()
        counter_chairs = len(information[0])
        number_of_visitors = int(information[1])
        if counter_chairs < number_of_visitors:
            needed_chairs_in_room = number_of_visitors - counter_chairs
            print(f"{needed_chairs_in_room} more chairs needed in room {current_room}")
            needed_chair += needed_chairs_in_room
        else:
            free_chairs += counter_chairs - number_of_visitors
    return free_chairs, needed_chair

counter_rooms = int(input())
total_free_chairs, total_needed_chairs = ckeck_the_rooms(counter_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

