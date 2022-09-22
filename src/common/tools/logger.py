import logging
import socket
from logging.handlers import SysLogHandler


def papertrail_logging(address: tuple, app_name='MY_APP', date_format='%b %d %H:%M:%S'):
    """
    Función para loggear usando Papertrail.
    """
    class ContextFilter(logging.Filter):
        hostname = socket.gethostname()

        def filter(self, record):
            record.hostname = ContextFilter.hostname
            return True

    syslog = SysLogHandler(address=address)
    syslog.addFilter(ContextFilter())
    format_str = f'%(asctime)s %(hostname)s {app_name}: [%(levelname)s] %(message)s'
    formatter = logging.Formatter(format_str, datefmt=date_format)
    syslog.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(syslog)
    logger.setLevel(logging.INFO)

    return logger
