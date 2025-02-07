from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from llama_index.llms.openai import OpenAI

response = OpenAI().complete("Paul Graham is ")
print(response)