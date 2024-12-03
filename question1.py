import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define constants
API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = os.getenv("API_TOKEN")

def generate_text(input_prompt, max_new_tokens=50, temperature=0.8):
    """
    Generate text using the Hugging Face Inference API with GPT-2.

    Parameters:
        input_prompt (str): The input text prompt.
        max_new_tokens (int): The maximum number of new tokens to generate.
        temperature (float): Sampling temperature for text generation.

    Returns:
        str: The generated text, trimmed to the last complete sentence.
    """
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs": input_prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
        },
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        generated_data = response.json()
        full_text = generated_data[0].get("generated_text", "").strip()

        # Trim to the last complete sentence
        if "." in full_text:
            sentences = full_text.split(".")
            return ".".join(sentences[:-1]) + "." if len(sentences) > 1 else full_text
        return full_text
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")


if __name__ == "__main__":
    # Example usage
    input_prompt = "Life is a box of"
    try:
        generated_text = generate_text(input_prompt, max_new_tokens=50, temperature=0.8)
        print(f"Input: {input_prompt}")
        print(f"Generated Text: {generated_text}")
    except Exception as e:
        print(f"An error occurred: {e}")
