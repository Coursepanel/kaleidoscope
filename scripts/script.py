from neo4j import GraphDatabase
import time
import traceback


def read_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


# Replace these with your actual Neo4j credentials
neo4j_url = "--"
neo4j_user = "neo4j"
neo4j_password = "----"

# Connect to the Neo4j database
driver = GraphDatabase.driver(neo4j_url, auth=(neo4j_user, neo4j_password))

# Your list of 2600 Cypher queries
queries = read_lines_to_list('./generated/prereq-code19.txt')

# Define a function to execute a batch of queries


def execute_batch(tx, batch):
    for query in batch:
        tx.run(query)


# Define batch size and the number of queries
batch_size = 1
num_queries = len(queries)

# Iterate through batches of queries
# Function to log errors to a text file


def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(error_message)


for i in range(0, num_queries, batch_size):
    batch = queries[i:i + batch_size]
    print(f"Executing queries {i + 1} to {i + len(batch)}")

    try:
        with driver.session() as session:
            session.execute_write(execute_batch, batch)

    except Exception as e:
        error_message = f"Error executing queries {i + 1} to {i + len(batch)}: {str(e)}\n"
        error_message += "Traceback:\n" + traceback.format_exc() + "\n"
        log_error(error_message)
        print("Error encountered. Check error_log.txt for details.")

    # Pause for a short time (e.g., 1 second) before executing the next batch
    time.sleep(1)

# Close the driver
driver.close()
