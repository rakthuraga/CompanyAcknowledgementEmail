from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.files.create(
  file=open("mydataFixed.jsonl", "rb"),
  purpose="fine-tune"
)

# Print the response to check if the upload was successful
print("Upload successful!")
print("File ID:", response.id)
print("Filename:", response.filename)
print("Status:", response.status)