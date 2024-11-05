# main.py

import os
from cv_reader import read_cv
from gpt3_generator import generate_questions_and_answers_with_aiml_api

# Fonction pour ouvrir et analyser le CV
def open_file(filename):
    keywords = read_cv(filename)
    questions_and_answers = generate_questions_and_answers_with_aiml_api(keywords)
    # Afficher les questions et réponses ou les utiliser dans votre application
    print(questions_and_answers)

# Exemple d'utilisation
if __name__ == "__main__":
    cv_filename = "sample_cv.pdf"  # Remplacez par le nom de votre fichier CV
    open_file(cv_filename)
