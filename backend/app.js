const express = require('express');
const { exec } = require('child_process');
const cors = require('cors');

const app = express();
const port = 3001;

app.use(cors());  // Enable CORS to allow frontend to access backend
app.use(express.json());  // Middleware to parse JSON requests

// Scrape Website API (Optional, if needed)
app.post('/scrape', (req, res) => {
  const { url } = req.body;
  exec(`python3 backend/scraper.py "${url}"`, (err, stdout, stderr) => {
    if (err) {
      console.error(`Error executing scraper script: ${stderr}`);
      return res.status(500).json({ error: 'Failed to scrape website.' });
    }
    console.log(stdout);
    res.status(200).json({ message: 'Scraping successful!' });
  });
});

// Q&A API to handle queries
app.post('/query', (req, res) => {
  const { query } = req.body;

  // Correct path to Python and the Python script
  exec(`C:/Python312/python.exe C:/Users/papun/OneDrive/Desktop/Website_QnA/backend/qa_system.py "${query}"`, (err, stdout, stderr) => {
    if (err) {
      console.error(`Error executing QA script: ${stderr}`);
      return res.status(500).json({ error: 'Failed to process query.' });
    }
    res.status(200).json({ answer: stdout.trim() });
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
