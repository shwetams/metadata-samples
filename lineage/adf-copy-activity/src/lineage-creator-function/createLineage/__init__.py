import logging
import json

import azure.functions as func


def main(msg: func.QueueMessage) -> None:
    logging.info('started')
    message = msg.get_body().decode('utf-8')
    logging.info('message decoded: %s', message)
    request = json.loads(message)
