import openai

from chatgpt_exp.job_description import read_job_description
from chatgpt_exp.resume import read_resume

API_KEY = "YOUR_API_KEY_HERE"


def main():
    """Entry point for the application script"""
    openai.api_key = API_KEY
    model_engine = "gpt-3.5-turbo"
    print(read_job_description())
    print(read_resume())
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are an interviewer."},
            {"role": "user", "content": read_job_description()},
            {"role": "user", "content": read_resume()},
            {"role": "user", "content": "is this resume a good fit for the job description?"},
        ])
    message = response.choices[0]['message']
    print("{}: {}".format(message['role'], message['content']))
