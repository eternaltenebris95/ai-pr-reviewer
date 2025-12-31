import sys
import openai

# Read OpenAI API key from environment variable
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def review_code(diff):
    prompt = (
        "You are a senior software engineer. "
        "Review the following Git diff and provide constructive feedback, "
        "including possible bugs, security issues, readability suggestions, "
        "and improvement ideas.\n\n"
        f"{diff}"
    )

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    diff = sys.stdin.read()
    review = review_code(diff)
    print(review)
