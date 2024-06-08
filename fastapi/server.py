from fastapi import FastAPI
from pydantic import BaseModel
from functions import *

app = FastAPI()

class QuestionInput(BaseModel):
    pdf_path: str
    questions: list[str]

@app.post("/answer-questions")
def answer_questions(input_data: QuestionInput):

    pdf_path = input_data.pdf_path
    questions = input_data.questions
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # SUmmarize the text
    summary = get_summary_from_chunks(pdf_text)

    results = {}
    for question in questions:
        answer = get_answer_from_text(summary, question)
        results[question] = answer
    
    # Post results to Slack
    post_slack(results)
    
    return results
