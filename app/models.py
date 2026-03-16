```python
# Define the database models

from app import db
from datetime import datetime

class NewsArticle(db.Model):
    """News article model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'NewsArticle({self.title}, {self.content})'

    def to_dict(self):
        """Convert the news article to a dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
        }
```

###