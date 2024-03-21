import logging


def create_logger():
    """
    Set the level of this logger.

    DEBUG: Detailed information, typically of interest only when diagnosing problems.
    INFO: Confirmation that things are working as expected.
    WARNING: An indication that something unexpected happened, or may happen soon
    (e.g. disk space low). The software is still working as expected.
    ERROR: More serious problem that prevented the software from performing a function.
    CRITICAL: A very serious error that may prevent the program from continuing to run.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("x.log")
    # Create formatters and add it to handlers
    c_format = logging.Formatter(
        "%(asctime)s - [%(levelname)s] -  %(name)s "
        "- (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(file_handler)
    return logger


if __name__ == "__main__":
    # Usage
    logger = create_logger("myLogger")
    logger.info("This is an info message")
