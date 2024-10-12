import requests
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

print(GEMINI_API_KEY)

HEADERS = {
    "Authorization": GEMINI_API_KEY,  
    "Content-Type": "application/json",
}

data_that_can_be_asked = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''). "
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_gemini_api(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = data_that_can_be_asked.format(dom_content=chunk, parse_description=parse_description)

        response = requests.post(GEMINI_API_URL, headers=HEADERS, json={"contents": [{"parts": [{"text": prompt}]}]})

        if response.status_code == 200:
            result = response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            parsed_results.append(result)
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    return "\n".join(parsed_results)

