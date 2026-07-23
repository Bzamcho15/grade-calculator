import json
import tkinter as tk

from grade_calculator import forward_calculator, backward_calculator

def load_last_calculation():
    try:
        with open("last_calculation.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_entries():
    data = {
        "current_grade": current_grade_entry.get(),
        "exam_weight": exam_weight_entry.get(),
        "exam_score": exam_score_entry.get(),
        "desired_grade": desired_grade_entry.get()
    }
    with open("last_calculation.json", "w") as f:
        json.dump(data, f)

def on_backward_click():
    try:
        current_grade = float(current_grade_entry.get())
        exam_weight = float(exam_weight_entry.get())
        desired_grade = float(desired_grade_entry.get())

        required = backward_calculator(desired_grade, exam_weight, current_grade)

        if required > 100:
            result_label.config(text=f"Need {round(required, 1)}% — not reachable")
            save_entries()
        else:
            result_label.config(text=f"You need: {round(required, 1)}% on the exam")
            save_entries()
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def on_click():
    try:
        current_grade = float(current_grade_entry.get())
        exam_weight = float(exam_weight_entry.get())
        exam_score = float(exam_score_entry.get())
        
        final_grade = forward_calculator(current_grade, exam_weight, exam_score)
        result_label.config(text=f"Final Grade: {round(final_grade, 2)}%")
        save_entries()(current_grade, exam_weight, exam_score, final_grade)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Grade Tracker")


entry = tk.Entry(root)
entry.pack()

tk.Label(root, text="Current Grade (%)").pack()
current_grade_entry = tk.Entry(root)
current_grade_entry.pack()

tk.Label(root, text="Exam Weight (%)").pack()
exam_weight_entry = tk.Entry(root)
exam_weight_entry.pack()

tk.Label(root, text="Exam Score (%)").pack()
exam_score_entry = tk.Entry(root)
exam_score_entry.pack()

tk.Label(root, text="Desired Final Grade (%)").pack()
desired_grade_entry = tk.Entry(root)
desired_grade_entry.pack()

tk.Button(root, text="Calculate Final Grade", command=on_click).pack()

tk.Button(root, text="Score Needed on Exam", command=on_backward_click).pack()


result_label = tk.Label(root, text="")
result_label.pack()

last_data = load_last_calculation()
if last_data is not None:
    current_grade_entry.insert(0, last_data.get("current_grade", ""))
    exam_weight_entry.insert(0, last_data.get("exam_weight", ""))
    exam_score_entry.insert(0, last_data.get("exam_score", ""))
    desired_grade_entry.insert(0, last_data.get("desired_grade", ""))

root.mainloop()