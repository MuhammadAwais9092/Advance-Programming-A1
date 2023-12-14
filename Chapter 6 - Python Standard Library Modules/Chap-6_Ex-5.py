# Chapter 6 Exercise 5: Working with JSON File

# Importing json library
import json

# Defining function to write into json file
def writing_into_json(filename, data):
    # Opening the JSON file in write mode and use json.dump to write data to the file
    with open(filename, 'w') as file:
        json.dump(data, file)

# Defining function to read from the json file
def reading_from_json(filename):
    # Opening the JSON file in read mode and use json.load to read data from the file
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def main():
    # Creating Task 1 which was to Write to JSON file
    student_data = {}
    # Get input from the user for student name, ID, and course
    student_data['Name'] = input("Enter the student name: ")
    student_data['ID'] = int(input("Enter the student ID: "))
    student_data['Course'] = input("Enter the student course: ")

    # Appending CourseDetails dictionary to student_data
    student_data['CourseDetails'] = {
        'Group': input("Enter the student group: "),
        'Year': int(input("Enter the student year: "))
    }

    # Calling the write_into_json function to write data to the JSON file
    writing_into_json('StudentJson.json', student_data)
    print("Details of the student are written to StudentJson.json")

    # Creating Task 2 which is to Read from JSON file
    # Call the reading_from_json function to read data from the JSON file
    retrieved_data = reading_from_json('StudentJson.json')

    print("\nDetails of the Student are")
    print(f"  Name: {retrieved_data['Name']}")
    print(f"  ID: {retrieved_data['ID']}")
    print(f"  Course: {retrieved_data['Course']}")

    # Displaying the CourseDetails
    print("  CourseDetails:")
    print(f"    Group: {retrieved_data['CourseDetails']['Group']}")
    print(f"    Year: {retrieved_data['CourseDetails']['Year']}")

# Ending the code
if __name__ == "__main__":
    main()
