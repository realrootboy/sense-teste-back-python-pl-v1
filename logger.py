import logging


def setup_logger():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)