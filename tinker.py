import json
import tkinter as tk

from grade_calculator import forward_calculator

def load_last_calculation():
    try:
        with open("last_calculation.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_last_calculation(current_grade, exam_weight, exam_score, final_grade):
    data = {
        "current_grade": current_grade,
        "exam_weight": exam_weight,
        "exam_score": exam_score,
        "final_grade": final_grade
    }
    with open("last_calculation.json", "w") as f:
        json.dump(data, f)

def on_click():
    try:
        current_grade = float(current_grade_entry.get())
        exam_weight = float(exam_weight_entry.get())
        exam_score = float(exam_score_entry.get())
        
        final_grade = forward_calculator(current_grade, exam_weight, exam_score)
        result_label.config(text=f"Final Grade: {round(final_grade, 2)}%")
        save_last_calculation(current_grade, exam_weight, exam_score, final_grade)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Grade Tracker")

# --- Step 1 goes here, replacing this ---
entry = tk.Entry(root)
entry.pack()
# --- with this ---
tk.Label(root, text="Current Grade (%)").pack()
current_grade_entry = tk.Entry(root)
current_grade_entry.pack()

tk.Label(root, text="Exam Weight (%)").pack()
exam_weight_entry = tk.Entry(root)
exam_weight_entry.pack()

tk.Label(root, text="Exam Score (%)").pack()
exam_score_entry = tk.Entry(root)
exam_score_entry.pack()

tk.Button(root, text="Calculate", command=on_click).pack()

result_label = tk.Label(root, text="")
result_label.pack()

last_data = load_last_calculation()
if last_data is not None:
    current_grade_entry.insert(0, str(last_data["current_grade"]))
    exam_weight_entry.insert(0, str(last_data["exam_weight"]))
    exam_score_entry.insert(0, str(last_data["exam_score"]))

root.mainloop()