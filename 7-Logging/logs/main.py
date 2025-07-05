from logger import logging

logging.info("Logger initialized from logger.py")

def add(a, b):
    logging.debug("Adding numbers")
    return a + b

result = add(2, 3)
logging.info(f"Result: {result}")
