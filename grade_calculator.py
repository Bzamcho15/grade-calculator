print("Hey guys, im making a grade calculator in python")


def forward_calculator():
    grade = float(input("What is your grade? "))
    exam_weight = float(input("What is the weight of the exam as a percentage? "))
    exam_weight = exam_weight / 100  # Convert percentage to decimal
    exam_score = float(input("What is your exam score? "))

    final_calculation = grade * (1 - exam_weight) + exam_score * exam_weight
    print(f"Your final grade is: {round(final_calculation, 1)}")

def backward_calculator():
    desired_grade = float(input("What is your desired final grade? "))
    exam_weight = float(input("What is the weight of the exam as a percentage? "))
    exam_weight = exam_weight / 100 # Convert percentage to decimal
    current_grade = float(input("What is your current grade? "))
    required_exam_score = (desired_grade - current_grade * (1 - exam_weight)) / exam_weight
    print(f"You need to score: {round(required_exam_score, 1)} on the exam to achieve your desired final grade.")
    if required_exam_score > 100:
        print("Unfortunately, it is not possible to achieve your desired final grade with your current grade and the exam weight.")

def main():
    print("Welcome to the Grade Calculator!")
    print("Please choose an option: ")
    print("1. Calculate final grade based on current grade and exam score")
    print("2. Calculate what you need to score on the exam to achieve a desired final grade")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        forward_calculator()
    elif choice == "2":
        backward_calculator()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()