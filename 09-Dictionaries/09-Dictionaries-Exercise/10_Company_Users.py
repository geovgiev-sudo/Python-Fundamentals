command = input()
users = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in users.keys():
        users[company_name] = []
    if employee_id not in users[company_name]:
        users[company_name].append(employee_id)

    command = input()

for name, company_ids in users.items():
    print(f"{name}")
    for company_id in company_ids:
        print(f"-- {company_id}")