name_movies = input()
total_counter_ticket_student = 0
total_counter_ticket_standard = 0
total_counter_ticket_kid = 0

while name_movies != "Finish":
    free_places = int(input())
    type_ticket = input()
    counter_ticket_student = 0
    counter_ticket_standard = 0
    counter_ticket_kid = 0
    while type_ticket != "End":
        if type_ticket == "student":
            counter_ticket_student += 1
        elif type_ticket == "standard":
            counter_ticket_standard += 1
        elif type_ticket == "kid":
            counter_ticket_kid += 1

        current_count_ticket = counter_ticket_student + counter_ticket_kid + counter_ticket_standard
        percent_current_ticket = current_count_ticket / free_places * 100
        if current_count_ticket == free_places:
            break
        type_ticket = input()

    total_counter_ticket_student += counter_ticket_student
    total_counter_ticket_standard += counter_ticket_standard
    total_counter_ticket_kid += counter_ticket_kid
    print(f"{name_movies} - {percent_current_ticket:.2f}% full.")

    name_movies = input()


all_ticket = total_counter_ticket_standard + total_counter_ticket_student + total_counter_ticket_kid
percent_ticket_student = total_counter_ticket_student / all_ticket * 100
percent_ticket_standard = total_counter_ticket_standard / all_ticket * 100
percent_ticket_kid = total_counter_ticket_kid / all_ticket * 100

if name_movies == "Finish":
    print(f"Total tickets: {all_ticket}")
    print(f"{percent_ticket_student:.2f}% student tickets.")
    print(f"{percent_ticket_standard:.2f}% standard tickets.")
    print(f"{percent_ticket_kid:.2f}% kids tickets.")
