import os
import ast
import astor
import click
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def parse_code_elements(filepath):
    """Parses a Python file and extracts functions and classes."""
    with open(filepath, "r", encoding="utf-8") as source:
        try:
            tree = ast.parse(source.read())
        except SyntaxError as e:
            print(f"  Skipping {filepath} due to syntax error: {e}")
            return [] # Skip files with syntax errors

    documents = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            source_code = astor.to_source(node)
            documents.append({
                "code": source_code,
                "filepath": filepath,
                "name": node.name
            })
    return documents

@click.command()
@click.option('--path', required=True, help='The path to the codebase directory to index.')
@click.option('--db-path', default='./code_db', help='The path to store the vector database.')
def index_codebase(path, db_path):
    """Indexes a codebase by parsing all Python files and storing them in a vector DB."""
    all_docs = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                print(f"Parsing: {filepath}")
                all_docs.extend(parse_code_elements(filepath))

    if not all_docs:
        print("No Python functions or classes found to index.")
        return

    print("\nCreating embeddings... (This might take a moment for the first run)")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    texts = [doc['code'] for doc in all_docs]
    metadatas = [{'filepath': doc['filepath'], 'name': doc['name']} for doc in all_docs]
    
    db = Chroma.from_texts(
        texts, 
        embeddings, 
        metadatas=metadatas, 
        persist_directory=db_path
    )
    db.persist()
    print(f"\n✅ Successfully indexed {len(all_docs)} functions/classes into '{db_path}'.")

if __name__ == '__main__':
    index_codebase()