# Reference - https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/pinecone.html
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import CSVLoader
from dotenv import load_dotenv
import os

load_dotenv()

loader= CSVLoader(file_path="/Users/ankitsanghvi/Desktop/kaleido_gpt/data/course-info.csv")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2048, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
# initialize pinecone
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment="northamerica-northeast1-gcp" # next to api key in console
)
index_name = "openai"

print("Creating 🍍 index...")
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
print("🍍 index created ! 🎉...")

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "Which is the best course for machine learning?"
print("Searching for similar documents to: ", query)
docs = docsearch.similarity_search(query)
print(docs[0].page_content)