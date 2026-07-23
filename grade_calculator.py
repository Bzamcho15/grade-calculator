print("Hey guys, im making a grade calculator in python")


def forward_calculator(grade, exam_weight, exam_score):
    exam_weight = exam_weight / 100
    final_calculation = grade * (1 - exam_weight) + exam_score * exam_weight
    return final_calculation

def run_forward_calculator():
    grade = float(input("Enter your current grade: "))
    exam_weight = float(input("Enter exam weight (%): "))
    exam_score = float(input("Enter exam score: "))
   
    result = forward_calculator(grade, exam_weight, exam_score)
    print(f"Your final grade is: {round(result, 2)}%")

def backward_calculator(desired_grade, exam_weight, current_grade):
    exam_weight = exam_weight / 100
    required_exam_score = (desired_grade - current_grade * (1 - exam_weight)) / exam_weight
    return required_exam_score

def run_backward_calculator():
    desired_grade = float(input("What is your desired final grade? "))
    exam_weight = float(input("What is the weight of the exam as a percentage? "))
    current_grade = float(input("What is your current grade? "))

    required = backward_calculator(desired_grade, exam_weight, current_grade)
    print(f"You need to score: {round(required, 1)} on the exam to achieve your desired final grade.")
    if required > 100:
        print("Unfortunately, it is not possible to achieve your desired final grade with your current grade and the exam weight.")

def main():
    print("Welcome to the Grade Calculator!")
    print("Please choose an option: ")
    print("1. Calculate final grade based on current grade and exam score")
    print("2. Calculate what you need to score on the exam to achieve a desired final grade")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        run_forward_calculator()
    elif choice == "2":
        run_backward_calculator()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
