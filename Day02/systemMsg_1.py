import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "Give answers in 2 lines only."
        },
        {
            "role": "user",
            "content": "You are a Python teacher. Give the definition of AI."
        }
    ]
)

print(response["message"]["content"])