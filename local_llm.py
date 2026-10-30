
import csv
from pathlib import Path
from datetime import datetime
from ollama import chat

# Project folders
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"

PROMPTS_FILE = DATASET_DIR / "prompts.csv"
RESPONSES_FILE = DATASET_DIR / "llm_responses.csv"
HISTORY_FILE = DATASET_DIR / "conversation_history.txt"

# Local LLM model
MODEL_NAME = "llama3.2"


def generate_response(prompt):
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content


def main():
    if not PROMPTS_FILE.exists():
        print("Error: prompts.csv was not found.")
        return

    with open(
        PROMPTS_FILE, "r", newline="", encoding="utf-8"
    ) as file:
        prompts = list(csv.DictReader(file))

    results = []

    with open(
        HISTORY_FILE, "w", encoding="utf-8"
    ) as history:

        history.write("WEEK 8 - LOCAL LLM CONVERSATION HISTORY\n")
        history.write(f"Model: {MODEL_NAME}\n")
        history.write(f"Date: {datetime.now()}\n")
        history.write("=" * 60 + "\n\n")

        for item in prompts:
            prompt_id = item["prompt_id"]
            domain = item["domain"]
            prompt = item["prompt"]

            print(f"\nProcessing {prompt_id}: {domain}")

            try:
                answer = generate_response(prompt)

                word_count = len(answer.split())

                results.append({
                    "prompt_id": prompt_id,
                    "domain": domain,
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "response": answer,
                    "response_word_count": word_count,
                    "status": "Success"
                })

                history.write(f"Prompt ID: {prompt_id}\n")
                history.write(f"Domain: {domain}\n")
                history.write(f"Prompt: {prompt}\n")
                history.write(f"Response:\n{answer}\n")
                history.write("-" * 60 + "\n\n")

                print(answer)
                print(f"Response word count: {word_count}")

            except Exception as error:
                print(f"Error: {error}")

                results.append({
                    "prompt_id": prompt_id,
                    "domain": domain,
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "response": "",
                    "response_word_count": 0,
                    "status": f"Error: {error}"
                })

    fieldnames = [
        "prompt_id",
        "domain",
        "model",
        "prompt",
        "response",
        "response_word_count",
        "status"
    ]

    with open(
        RESPONSES_FILE, "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nProject execution completed.")
    print(f"Responses saved to: {RESPONSES_FILE}")
    print(f"History saved to: {HISTORY_FILE}")


if __name__ == "__main__":
    main()
