# 🤖 JAC ChatBot 

This project is an **AI-powered RAG (Retrieval Augmented Generation) chatbot** built using **Jac** and **Streamlit**. It uses Supabase for vector storage, sentence-transformers/all-mpnet-base-v2 for embeddings and Google's Gemini API for intelligent document-based responses.

---

## 📌 Overview

The **JAC ChatBot** is a sophisticated web-based conversational AI that:

* Ingests and processes markdown documents from your knowledge base.
* Performs **vector similarity search** using Supabase pgvector for relevant context retrieval.
* Provides **context-aware responses** using Google's Gemini AI with retrieved document snippets.
* Offers an **interactive chat interface** built with Streamlit for seamless user experience.
* Demonstrates **superior performance** compared to basic AI models through RAG architecture.

It's an intelligent solution for document-based question answering, knowledge management, and educational content interaction.

---

## 🔍 Key Features

* 🚀 **Document Ingestion**: Automatically processes markdown files and creates vector embeddings.
* 🔍 **Vector Search**: Uses Supabase pgvector for fast and accurate similarity search.
* 💬 **Interactive Chat**: Clean, user-friendly Streamlit interface for conversations.
* ✅ **Context-Aware**: Retrieves relevant document chunks before generating responses.
* 🧠 **Smart Responses**: Powered by Google's Gemini Pro for high-quality text generation.
* 📊 **Performance Comparison**: Demonstrates improved accuracy over basic AI responses.
* 🔄 **Real-time Processing**: Fast query processing and response generation.
* 📚 **Knowledge Base**: Supports multiple document chapters and sections.

---

## 🔧 Technologies & Tools Used

* **Jac Language** – Core logic and RAG implementation
* **Google Gemini AI** – Embeddings generation and text completion
* **Supabase** – Vector database with pgvector extension
* **Python 3.8+** – Backend runtime environment
* **Streamlit** – Interactive web interface for chat
* **LangChain** – Document processing and text splitting

> ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=FFFF00)
> ![Jac](https://img.shields.io/badge/JacLang-%23009b77.svg?logoColor=white)
> ![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?logo=streamlit&logoColor=white)
> ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white)
> ![Gemini](https://img.shields.io/badge/Gemini_AI-%2300AEEF?logo=google&logoColor=white)

---

## ⚙️ How It Works

1. **Document Processing**: Markdown files are split into chunks and embedded using all-mpnet-base-v2 SLM model.
2. **Vector Storage**: Embeddings are stored in Supabase with pgvector extension for efficient similarity search.
3. **Query Processing**: User queries are embedded and matched against stored document embeddings.
4. **Context Retrieval**: Most relevant document chunks are retrieved based on semantic similarity.
5. **Response Generation**: Retrieved context is used to generate accurate, contextual responses with Gemini Pro.
6. **Interactive Interface**: Users interact through a clean Streamlit web interface.

---

## 🧰 Setup & Run Guide (VS Code)

### ✅ Requirements

* Python 3.8+
* Supabase account and project
* [JacLang CLI](https://jaclang.com/docs/getting-started/installation/)
* All dependencies listed in `requirements.txt`
* Gemini API Key: [Get it here](https://makersuite.google.com/app)

---

### 🔐 Set Up Environment Variables

Create a `.env` file with your credentials:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
GEMINI_API_KEY=your_gemini_api_key
```

**Windows PowerShell (Alternative)**:
```powershell
$env:SUPABASE_URL="your_supabase_url"
$env:SUPABASE_KEY="your_supabase_anon_key"  
$env:GEMINI_API_KEY="your_gemini_api_key"
```

---

### 🏗️ Supabase Database Setup

1. Go to your Supabase project dashboard
2. Navigate to SQL Editor
3. Run the relevant SQL script 

This will:
- Create the `docs` table
- Enable the pgvector extension  
- Create the vector similarity search function
- Add necessary indexes

---

### 🚀 Run the Project Locally

**1. Clone the Repository**:
```bash
git clone https://github.com/SahanUday/Jac_ChatBot.git
cd Jac_ChatBot
```

**2. Install Dependencies**:
```bash
pip install -r requirements.txt
```

**Or install manually**:
```bash
pip install jaclang mtllm gitpython streamlit requests python-dotenv supabase sentence-transformers langchain numpy
```

**3. Start the Chatbot**:
```bash
python main.py
```

**Alternative: Launch with Streamlit**:
```bash
streamlit run app.py
```

**Then open your browser and visit**:
```bash
http://localhost:8501
```

---

## 📊 Performance Comparison

Here's a visual comparison showing how our **RAG-enhanced chatbot** outperforms basic AI responses:

### 🔄 RAG Architecture vs Basic Gemini Flash

| **RAG-Enhanced Response** |
|:-------------------------:|
| ![RAG Response](assets/RAGarc_base_response.jpg) |

| **Basic Gemini Flash Response** |
|:--------------------------------:|
| ![Gemini Flash Response](assets/geminiflash_response.jpg) |

> 🧠 **Key Advantages of RAG Architecture**:
> - **Contextual Accuracy**: Responses based on your specific documents
> - **Domain Knowledge**: Understands your content better than general AI
> - **Factual Reliability**: Reduced hallucination through document grounding
> - **Customizable**: Adapts to your knowledge base and use case

---

## 🛠 Built With

🧬 **JacLang** – for core RAG logic and walker definitions  
🤖 **Google Gemini Pro** – for embeddings and text generation  
🗄️ **Supabase** – for vector database and similarity search  
🐍 **Python 3.8+** – used for backend processing  
🖥️ **Streamlit** – clean and responsive frontend UI  
🦜 **LangChain** – for document processing and text splitting

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
