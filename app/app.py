import sys
from dotenv import load_dotenv
load_dotenv()
from nlp_to_sql import main
from global_variables import DATABASE_NAME
from db_handler import get_data


def cli_app():
    """
    CLI App: Takes input query and gets the output
    """
    if len(sys.argv) < 2:
        print("Usage: python app.py <input_query>")
        sys.exit(1)

    input_query = sys.argv[1]
    input_event = {
        "input_query": input_query}
    input_natural_language_query = input_event["input_query"]
    
    # To Update the DB
    if input_event["input_query"]=='update_db':
        get_data(query='', db_name=DATABASE_NAME, create_db=True)
        return "--Database Updated--"
    # Answer of the Natural language Query
    output = main(input_natural_language_query)
    return output


if __name__ == '__main__':
    cli_app()
