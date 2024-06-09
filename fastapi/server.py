from fastapi import FastAPI
from pydantic import BaseModel
from functions import *
import logging
from log_folder.logging_config import get_logger

logger = get_logger()

# logging.basicConfig(filename='./log_folder/app.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#                     datefmt='%d-%b-%Y %H:%M:%S')

app = FastAPI()

class QuestionInput(BaseModel):
    pdf_path: str
    questions: list[str]

@app.post("/answer-questions")
def answer_questions(input_data: QuestionInput):

    logger.info("list of questions: %s", input_data.questions)

    pdf_path = input_data.pdf_path
    questions = input_data.questions
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    logger.info("Successfully extracted text from PDF !!")
    
    # SUmmarize the text
    summary = get_summary_from_chunks(pdf_text)
    logger.info("Successfully created summary !!")

    results = {}
    for question in questions:
        answer = get_answer_from_text(summary, question)
        results[question] = answer
    logger.info("Successfully retrieved answers for questions from summary !!")
    
    # Post results to Slack
    post_slack(results)
    logger.info("Successfully posted to slack !!")
    
    logger.info("results: %s", results)
    return results
