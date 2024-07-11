import pathlib
import textwrap
from config import GOOGLE_API_KEY
import main
# Used to securely store your API key
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import pandas as pd

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')



# Extract text


def to_markdown(text):
    response = model.generate_content(text)
    
    # df = pd.json_normalize(response, record_path=['candidates', 'content', 'parts'])
    # Extract the "text" value
    # text_value = df.at[0, 'text']
    print(response.text)