```python
# Define utility functions

import logging

def setup_logging():
    """Setup logging"""
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging setup')

def handle_error(error):
    """Handle errors"""
    logging.error(error)
    return jsonify({'error': str(error)}), 500
```

###