# gpt3_generator.py

import openai
from cv_reader import read_cv

def generate_questions_and_answers_with_gpt3(cv_file):
    text_from_cv = read_cv(cv_file)

    client = openai.OpenAI(api_key="a12d74adbf9445cb8271f6d908bd0b7c", base_url="https://api.aimlapi.com")

    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": "You are reviewing a candidate's CV. Be descriptive and professional."},
            {"role": "user", "content": text_from_cv}
        ],
        temperature=0.7,
        max_tokens=128,
    )

    response = chat_completion.choices[0].message.content
    return response
