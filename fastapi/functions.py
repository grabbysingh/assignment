import os
import fitz
import openai
# import config
from slack_sdk import WebClient
from dotenv import load_dotenv
import logging
from log_folder.logging_config import get_logger

logger = get_logger()

# logging.basicConfig(filename='./log_folder/app.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#                     datefmt='%d-%b-%Y %H:%M:%S')

load_dotenv()

model_name = "gpt-3.5-turbo-0125"
# openai.api_key = config.OPENAI_API_KEY
# client = WebClient(token=config.SLACK_TOKEN)
openai.api_key = os.getenv("OPENAI_API_KEY")
client = WebClient(token=os.getenv("SLACK_TOKEN"))

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document[page_num]
            text += page.get_text()
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")

def get_summary_from_chunks(text):
    try:
        chunk_size = 10800
        lst_text = text.split(' ')
        num = round(len(lst_text)/chunk_size)
        summary_size = round(chunk_size/num) if num != 0 else chunk_size
        chunks = [" ".join(lst_text[i:i + chunk_size]) for i in range(0, len(lst_text), chunk_size)]

        summary = ""
        for chunk in chunks:
            response = openai.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": f"You are an assistant that summarizes the given text in {summary_size} words"},
                    {"role": "user", "content": f"Text: {chunk}"}
                ]
            )
            answer = response.choices[0].message.content.strip()
            summary += answer
        return summary
    except Exception as e:
        logger.error(f"Error getting summary from OpenAI: {e}")

def get_answer_from_text(text_summary, question):
    try:
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are an assistant that extracts information from text."},
                {"role": "user", "content": f"Text: {text_summary}"},
                {"role": "user", "content": f"Question: {question}"}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        logger.error(f"Error getting answer from OpenAI: {e}")
        return "Data Not Available"

def post_slack(dct_qa):
    try:
        for question, answer in dct_qa.items():
            client.chat_postMessage(
                channel="bot-updates",
                text=str(f"Question: {question}, Answer: {answer}"),
                username="Bot User"
            )
    except Exception as e:
        logger.error(f"Error posting to Slack: {e}")