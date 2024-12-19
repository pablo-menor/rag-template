from chromadb import Client
from sentence_transformers import SentenceTransformer
import random

client = Client()
collection = client.get_or_create_collection(name='test_collection')

model = SentenceTransformer('all-MiniLM-L6-v2')

def store_in_chormadb(chunks, embeddings, file_name):
  for i, (chunk, embeddings) in enumerate(zip(chunks, embeddings)):
    collection.add(
        documents=[chunk],
        embeddings=[embeddings.cpu().numpy().tolist()],
        metadatas=[{"file_name": file_name}],
        ids = [f'{file_name}_chunk{i+1}_{random.randint(1, 10000)}']
    )

def search(query, n_results=1):
  query_embedding = model.encode(query, convert_to_tensor=True)
  results = collection.query(query_embedding.cpu().numpy().tolist(), n_results=n_results)
  return results
