from neo4j_graph import execute_query
from llm import generate_response

def handle_query(user_input):
    # Here you can still convert user input into Cypher queries
    if "total movies" in user_input.lower():
        query = "MATCH (t:Movie) RETURN COUNT(t) AS movies"
    elif "fraud transactions" in user_input.lower():
        query = "MATCH (t:Transaction) WHERE t.fraud = 1 RETURN COUNT(t) AS fraud_transactions"
    elif "transactions for customer" in user_input:
        customer_id = user_input.split()[-1]  # Assumes the user ends the input with the customer ID
        query = f'MATCH (t:Customer {{customerId: "{customer_id}"}})-[:MADE]->(c:Transaction) RETURN c'
    else:
        return "Sorry, I didn't understand your question."

    # Execute the Cypher query
    results = execute_query(query)
    
    # If there are results, prepare a response
    if results:
        response_text = f"The query returned: {results}"
    else:
        response_text = "No results found."

    # Use OpenAI to generate a more natural response
    final_response = generate_response(response_text)
    return final_response
