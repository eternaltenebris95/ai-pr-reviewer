import sys
import os
from openai import OpenAI

# Load the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=api_key)


def review_code(diff):
    prompt = (
        "You are a senior software engineer. "
        "Review the following Git diff and provide constructive feedback, "
        "including possible bugs, security issues, readability suggestions, "
        "and improvement ideas.\n\n"
        f"{diff}"
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    diff = sys.stdin.read()
    review = review_code(diff)
    print(review)
