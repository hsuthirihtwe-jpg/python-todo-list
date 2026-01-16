# Basic To-Do List - Step 1: Add tasks

tasks = []  # empty list to store tasks

while True:
    task = input("Enter a task (or type 'quit' to stop): ")
    if task.lower() == 'quit':
        break
    tasks.append(task)
    print("Task added!")

# Show all tasks at the end
print("\nYour tasks:")
for t in tasks:
    print("-", t)
