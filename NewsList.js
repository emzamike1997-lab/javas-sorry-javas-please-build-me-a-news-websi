```javascript
import React from 'react';

function NewsList({ news }) {
    return (
        <ul className="news-list">
            {news.map((item) => (
                <li key={item.id}>
                    <h2 className="news-title">{item.title}</h2>
                    <p className="news-description">{item.description}</p>
                </li>
            ))}
        </ul>
    );
}

export default NewsList;
```

###