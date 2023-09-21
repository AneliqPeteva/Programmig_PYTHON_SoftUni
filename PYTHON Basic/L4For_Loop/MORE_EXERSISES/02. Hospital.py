# Read user input
n = int(input())
count_doctors = 7
treated_patients = 0
untreated_patients = 0
# Logic
for i in range(1, n + 1):
    count_patients = int(input())
    if i % 3 == 0:
        if treated_patients < untreated_patients:
            count_doctors += 1
    if count_doctors >= count_patients:
        treated_patients += count_patients
    else:
        untreated_patients += count_patients - count_doctors
        treated_patients += count_doctors
# Print output
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")