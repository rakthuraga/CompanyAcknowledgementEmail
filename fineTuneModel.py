from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.fine_tuning.jobs.create(
  training_file="file-FvDuAaU9H2xvi285hmivQcka", 
  model="gpt-4o-mini-2024-07-18"
)

# Print the response to check if the fine-tuning job was created successfully
print("Fine-tuning job created successfully!")
print("Job ID:", response.id)
print("Model:", response.model)
print("Status:", response.status)
print("Created at:", response.created_at)