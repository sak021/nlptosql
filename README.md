**NLP to SQL Converter**

This project allows users to convert natural language queries into SQL queries and retrieve the answers from a database. The application is built with the aim of simplifying data querying, enabling users without SQL knowledge to interact with databases effortlessly.

Features
Converts natural language questions to SQL queries.
Executes generated SQL queries against a database.

Prerequisites
Ensure you have the following installed:

Python 3.9 or higher
pip (Python package manager)
A valid SQLite database (or compatible database)

Installation
Clone the Repository
git clone https://github.com/sak021/nlptosql.git  
cd NLPtoSQL  

Set Up the Environment
Create a virtual environment:
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate  

Install dependencies:
pip install -r requirements.txt  

Run Application:
Run run_test_cases.py file
Example: python3 run_test_cases.py "Your Query Here"



File Structure:

NLPtoSQL/  
│  
├── app/  
│   ├── app.py              # CLI application  
│   ├── db_handler.py       # Database handling/querying logic  
│   └── llm.py/             # Gemini Model api handling logic
│   └── modify_sql_query.py # Modify SQL query according to the data in the database 
│   ├── search_model.py     # Search model to handle matching values in SQL Query (SQL Query works on exact matches)
│   └── weather_data.csv    # Weather Data
│   └── Weather.db          # SQL Db for Weather Data
│   └── global_variables.py # Contain Global Variables
│  
├── run_test_cases.py   # Run test cases 
├── requirements.txt    # Python dependencies   
├── .env                # Environment variables  
└── README.md           # Documentation  


Improvements:
Search model could be improved to take into account spelling mistakes/closely related words (can be done by finetuning or using other models) 

Contact
For queries or support, please reach out to salmanskhan21@gmail.com.
