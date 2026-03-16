```javascript
import axios from 'axios';

const apiEndpoint = 'https://newsapi.org/v2/everything';

const NewsService = {
    getNews: async () => {
        try {
            const response = await axios.get(apiEndpoint, {
                params: {
                    apiKey: 'YOUR_API_KEY',
                    q: 'news',
                },
            });
            return response.data.articles;
        } catch (error) {
            throw error;
        }
    },
};

export default NewsService;
```

###