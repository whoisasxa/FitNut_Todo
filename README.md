# Fit & Nut To‑Do (CLI)

A simple, elegant command‑line **to‑do list** tailored for **fitness & nutrition**.
Track workouts, meals, recovery, and mindset with a minimal Python app.

## Features
- Clean CLI with menu: **Add • View • Delete • Quit**
- In‑memory storage via a Python **list**
- Helpful categories: *Workout, Nutrition, Recovery, Mindset*
- Optional **priority** (Low/Medium/High) and **due date** (YYYY‑MM‑DD)
- Robust input validation and error handling (`try/except/else/finally`)
- Zero dependencies — just Python 3.9+

---

## Getting Started

### 1) Clone or download
```bash
git clone https://github.com/whoisasxa/FitNut_Todo.git
cd fitnut-todo
```

### 2) Run
```bash
python fitnut_todo.py
```

> Tip: On some systems you may need `python3` instead of `python`.

---

## Usage
- **Add task**: Provide a title, pick a category/priority, optionally add a due date and notes.
- **View tasks**: Shows tasks sorted by priority then due date.
- **Delete task**: Enter the number shown to remove a task.
- **Quit**: Exit gracefully with a friendly message.

Example entries:
- Workout: `Upper body day` (High, due 2025‑10‑20)
- Nutrition: `Prep 3 lunches` (Medium)
- Recovery: `10‑minute mobility flow` (Low)
- Mindset: `Gratitude journaling`

---

## Testing & Edge Cases
Manually verify the following:
- Viewing with an **empty list** shows an informative message.
- Entering **letters** or out‑of‑range numbers for menu choices triggers a warning.
- Trying to **delete** when there are **no tasks** shows a warning.
- Providing an **invalid date** is handled (date cleared).
- `Ctrl+C` exits gracefully.

---

## Project Structure
```text
fitnut_todo.py   # CLI application (single file)
README.md        # How to run/use and rubric notes
```

---

## Submission Notes
- The app demonstrates:
  - Python **syntax, data types**, and **control flow**
  - **Functions** with descriptive names and docstrings
  - **Input validation** and **error handling** (`try/except/else/finally`)
- Storage is a Python **list** per the assignment.
- No third‑party libraries required.

---

## Publish to GitHub (quick guide)

```bash
# from inside the project folder
git init
git add .
git commit -m "Initial commit: Fit & Nut To-Do"
git branch -M main
git remote add origin https://github.com/<your-username>/fitnut-todo.git
git push -u origin main
```

Replace `<your-username>` with your GitHub handle.

---


