import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv("physics.csv")

# Define a helper function to find the student with the highest attendance in a given DataFrame
def find_highest_attendance(data):
    # Locate the row with the maximum value in the last column (attendance)
    highest_attendance_row = data.loc[data.iloc[:, -1].idxmax()]
    return highest_attendance_row

# Section 1: Find the student with the highest attendance in the first five rows
first_five_students = df.head(5)  # Get the first five rows
highest_first_five = find_highest_attendance(first_five_students)
print("Highest attendance student in the first five rows:")
print(highest_first_five)

# Section 2: Find the student with the highest attendance in the last five rows
last_five_students = df.tail(5)  # Get the last five rows
highest_last_five = find_highest_attendance(last_five_students)
print("\nHighest attendance student in the last five rows:")
print(highest_last_five)

# Section 3: Find the student with the highest attendance between rows 10 and 20
rows_10_to_20_students = df.iloc[9:20]  # Slice the DataFrame to get rows 10 to 20 (indices 9 to 19)
highest_rows_10_to_20 = find_highest_attendance(rows_10_to_20_students)
print("\nHighest attendance student between rows 10 and 20:")
print(highest_rows_10_to_20)

# Section 4: Find the student with the highest attendance overall in the entire class
highest_overall = find_highest_attendance(df)
print("\nStudent with the highest attendance overall:")
print(highest_overall)

# Plotting: Create a bar chart to visualize the attendance of all students
plt.figure(figsize=(12, 6))  # Set the figure size

# Extract student names and attendance values for the entire class
student_names = df.iloc[:, 0]  # Assuming student names are in the first column
attendance_values = df.iloc[:, -1]  # Assuming attendance is in the last column

# Create a bar plot for student attendance
plt.bar(student_names, attendance_values, color='skyblue')

# Add labels and title to the plot
plt.xlabel("Students")
plt.ylabel("Attendance")
plt.title("Student Attendance in Physics Class")

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()
