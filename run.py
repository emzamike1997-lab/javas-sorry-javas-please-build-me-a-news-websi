```python
# Run the Flask application

from app import create_app
from app.utils import setup_logging

if __name__ == '__main__':
    setup_logging()
    app = create_app()
    app.run(debug=True)
```

###