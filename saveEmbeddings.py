import os, glob
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import numpy as np

# --- Load environment variables ---
load_dotenv()

# --- configure Supabase ---
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- configure SentenceTransformer ---
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# --- embedding function ---
def get_embedding(text):
    # Returns embedding as list (compatible with Supabase vector storage)
    emb = model.encode([text])[0]
    return emb.tolist()  # convert numpy array to list

# --- load markdown files ---
md_paths = glob.glob("docs/**/*.md", recursive=True)

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

for path in md_paths:
    with open(path, "r", encoding="utf-8") as f:
        md = f.read()
    chunks = splitter.split_text(md)

    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk)
        row = {
            "content": chunk,
            "embedding": emb,
            "metadata": {"file": os.path.basename(path), "chunk": i}
        }
        supabase.table("docs").insert(row).execute()

print("All markdown files ingested with local embeddings.")
