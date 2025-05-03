# import os
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI

# # Set API keys for OpenAI
# os.environ["OPENAI_API_KEY"] = "your api key"

# # Path to your document file (occams.txt)
# file_path = 'occams.txt'

# # Read the content of the file
# with open(file_path, 'r', encoding='utf-8') as file:
#     raw_text = file.read()

# # Split the text into manageable chunks
# text_splitter = CharacterTextSplitter(
#     separator="\n",  # Split by new line
#     chunk_size=1000,  # Max size of each chunk
#     chunk_overlap=200,  # Overlap for chunking to maintain context
#     length_function=len,
# )
# texts = text_splitter.split_text(raw_text)

# # Create embeddings for the documents
# embeddings = OpenAIEmbeddings()

# # Store the embeddings in FAISS (a vector database for efficient search)
# document_search = FAISS.from_texts(texts, embeddings)

# # Load the QA chain with OpenAI for question answering
# chain = load_qa_chain(OpenAI(max_tokens=2000), chain_type="map_reduce")

# # Function to process the query and return the answer
# def get_answer_from_document(query):
#     # Perform similarity search to find the most relevant documents
#     docs = document_search.similarity_search(query, k=5)  # Retrieve top 5 relevant documents
#     answer = chain.run(input_documents=docs, question=query)  # Run the QA chain on those documents
#     return answer

# # Get the query from the command line arguments
# import sys
# query = sys.argv[1]  # The query is passed as the first argument

# # Get the answer based on the query
# answer = get_answer_from_document(query)

# # Output the answer to the console
# print(answer)


import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# Load environment variables from the .env file located in the backend directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Path to your document file (occams.txt)
file_path = 'occams.txt'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    raw_text = file.read()

# Split the text into manageable chunks
text_splitter = CharacterTextSplitter(
    separator="\n",  # Split by new line
    chunk_size=1000,  # Max size of each chunk
    chunk_overlap=200,  # Overlap for chunking to maintain context
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Create embeddings for the documents
embeddings = OpenAIEmbeddings()

# Store the embeddings in FAISS (a vector database for efficient search)
document_search = FAISS.from_texts(texts, embeddings)

# Load the QA chain with OpenAI for question answering
chain = load_qa_chain(OpenAI(max_tokens=2000), chain_type="map_reduce")

# Define the system prompt
system_prompt = """
You are a helpful assistant that provides concise and accurate answers based on the given document. 
Use the context from the document to answer the question and provide detailed explanations where necessary. 
Your response should be clear and well-structured.
"""

# Function to process the query and return the answer
def get_answer_from_document(query):
    # Perform similarity search to find the most relevant documents
    docs = document_search.similarity_search(query, k=5)  # Retrieve top 5 relevant documents

    # Run the QA chain on those documents, passing the system prompt
    answer = chain.run(input_documents=docs, question=query, system_message=system_prompt)
    return answer

# Get the query from the command line arguments
import sys
query = sys.argv[1]  # The query is passed as the first argument

# Get the answer based on the query
answer = get_answer_from_document(query)

# Output the answer to the console
print(answer)
