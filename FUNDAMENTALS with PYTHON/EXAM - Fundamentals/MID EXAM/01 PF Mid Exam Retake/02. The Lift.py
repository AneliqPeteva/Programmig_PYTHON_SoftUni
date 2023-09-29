people_waiting_for_lift = int(input())
current_state_of_the_lift = [int(x) for x in input().split()]
max_people_lift = 4

for wagon_lift in range(len(current_state_of_the_lift)):
    max_people = min(max_people_lift - current_state_of_the_lift[wagon_lift], people_waiting_for_lift)
    current_state_of_the_lift[wagon_lift] += max_people
    people_waiting_for_lift -= max_people

if people_waiting_for_lift > 0:
    print(f"There isn't enough space! {people_waiting_for_lift} people in a queue!")
elif any(wagon < max_people_lift for wagon in current_state_of_the_lift):
    print("The lift has empty spots!")

#print(*current_state_of_the_lift)

#for element in current_state_of_the_lift:
#    print(element, end=" ")

print(" ".join(str(element) for element in current_state_of_the_lift))

