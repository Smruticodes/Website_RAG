import React, { useState } from 'react';

function ScrapePage() {
  const [url, setUrl] = useState('');
  const [message, setMessage] = useState('');

  const scrapeWebsite = async () => {
    const res = await fetch('http://localhost:3001/scrape', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });

    const data = await res.json();
    setMessage(data.message || 'Scraping failed.');
  };

  return (
    <div>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL to scrape"
      />
      <button onClick={scrapeWebsite}>Start Scraping</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default ScrapePage;
