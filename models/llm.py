import requests


def generate_response(conversation):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": conversation,
            "stream": False
        }
    )

    result = response.json()
    print("\n=== OLLAMA RESPONSE ===")
    print(result)
    return result.get("response", "")