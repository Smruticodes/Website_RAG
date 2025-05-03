### **Q\&A Web Scraping System**

This project enables users to scrape a website and perform question-and-answer (Q\&A) tasks based on the content of the scraped website. The backend is powered by Python and Node.js, while the frontend is created using React.js. The Q\&A functionality is powered by LangChain, OpenAI embeddings, and FAISS for document-based searches.

**Key Features:**

1. **Web Scraping**: It allows users to scrape websites and gather text content and images. This data is then used for answering questions.
2. **Question Answering**: Once the data is scraped, users can ask questions related to the content of the website, and the system will find the most relevant documents and provide an answer using the LangChain Q\&A pipeline.
3. **Frontend**: A simple and clean UI built using React.js that allows users to ask questions after scraping a website.
4. **Backend**: Combines Node.js (for API server) and Python (for Q\&A and web scraping). Python handles document processing, embedding, and Q\&A tasks.

### **Folder Structure**

Here’s how the project is organized:

```
Website_QnA
├── backend/
│   ├── .env               # Environment variables (API keys)
│   ├── occams.txt         # Example document used for Q&A
│   ├── package.json       # Backend dependencies
│   ├── qa_system.py       # Python script that processes queries
│   ├── scraper.py         # Python script to scrape websites
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── node_modules/      # Node.js dependencies
│   ├── public/
│   ├── src/
│   │   ├── App.css        # CSS for the frontend
│   │   ├── App.js         # Main React component
│   │   ├── ScrapePage.js  # Component for scraping a website
│   │   └── QAPage.js      # Component for asking questions
│   ├── package.json       # Frontend dependencies
│   └── README.md          # Readme for frontend setup and instructions
├── .gitignore             # Files and folders to ignore in Git
├── README.md              # Main Readme for the whole project
└── package-lock.json      # Backend package lock
```

### **Processes to Run**

To get this system up and running, follow these steps:

#### 1. **Set Up the Backend (Python and Node.js)**

1. **Navigate to the `backend` directory**:

   ```bash
   cd backend
   ```

2. **Create a Python Virtual Environment** (if not already created):

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On MacOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file** in the `backend/` folder and add your OpenAI API key:

   ```text
   OPENAI_API_KEY=your_openai_api_key
   ```

6. **Run the Node.js server** for API:

   ```bash
   node app.js
   ```

   This will start the server at `http://localhost:3001`.

#### 2. **Set Up the Frontend (React)**

1. **Navigate to the `frontend` directory**:

   ```bash
   cd frontend
   ```

2. **Install frontend dependencies**:

   ```bash
   npm install
   ```

3. **Run the React development server**:

   ```bash
   npm start
   ```

   This will start the React app at `http://localhost:3000`.

#### 3. **Running the System**

1. **Scrape a Website**:

   * Go to the **frontend** at `http://localhost:3000`.
   * Enter a website URL and click **Scrape Website**. This will scrape the content of the website and store the information for further querying.

2. **Ask a Question**:

   * After scraping the website, type your question and click **Submit**. The backend will process the query and provide an answer based on the scraped content.

---

### **Final Notes**

* **Frontend (React)**: The user interface allows users to input website URLs and ask questions after scraping the content.
* **Backend (Node.js and Python)**: Handles both web scraping and Q\&A functionality. The Python scripts handle document processing, embeddings, and question-answering, while Node.js serves as an API server.
* **.env File**: This file holds your API keys (such as OpenAI and SerpAPI) securely.


