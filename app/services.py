```python
# Define the business logic services

from app import db
from app.models import NewsArticle

class NewsService:
    """News service class"""
    def get_all_news(self):
        """Get all news articles"""
        return NewsArticle.query.all()

    def create_news(self, data):
        """Create a new news article"""
        news_article = NewsArticle(title=data['title'], content=data['content'])
        db.session.add(news_article)
        db.session.commit()
        return news_article

    def get_news_by_id(self, news_id):
        """Get a news article by ID"""
        return NewsArticle.query.get(news_id)

    def update_news(self, news_id, data):
        """Update a news article"""
        news_article = NewsArticle.query.get(news_id)
        if news_article:
            news_article.title = data['title']
            news_article.content = data['content']
            db.session.commit()
        return news_article

    def delete_news(self, news_id):
        """Delete a news article"""
        news_article = NewsArticle.query.get(news_id)
        if news_article:
            db.session.delete(news_article)
            db.session.commit()
        return news_article
```

###