import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def some_function():
    # Log an informational message
    logger.info("This is an informational message.")

    # Your function implementation
    # ...

if __name__ == "__main__":
    some_function()
