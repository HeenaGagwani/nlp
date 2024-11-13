from neo4j import GraphDatabase
import streamlit as st

# Update with your Neo4j connection details
uri = st.secrets["NEO4J_URI"]
username = st.secrets["NEO4J_USERNAME"]
password =  st.secrets["NEO4J_PASSWORD"]

driver = GraphDatabase.driver(uri, auth=(username, password))

def execute_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]
