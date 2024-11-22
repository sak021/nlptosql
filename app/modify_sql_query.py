import sqlparse
import re
from search_model import match_column_to_query
from db_handler import get_data
from global_variables import DATABASE_NAME, TABLE_NAME


def modify_sql_query(sql_query):
    """
    Parse and modify the WHERE clause of an SQL query.

    Args:
        sql_query (str): Original SQL query.
        modifications (str): Modifications to add to the WHERE clause.

    Returns:
        str: Modified SQL query.
    """
    # Parse the SQL query
    parsed_query = sqlparse.parse(sql_query)[0]
    
    # Split the query into tokens
    # Find and modify the WHERE clause
    modified_tokens = []
    for token in parsed_query.tokens:
        if token.ttype is None and token.value.startswith('WHERE'):  # Locate WHERE clause
            where_clause = token.value

            # Modify the WHERE clause (simple example: append modifications)
            new_where_clause = f"WHERE {modify_where_clause(where_clause)}"
            token.value = new_where_clause
        modified_tokens.append(token.value)

    

    modified_query = "".join(modified_tokens)
    if not modified_query.endswith(';'):
        return f"{modified_query};"
    return modified_query


def modify_where_clause(where_clause):
    # 
    where_clause = where_clause.replace("WHERE", "")

    where_clause_list = where_clause.split("AND")
    individual_where_clause = []
    for where_clause in where_clause_list:
        individual_where_clause.append(update_individual_where_clause(where_clause))
    return ' AND'.join(individual_where_clause)


def update_individual_where_clause(where_clause):   
    if "=" in where_clause:
        pattern = r"(\w+)\s*=\s*'(\w+)'"
        # Search for the pattern
        match = re.search(pattern, where_clause)

        if match:
            # Extract the variable and its value
            column_name = match.group(1)
            column_value = match.group(2)
        else:
            return where_clause

        # Get Data from data base
        query = f"SELECT * FROM {TABLE_NAME};"
        df = get_data(query, db_name=DATABASE_NAME)
        # df  = pd.read_csv('app/weather_data.csv')
        column_data = df[column_name].str.lower().unique()

        # Match
        matches = match_column_to_query(column_value, column_data)
        print(column_name, matches)
        return f"LOWER({column_name}) IN ({', '.join([repr(val) for val in matches])})"
    return where_clause



if __name__ == "__main__":

    # Example SQL query
    sql_query = """
    SELECT city
    FROM Weather_Data
    WHERE weather = 'raining';
    """


    # Apply the modification
    modified_query = modify_sql_query(sql_query)
    print("Modified Query:\n", modified_query)

