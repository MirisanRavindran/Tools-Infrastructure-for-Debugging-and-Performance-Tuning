import logging
from fluent import handler

# Set up Fluentd logging
logger = logging.getLogger('api_service')
logger.setLevel(logging.INFO)

# Use 'host.docker.internal' to ensure proper connection to Fluentd inside Docker
fluent_handler = handler.FluentHandler('fluentd.test', host='host.docker.internal', port=24224)
logger.addHandler(fluent_handler)

# Example route that generates a log
@app.route('/')
def hello():
    logger.info('Request received at /')  # Log that should be sent to Fluentd
    return "Hello from API service!"
