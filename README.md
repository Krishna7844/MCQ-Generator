**ABOUT THIS PROJECT**

The MCQ Generator is an end-to-end application that automatically generates multiple-choice questions from text-based files such as PDF and TXT. By leveraging the Gemini API, the project extracts content from the uploaded file and creates a set of questions with four options and the correct answer. Users can specify how many questions they want, making it useful for quizzes, practice tests, and assessments.

The project is built with Python, LangChain, and Streamlit, combining natural language processing with a clean and interactive web interface. It also integrates environment management using dotenv for secure API handling. This project highlights skills in NLP, LLM integration, and full-stack AI application deployment, offering a practical solution for educators, students, and training professionals.


**HOW TO INSTALL IMPORTANT LIBRARIES**

First locate your terminal to the main directory of this project then write this command in the terminal---->👇🏻

```pip install -r requirements.txt```

**HOW TO RUN THIS PROJECT**

First things first you need to make a file with the name ".env" in the root directory and paste the gemini API-KEY there like this ----->👇🏻

```API_KEY = "Enter your gemini api key"```

Open the file named as StreamlitAPP.py and the type the command in the terminal----->👇🏻

```streamlit run StreamlitAPP.py```

**HOW TO MODIFY YOUR MCQ GENERATOR MODEL**
 
Go to the file MCQGenertor.py which is inside the "src/mcqgenerator" folder and there you can change your prompt according to your need.



ENJOY ;).....