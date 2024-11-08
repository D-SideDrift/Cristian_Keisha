import pandas as pd

# Step 1: Input for Assignment details
assignment_name = input("Enter the assignment name: ")
days_left = int(input("Enter the number of days before the assignment is due: "))

# Step 2: Store values in variables
Assignment_1 = assignment_name
Upcoming_Deadline_1 = days_left

# Print stored values
print(f"Assignment: {Assignment_1}, Deadline in: {Upcoming_Deadline_1} days")

# Step 3: Input for completion status
Amount_Completed = int(input("Enter completion status (1-5): "))

# Step 4: Check completion status and print corresponding message
if Amount_Completed == 1:
    print(f"You have {Upcoming_Deadline_1} days to complete the whole assignment.")
elif Amount_Completed == 2:
    print(f"You have {Upcoming_Deadline_1} days to complete most of the assignment.")
elif Amount_Completed == 3:
    print(f"You have {Upcoming_Deadline_1} days to complete the other half of the assignment.")
elif Amount_Completed == 4:
    print(f"You have {Upcoming_Deadline_1} days to complete the rest of the assignment.")
elif Amount_Completed == 5:
    print(f"You have completed the whole assignment.")
else:
    print("Sorry, I don't understand.")

# Step 5: Create a DataFrame (table) with the assignment details
data = {
    'Assignment': [Assignment_1],
    'Upcoming Deadline (Days)': [Upcoming_Deadline_1],
    'Amount Completed': [Amount_Completed]
}

df = pd.DataFrame(data)

# Step 6: Sort the DataFrame by 'Upcoming Deadline (Days)'
df_sorted = df.sort_values(by='Upcoming Deadline (Days)', ascending=True)

# Step 7: Alert if the assignment is due in less than 7 days
if Upcoming_Deadline_1 < 7:
    print(f"ALERT: The assignment '{Assignment_1}' is due in less than 7 days!")

# Display sorted DataFrame
print("\nSorted Assignment DataFrame:")
print(df_sorted)
