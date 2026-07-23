# Grade Calculator

A grade calculator that works in two directions: it can tell you your final
grade given an exam score, or tell you what score you need on the exam to
hit a target final grade.

## Files

- `grade_calculator.py` — terminal version with a menu
- `grade_tracker_gui.py` — GUI version built with tkinter

Both share the same calculation functions, so the math only lives in one place.

## Running it

Terminal version:

    python3 grade_calculator.py

GUI version:

    python3 grade_tracker_gui.py

## Features

- **Calculate Final Grade** — enter current grade, exam weight, and exam
  score to get your final grade
- **Score Needed on Exam** — enter current grade, exam weight, and desired
  final grade to get the score you need, with a warning when the target
  isn't reachable
- Input validation — non-numeric entries show an error instead of crashing
- The GUI saves your last inputs to `last_calculation.json` and reloads
  them the next time you open it

## Built with

Python 3, tkinter (standard library), json (standard library)