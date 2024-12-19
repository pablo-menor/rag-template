from doc_process import read_pdf, chunking, generate_embeddings
from vector_db import store_in_chormadb, search
import cohere
from dotenv import load_dotenv
import os

load_dotenv()


model_co = cohere.Client(os.getenv('COHERE_SECRET'))

def create_vector_db():
  folder_path = "./docs"
  for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):
      file_path = os.path.join(folder_path, file_name)
      pages_text = read_pdf(file_path)
      chunks = chunking(pages_text)
      embeddings = generate_embeddings(chunks)
      print(file_name)
      store_in_chormadb(chunks, embeddings, file_path)


def answer_question(query):
  relevant_docs = get_relevant_docs(query)
  response = call_llm(query, relevant_docs)
  return response

def get_relevant_docs(query):
  search_results = search(query, n_results=2)
  documents = []
  for doc in search_results['documents'][0]:
    documents.append({"title": "Doc1", "snippet": f"{doc}"})
    return documents

prompt = f""" 
Analyze the user's query and answer to the best of you capabilities.
User's question: 
"""
def call_llm(query, documents):
  response = model_co.chat(
    model="command-r-plus",
    message=f"{prompt}{query}",
    documents=documents,
    temperature=0.5,
    )
  response_text = response.text 
  return response_text
  