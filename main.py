import logging
import genai_manager 

# TODO: Configure logging
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    text = input("Enter your value: ")
    genai_manager.to_markdown(text)
