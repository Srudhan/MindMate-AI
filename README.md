# 🧠 MindMate AI - Emotion Aware Mental Wellness Assistant

MindMate AI is a local AI-powered mental wellness assistant designed to provide supportive conversations, personalized responses, and evidence-based coping strategies.

The project combines Large Language Model concepts, Natural Language Processing (NLP), Retrieval-Augmented Generation (RAG), and conversational memory to create an empathetic chatbot that can understand a user's mental state and respond accordingly.

Unlike many AI chatbots that depend on cloud APIs, MindMate AI runs completely on local hardware using Small Language Models (SLMs), making it lightweight, private, and cost-effective.

---

## ✨ Features

### 💬 Conversational Mental Wellness Assistant

* Interactive chat interface built with Streamlit.
* Provides supportive and empathetic responses.
* Maintains conversation history during the session.

### 🧠 Mental State Detection

* Detects user mental states such as:

  * Anxious
  * Stressed
  * Sad
  * Overwhelmed
  * Positive
  * Neutral

The detected state is used internally to personalize responses.

### 📚 Retrieval-Augmented Generation (RAG)

* Reads and processes mental wellness PDFs.
* Creates embeddings using Sentence Transformers.
* Stores embeddings in a FAISS vector database.
* Retrieves relevant information before generating responses.

### 📝 Personalized Memory

The chatbot remembers important user information such as:

* Upcoming exams
* Sleep issues
* Stress triggers
* Personal concerns

This helps the assistant provide more personalized and context-aware responses.

### 📈 Mood Tracking

Every conversation stores:

* Timestamp
* User message
* Detected mental state

This allows future analysis of mood patterns.

### 🚨 Crisis Detection

The assistant detects potentially harmful messages related to self-harm or suicidal thoughts and immediately displays emergency support information.

### 🔒 Fully Local AI

The entire application runs locally using:

* Ollama
* Qwen 2.5 3B Model

No external APIs or paid AI services are required.

---

## 🌟 Project Highlights

- Local AI assistant powered by Qwen 2.5 3B
- Retrieval-Augmented Generation (RAG)
- Mental state detection and personalized memory
- Crisis detection and safety features
- Fully offline and privacy-friendly

  
# 🏗️ System Architecture

```text
User
 ↓
Streamlit Interface
 ↓
Crisis Detection
 ↓
Mental State Detection
 ↓
Personalized Memory
 ↓
RAG Retriever
 ↓
FAISS Vector Database
 ↓
Qwen 2.5 (Local SLM)
 ↓
Response Generation
```

---

# 🛠️ Technologies Used

### Programming Language

* Python 3.13

### AI & NLP

* Ollama
* Qwen 2.5 3B
* Sentence Transformers
* Transformers

### RAG Components

* FAISS
* PyPDF

### Frontend

* Streamlit

### Database

* SQLite

### Libraries

* Requests
* NumPy
* Pandas

---

# 📂 Project Structure

```text
MindMate-AI
│
├── app.py
│
├── data
│   └── documents
│
├── models
│   ├── llm.py
│   ├── mental_state_detector.py
│   ├── crisis_detector.py
│   └── memory_extractor.py
│
├── rag
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── setup_rag.py
│   └── rag_pipeline.py
│
├── database
│   ├── mood_tracker.py
│   ├── memory.py
│   └── mood.db
│
├── utils
│   └── prompts.py
│
└── venv
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd MindMate-AI
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama:

https://ollama.com

---

## 5. Pull Qwen Model

```bash
ollama pull qwen2.5:3b
```

---

## 6. Add Knowledge Base PDFs

Place your PDFs inside:

```text
data/documents/
```

Example:

```text
exam_stress.pdf
sleep_hygiene.pdf
anxiety_management.pdf
mindfulness.pdf
```

---

## 7. Run the Application

```bash
streamlit run app.py
```

---

# 💡 Example Conversations

### User

```text
I have exams next week.
```

### Assistant

```text
It sounds like exams are on your mind right now. How are you feeling about them?
```

---

### User

```text
I'm stressed.
```

### Assistant

```text
I'm sorry you're feeling stressed. You mentioned earlier that your exams are coming up. Is that contributing to your stress?
```

---

# 🎯 Project Objectives

* Build an AI assistant that can provide supportive conversations.
* Explore the practical use of RAG and local language models.
* Demonstrate NLP techniques such as mental state detection and memory.
* Create a privacy-friendly assistant that runs entirely on local hardware.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Local LLM Deployment
* Natural Language Processing
* Streamlit Application Development
* SQLite Integration
* AI System Design

---

# 👨‍💻 Author

**Srudhan Varma Eerla**

M.Tech in Computer Science and Engineering (Big Data Analytics)
