import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "create a resume"
        }
    ]
)

print(response["message"]["content"])