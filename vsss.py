# Define the employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

# Function to sort and print employee data based on the chosen parameter
def sort_and_print_data(parameter):
    sorted_data = sorted(employee_data, key=lambda x: x[parameter])
    print("\nSorted Employee Data by", parameter)
    print("-" * 40)
    for employee in sorted_data:
        print(f"Employee ID: {employee['Employee ID']}")
        print(f"Name: {employee['Name']}")
        print(f"Age: {employee['Age']}")
        print(f"Salary (PM): {employee['Salary (PM)']}")
        print("-" * 40)

# Main program
while True:
    print("\nChoose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        sort_and_print_data('Age')
    elif choice == '2':
        sort_and_print_data('Name')
    elif choice == '3':
        sort_and_print_data('Salary (PM)')
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
