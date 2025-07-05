import logging
import os

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
