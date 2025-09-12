import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from experiment.callback import TokenUsageHandler
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging 


#Load environment variables from the .env file
load_dotenv()

#Loading a json file
with open("Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#Creating a title for the app
st.title("MCQs Creater Application with Langchain 🦜⛓️‍💥")

#Create a form using st.form
with st.form("user_inputs"):
    #File Upload 
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    #Input Fields
    mcq_count = st.number_input("No. of MCQs", min_value = 3, max_value=50)
     
    #Subject
    subject = st.text_input("Insert Subject", max_chars = 20)

    #Quiz Tone 
    tone = st.text_input("Complexity Level of the Questions", max_chars=20, placeholder="Simple")

    #Add Button 
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                #Count tokens and the cost of API call
                # with TokenUsageHandler() as cb:
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
                 
            else:
                # print(f"Total Tokens: {cb.total_tokens}")
                # print(f"Prompt Tokens:{cb.prompt_tokens}")
                # print(f"Completion Tokens:{cb.completion_tokens}")
                # print(f"Total_Cost: {cb.total_cost}")
                if isinstance(response, dict):
                    # Extract the quiz data from the response

                    quiz = response.get("quiz", None)
                    start = quiz.find("{")
                    end = quiz.rfind("}") + 1
                    quiz = quiz[start:end]
                    # quiz_json= json.loads(quiz)
                    print("*********************************************** Here is the Response ***********************************************", response)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        # st.write("DEBUG - type of table_data:", type(table_data))
                        # st.write("DEBUG - table_data content:", table_data)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            #Display the review in atext box as well
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")
                    
                    else:
                        st.write(response)
                    