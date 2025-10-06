🤖 RefactoPilot
An AI-powered assistant that provides context-aware refactoring suggestions directly in your VS Code editor.

RefactoPilot goes beyond simple static analysis. It uses a Retrieval-Augmented Generation (RAG) pipeline to understand the context of your entire codebase, offering intelligent insights to help you write cleaner, more maintainable code.

🚀 Features
Context-Aware Analysis: Understands your entire project to provide suggestions based on existing patterns and duplicated logic.

AI-Powered Suggestions: Leverages Large Language Models to generate human-like explanations and refactored code snippets.

Seamless IDE Integration: Right-click any function name in VS Code to get instant analysis and feedback.

Semantic Understanding: Uses Abstract Syntax Trees (AST) to parse code, ensuring a deep and accurate understanding of your project's structure.

🛠️ Tech Stack
This project is a combination of a Python backend and a TypeScript-based VS Code extension.

Backend (Core Engine):

Python 3.9+

LangChain: For orchestrating the RAG pipeline.

Google Gemini: The LLM used for generating suggestions.

ChromaDB: For storing code embeddings as a local vector database.

SentenceTransformers: For creating vector embeddings of code.

Click: For creating the command-line interface.

Frontend (IDE Integration):

TypeScript

VS Code Extension API

Node.js

