import React, { useState } from 'react';

function QAPage() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:3001/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });

      if (!res.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await res.json();
      setAnswer(data.answer || 'No answer found.');
    } catch (error) {
      console.error('Error during fetching Q&A:', error);
      setAnswer('Failed to fetch answer.');
    }
    setLoading(false);
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question"
      />
      <button onClick={askQuestion} disabled={loading}>
        {loading ? 'Loading...' : 'Ask'}
      </button>
      {answer && <p>{answer}</p>}
    </div>
  );
}

export default QAPage;
