list_numbers = [int(x) for x in input().split()]
command = input().split()
count = 0
while command[0] != "end":
    if command[0] == "exchange":
        command[1] = int(command[1])
        if 0 <= command[1] < len(list_numbers):
            list_numbers = list_numbers[int(command[1]) + 1:] + list_numbers[:int(command[1]) + 1]
        else:
            print("Invalid index")

    elif command[0] == "max":
        if command[1] == "even":
            for index_list in range(len(list_numbers)):
                if list_numbers[index_list] % 2 == 0:
                    number = list_numbers.index(max(list_numbers))
                    print(number)
                    break
            else:
                print("No matches")
        elif command[1] == "odd":
            for index_list in range(len(list_numbers)):
                if list_numbers[index_list] % 2 != 0:
                    number = int(list_numbers.index(max(list_numbers)))
                    count += 1
                    print(number)
                    break
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            for index_list in range(len(list_numbers) - 1, -1, -1):
                if list_numbers[index_list] % 2 == 0:
                    print(list_numbers.index(min(list_numbers)))
                    break
            else:
                print("No matches")

        elif command[1] == "odd":
            for index_list in range(len(list_numbers) -1, -1, -1):
                if list_numbers[index_list] % 2 != 0:
                    print(list_numbers.index(min(list_numbers)))
                    break
            else:
                print("No matches")


    elif command[0] == "first":
        if int(command[1]) > len(list_numbers):
            print("Invalid count")
        else:
            if command[2] == "even":
                list_even = []
                for index_list in range(int(command[1])):
                    if list_numbers[index_list] % 2 == 0:
                        list_even.append(list_numbers[index_list])
                print(list_even)
            elif command[2] == "odd":
                if int(command[1]) > len(list_numbers):
                    print("Invalid count")
                list_odd = []
                for index_list in range(int(command[1])):
                    if list_numbers[index_list] % 2 != 0:
                        list_odd.append(list_numbers[index_list])
                print(list_odd)
    elif command[0] == "last":
        if int(command[1]) > len(list_numbers):
            print("Invalid count")
        else:
            if command[2] == "even":
                list_even = []
                for index_list in range(int(command[1])):
                    if int(command[1]) > len(list_numbers):
                        print("Invalid count")
                    else:
                        if list_numbers[index_list] % 2 == 0:
                            list_even.append(list_numbers[index_list])
                print(list_even)
            elif command[2] == "odd":
                if int(command[1]) > len(list_numbers):
                    print("Invalid count")
                list_odd = []
                for index_list in range(int(command[1])):
                    if int(command[1]) > len(list_numbers):
                        print("Invalid count")
                    else:
                        if list_numbers[index_list] % 2 != 0:
                            list_odd.append(list_numbers[index_list])
                print(list_odd)
    command = input().split()

print(list_numbers)
NE E DOVYRSHENA








