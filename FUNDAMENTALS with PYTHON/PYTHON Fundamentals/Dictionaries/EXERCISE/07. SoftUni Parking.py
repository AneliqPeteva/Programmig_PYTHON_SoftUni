number = int(input())
parking = {}
for current_command in range(number):
    command = input().split()
    if command[0] == "register":
        username, license_plate_number = command[1], command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for name, reg in parking.items():
    print(f"{name} => {reg}")
