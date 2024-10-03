from flask import Flask
from prometheus_client import Summary, start_http_server

app = Flask(__name__)

# Create a metric to track time spent processing requests
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
def hello():
    # Manually observe some time for debugging purposes
    REQUEST_TIME.observe(1.0)  # Increment by 1 second for each request
    return "Hello, this is the performance monitoring tool!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
