from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import ast
import openai
import py2neo
from prompt import return_prompt

OPENAI_API_KEY='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'

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Replace these with your actual Neo4j credentials
neo4j_url = "bolt+s://272d3af7.databases.neo4j.io"
neo4j_user = "neo4j"
neo4j_password = "F3d6-Z3O-cZpB3vp6oQdpw8OXl21R_xFLRp9a0PTsNE"
graph = py2neo.Graph(neo4j_url, auth=(neo4j_user, neo4j_password))

app = Flask(__name__)

# The cosine similarity is a measure of similarity between two non-zero vectors by calculating the cosine of the angle between them
def cosine_similarity(a, b):
    a = ast.literal_eval(a)
    b = ast.literal_eval(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_similar_courses(course_id, embeddings, threshold=0.8):
    target_embedding = embeddings[course_id]
    similarities = []

    for idx, embedding in enumerate(embeddings):
        if idx == course_id:
            continue
        
        similarity = cosine_similarity(target_embedding, embedding)
        
        if similarity > threshold:
            similarities.append((idx, similarity))

    # Sort by similarity score
    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities

@app.route('/similar_courses/<course_id>')
def return_similar_courses(course_id):
    df = pd.read_csv('https://testbucket1841.s3.ap-south-1.amazonaws.com/csv-dump/embedded_data.csv')
    embeddings = df['ada_embedding']
    course_idx = df.loc[df['id'] == course_id].index[0]
    sims = find_similar_courses(course_idx, embeddings)
    # Convert the array of tuples into a list of dictionaries
    dict_list = [{'index': t[0], 'similarity': t[1]} for t in sims[:5]]
    key_to_extract = 'index'
    # Extract the indices from the list of dictionaries
    indices = [d[key_to_extract] for d in dict_list]
    # Use the indices to get the corresponding course data rows from the dataframe df
    # Convert the list of dictionaries into a JSON string
    similar_courses_dict_list = df.iloc[indices].drop(['ada_embedding','courseContent','text','tags'], axis=1).to_dict('records')
    similar_courses = jsonify(similar_courses_dict_list)
    return similar_courses


@app.route('/english_to_cypher', methods=['POST'])
def english_to_cypher():
    data = request.get_json()
    english_statement = data.get('statement')

    if not english_statement:
        return jsonify({'error': 'Statement is missing'}), 400

    # Query OpenAI API to get the Cypher query
    prompt = return_prompt(english_statement)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0,
    )
    
    cypher_query = response.choices[0].text.strip().replace('\n', '')
    # Execute the Cypher query against Neo4j
    result = graph.run(cypher_query).data()

    # Return the query result as JSON
    return jsonify(result)