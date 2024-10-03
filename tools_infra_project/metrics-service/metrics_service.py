import logging
from fluent import handler

logger = logging.getLogger('metrics_service')
logger.setLevel(logging.INFO)

fluent_handler = handler.FluentHandler('fluentd.test', host='localhost', port=24224)
logger.addHandler(fluent_handler)

@app.route('/metrics')
def metrics():
    logger.info('Metrics request received')
    return generate_latest()
