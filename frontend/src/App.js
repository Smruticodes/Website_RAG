import React, { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");  // State for storing user query
  const [answer, setAnswer] = useState(""); // State for storing the answer
  const [loading, setLoading] = useState(false);  // Loading state

  // Function to handle the form submission
  const askQuestion = async () => {
    setLoading(true);
    setAnswer("");  // Clear previous answer
    try {
      const response = await fetch("http://localhost:3001/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      if (!response.ok) {
        throw new Error("Error fetching the answer");
      }

      const data = await response.json();
      setAnswer(data.answer || "No answer found.");
    } catch (error) {
      console.error("Error:", error);
      setAnswer("Failed to fetch answer.");
    }
    setLoading(false);  // Set loading to false after getting the response
  };

  return (
    <div className="container">
      <h1 className="title">Occams Advisory Q&A</h1>
      <div className="query-container">
        <textarea
          className="query-input"
          placeholder="Ask a question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="submit-btn" onClick={askQuestion} disabled={loading}>
          {loading ? "Processing..." : "Submit"}
        </button>
      </div>
      <div className="response-container">
        {loading ? (
          <div className="loading">Loading...</div>
        ) : (
          <p className="response">{answer}</p>
        )}
      </div>
    </div>
  );
}

export default App;
