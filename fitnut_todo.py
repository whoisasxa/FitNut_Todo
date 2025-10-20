"""
Fit & Nut To‑Do — a simple, clean CLI to track fitness and nutrition tasks.

Storage: in‑memory Python list (no files, no DB).
Run: python fitnut_todo.py
"""
from datetime import datetime
import sys

# Global in‑memory store (list of dicts)
TASKS = []

CATEGORIES = ["Workout", "Nutrition", "Recovery", "Mindset"]
PRIORITIES = ["Low", "Medium", "High"]


def divider(char="─", width=54):
    return char * width


def header(title="Fit & Nut To‑Do"):
    print("\n" + divider("═"))
    print(f"  {title}")
    print(divider("═"))


def pretty_task(t, idx):
    due = f" (due {t['due']})" if t['due'] else ""
    notes = f" — {t['notes']}" if t['notes'] else ""
    return f"[{idx}] {t['category']} • {t['title']} • {t['priority']}{due}{notes}"


def show_menu():
    header()
    print("  1) Add task")
    print("  2) View tasks")
    print("  3) Delete task")
    print("  4) Quit")
    print(divider())


def prompt_choice(prompt, min_val, max_val):
    """
    Get an integer choice within [min_val, max_val] with validation.
    Demonstrates try/except/else/finally for the assignment rubric.
    """
    while True:
        try:
            raw = input(prompt).strip()
            choice = int(raw)
            if choice < min_val or choice > max_val:
                raise ValueError("Choice out of range.")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number shown in the menu.")
        else:
            return choice
        finally:
            # Always runs, even if the user mis‑types
            pass


def prompt_from_list(title, options):
    print(f"Select {title}:")
    for i, opt in enumerate(options, start=1):
        print(f"  {i}) {opt}")
    idx = prompt_choice("Enter number: ", 1, len(options))
    return options[idx - 1]


def prompt_date(label="Due date (YYYY‑MM‑DD, optional)"):
    raw = input(f"{label}: ").strip()
    if not raw:
        return ""
    try:
        # Validate format but store as original string
        datetime.strptime(raw, "%Y-%m-%d")
        return raw
    except ValueError:
        print("⚠️  Invalid date. Leaving blank.")
        return ""


def add_task():
    header("Add Task")
    title = input('Task title (e.g., "Upper body day", "Track macros"): ').strip()
    if not title:
        print("⚠️  Title cannot be empty. Task not added.")
        return

    category = prompt_from_list("category", CATEGORIES)
    priority = prompt_from_list("priority", PRIORITIES)
    due = prompt_date()
    notes = input("Notes (optional): ").strip()

    TASKS.append({
        "title": title,
        "category": category,
        "priority": priority,
        "due": due,
        "notes": notes,
    })
    print("✅  Task added!")


def view_tasks():
    header("Your Tasks")
    if not TASKS:
        print("ℹ️  No tasks to view. Add one from the main menu.")
        return
    # Sort by priority then due date (blank due dates last)
    priority_rank = {p: i for i, p in enumerate(PRIORITIES)}

    def sort_key(t):
        due_key = t["due"] if t["due"] else "9999-12-31"
        return (priority_rank.get(t["priority"], 9), due_key, t["category"], t["title"].lower())

    sorted_tasks = sorted(TASKS, key=sort_key)
    for idx, task in enumerate(sorted_tasks, start=1):
        print(pretty_task(task, idx))
    print(divider())


def delete_task():
    header("Delete Task")
    if not TASKS:
        print("ℹ️  No tasks available to delete.")
        return

    # Show current tasks with their positions in the current list order
    for i, t in enumerate(TASKS, start=1):
        print(pretty_task(t, i))
    print(divider())

    try:
        idx = prompt_choice("Enter the task number to delete: ", 1, len(TASKS))
        removed = TASKS.pop(idx - 1)
    except IndexError:
        # Should not happen because of prompt_choice validation, but included to demonstrate handling
        print("⚠️  That task doesn’t exist.")
        return
    else:
        print(f"🗑️  Deleted: {removed['title']} ({removed['category']})")
    finally:
        # Helpful footer after any attempt
        print(divider())


def main_loop():
    print("\nWelcome to Fit & Nut To‑Do ✨ — track workouts, meals, recovery, and mindset.")
    print('Tip: Keep entries short and action‑oriented (e.g., "5x5 squats", "prep 3 lunches").')
    try:
        while True:
            show_menu()
            choice = prompt_choice("Choose an option (1-4): ", 1, 4)
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("👋  Good luck with your goals!")
                break
    except KeyboardInterrupt:
        print("\n^C  Exiting… stay consistent!")
    finally:
        # Ensures a friendly goodbye regardless of how the loop ends
        print("Bye Now!")


if __name__ == "__main__":
    main_loop()
