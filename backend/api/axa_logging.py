import logging as l
import sys

LOG_LEVEL = l.INFO
CONSOLE_LOG_LEVEL = l.ERROR
FILE_LOG_LEVEL = l.DEBUG
LOGGER_NAME = "axa_logger"


def get_axa_logger() -> l.Logger:
    """
    Returns the axa logger instance.
    """
    _logger = l.getLogger(LOGGER_NAME)
    if not _logger.hasHandlers():
        console_handler = l.StreamHandler(sys.stdout)
        console_handler.setLevel(CONSOLE_LOG_LEVEL)
        console_formatter = l.Formatter(
            "%(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        _logger.addHandler(console_handler)

        file_handler = l.FileHandler("axa.log")
        file_handler.setLevel(FILE_LOG_LEVEL)
        file_formatter = l.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)
    _logger.setLevel(LOG_LEVEL)
    _logger.propagate = False
    return _logger
