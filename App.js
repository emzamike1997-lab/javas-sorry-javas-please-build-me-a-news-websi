```javascript
import React, { useState, useEffect } from 'react';
import NewsList from './NewsList';
import NewsService from './NewsService';

function App() {
    const [news, setNews] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchNews = async () => {
            setLoading(true);
            try {
                const data = await NewsService.getNews();
                setNews(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };
        fetchNews();
    }, []);

    return (
        <div className="container">
            <h1>News Website</h1>
            {loading ? (
                <p>Loading...</p>
            ) : error ? (
                <p>Error: {error}</p>
            ) : (
                <NewsList news={news} />
            )}
        </div>
    );
}

export default App;
```

###