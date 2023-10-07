import tkinter as tk
import random

# Function to start the quiz
def start_quiz():
    # Read questions from a file and store them in a list
    questions = []
    with open('questions.csv', 'r') as file:
        for line in file:
            question, answer = line.strip().split(',')
            questions.append((question, answer))

    # Randomly select questions for the quiz
    num_questions = int(num_questions_entry.get())
    selected_questions = random.sample(questions, num_questions)

    # Display questions and collect user answers (you'll need to implement this part)

# Create the GUI
root = tk.Tk()
root.title("Quiz Maker")

# Label and Entry for the number of questions
num_questions_label = tk.Label(root, text="Number of Questions:")
num_questions_label.pack()
num_questions_entry = tk.Entry(root)
num_questions_entry.pack()

# Start Quiz Button
start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

root.mainloop()