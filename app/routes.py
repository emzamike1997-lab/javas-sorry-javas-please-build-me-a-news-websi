```python
# Define the API routes

from flask import Blueprint, request, jsonify
from app import db
from app.models import NewsArticle
from app.services import NewsService

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route('/news', methods=['GET'])
def get_news():
    """Get all news articles"""
    news_service = NewsService()
    news_articles = news_service.get_all_news()
    return jsonify([article.to_dict() for article in news_articles])

@news_blueprint.route('/news', methods=['POST'])
def create_news():
    """Create a new news article"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    news_service = NewsService()
    news_article = news_service.create_news(data)
    return jsonify(news_article.to_dict()), 201

@news_blueprint.route('/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    """Get a news article by ID"""
    news_service = NewsService()
    news_article = news_service.get_news_by_id(news_id)
    if not news_article:
        return jsonify({'error': 'News article not found'}), 404
    return jsonify(news_article.to_dict())

@news_blueprint.route('/news/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    """Update a news article"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    news_service = NewsService()
    news_article = news_service.update_news(news_id, data)
    if not news_article:
        return jsonify({'error': 'News article not found'}), 404
    return jsonify(news_article.to_dict())

@news_blueprint.route('/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    """Delete a news article"""
    news_service = NewsService()
    news_article = news_service.delete_news(news_id)
    if not news_article:
        return jsonify({'error': 'News article not found'}), 404
    return jsonify({'message': 'News article deleted'})
```

###