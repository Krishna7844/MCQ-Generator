from setuptools import find_packages, setup

setup(
    name = "mcqgenerator",
    version = '0.0.1',
    author = 'krishna',
    author_email= 'himanshu.kmp.prajapati@gmail.com',
    install_requires = ["google-genai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
)

