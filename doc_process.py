import  PyPDF2
from sentence_transformers import SentenceTransformer

def read_pdf(file_path):
  with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    pages_text = [page.extract_text() for page in reader.pages]
  return pages_text

def chunking(pages_text):
  return pages_text   

# Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
  embeddgins = model.encode(chunks, convert_to_tensor=True)
  return embeddgins