import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# Set API keys
os.environ["OPENAI_API_KEY"] = "your openai api key"
os.environ["SERPAPI_API_KEY"] = "your serpai api key"

# Read the content of the text file with correct encoding
file_path = r'backend\occams.txt'  # raw string avoids escape issues
with open(file_path, 'r', encoding='utf-8') as file:
    raw_text = file.read()

# Optional: print raw text for debug
# print(raw_text)

# Split the text into manageable chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create FAISS vector store
document_search = FAISS.from_texts(texts, embeddings)

# Load the QA chain
chain = load_qa_chain(OpenAI(max_tokens=2000), chain_type="map_reduce")

# Function to get answer from document
def get_answer_from_document(query):
    docs = document_search.similarity_search(query, k=5)
    answer = chain.run(input_documents=docs, question=query)
    return answer

# Example usage
query = "Which awards did Occams Advisory receive in 2024?"
answer = get_answer_from_document(query)

print("Answer:", answer)
