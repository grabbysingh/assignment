import os
import requests
import streamlit as st
import logging
from log_folder.logging_config import get_logger

logger = get_logger()

# logging.basicConfig(filename='./log_folder/app.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#                     datefmt='%d-%b-%Y %H:%M:%S')

st.set_page_config(layout="wide")
st.title("AI Agent")
col1, col2 = st.columns(2)

# File upload and total no of questions on left side
with col1:
    st.header("Upload PDF File")
    pdf_file = st.file_uploader(" ", type=['pdf'])
    st.subheader("How many questions do you have?")
    num_questions = st.number_input(" ", min_value=1)
logger.info("Successfully taken pdf file and number of questions !!")

# All questions input on right side
with col2:
    st.subheader("Write all Questions below !!")
    lst_questions = []
    for i in range(num_questions):
        question_text = st.text_area(f"Enter question {i+1}", "")
        lst_questions.append(question_text)
logger.info("Successfully taken all questions !!")

# Save PDF Path
pdf_save_path = None
if pdf_file:
    pdf_save_path = os.path.join("./uploaded_pdfs", pdf_file.name)
    try:
        with open(pdf_save_path, "wb") as f:
            f.write(pdf_file.getvalue())
        logger.info("PDF file saved at: %s", pdf_save_path)
    except Exception as e:
        logger.error("Error saving PDF file: %s", e)
logger.info("Successfully saved pdf file to %s!!", pdf_save_path)

# Process Questions
if pdf_file and lst_questions:
    col1, col2, col3 = st.columns([1, 1, 2])
    with col3:
        process_questions = st.button("Process Questions !!")
    if process_questions:
        # Send data to FastAPI endpoint
        data = {'pdf_path': pdf_save_path, 'questions': lst_questions}
        response = requests.post('http://fastapi-server:8000/answer-questions', json=data)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error processing questions")
logger.info("Successfully sent data to fastapi functions for processing !!")
