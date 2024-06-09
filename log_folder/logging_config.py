import logging

logger = None  # Global variable to hold the logger instance

def get_logger():
    global logger
    if logger is None:
        # Create a logger
        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.DEBUG)

        # Create a file handler
        with open('app.log', 'w') as f:
            pass
        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger