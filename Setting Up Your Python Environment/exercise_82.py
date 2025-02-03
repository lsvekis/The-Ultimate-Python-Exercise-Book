# Save as logging_example.py:
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logging.info("This is an info message.")
logging.warning("This is a warning message.")
