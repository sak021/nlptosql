from db_handler import get_data
from llm import fetch_llm_response, parse_llm_response
from global_variables import DATABASE_NAME
from modify_sql_query import modify_sql_query


def natural_language_to_sql(natural_language_query):
    # Get generated SQL Query from intent using LLM
    llm_response = fetch_llm_response(natural_language_query)
    sql_query = parse_llm_response(llm_response.content)
    return sql_query


def get_answer_using_sql_query(sql_query_modified):
    # Execute the SQL Query and get the ouptut
    answer = get_data(sql_query_modified, db_name=DATABASE_NAME)
    return answer


def format_sql_output(df):
    """
    Format the SQL output i.e. dataframe to a list(multiple values) or single value
    """
    if df.empty:
        return "No Data Found"
    elif df.shape[0] == 1 and df.shape[1] == 1:  # Single value
        return df.iloc[0, 0]
    elif df.shape[1] == 1:  # Single column
        return df.iloc[:, 0].tolist()
    else:  # Multiple columns
        return [tuple(row) for row in df.itertuples(index=False, name=None)]
    

def main(natural_language_query):
    """
    Input: Input Query
    Output: Value from SQL Database
    """
    sql_query = natural_language_to_sql(natural_language_query)
    sql_query_modified = modify_sql_query(sql_query)
    answer = get_answer_using_sql_query(sql_query_modified)
    formatted_answer = f"Answer is: {format_sql_output(answer)}"
    return formatted_answer

if __name__ == "__main__":
    natural_language_query = "What's the temperature in Fort Worth?"
    output = main(natural_language_query)
    print(output)