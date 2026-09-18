import logging
import os
from datetime import datetime

def get_logger(name):
    # logs folder banayein agar exist nahi karta
    os.makedirs("logs", exist_ok=True)

    # har run ki alag log file (timestamp k sath)
    log_filename = f"logs/test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Agar handlers already add hain toh dobara add na karein (duplicate logs se bachne k liye)
    if not logger.handlers:
        # File mein likhne wala handler
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)

        # Console pe bhi dikhane wala handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger