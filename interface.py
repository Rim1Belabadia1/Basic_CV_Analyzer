import tkinter as tk
from tkinter import filedialog, Text
import os
from cv_reader import read_cv
from gpt3_generator import generate_questions_and_answers_with_gpt3

root = tk.Tk()

def upload_cv():
    file_path = filedialog.askopenfilename()
    # Call function to process the uploaded CV
    questions_and_answers = generate_questions_and_answers_with_gpt3(file_path)
    # Display questions and answers in the interface
    text.insert(tk.END, questions_and_answers)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

upload_button = tk.Button(root, text="Upload CV", padx=10, pady=5, fg="white", bg="#263D42", command=upload_cv)
upload_button.pack()

text = tk.Text(frame)
text.pack()

root.mainloop()
