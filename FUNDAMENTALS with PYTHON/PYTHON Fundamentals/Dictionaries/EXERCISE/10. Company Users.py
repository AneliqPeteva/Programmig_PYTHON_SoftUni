companies = {}
command = input()
while command != "End":
    company_name, employees_id = command.split(" -> ")
    if company_name not in companies.keys():
        companies[company_name] = []
    if employees_id not in companies[company_name]:
        companies[company_name].append(employees_id)
    command = input()
for company_name, employees in companies.items():
    print(f"{company_name}")
    for employee in employees:
        print(f"-- {employee}")
