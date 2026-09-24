import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":="user",
            "content":"""
1.  cat->animal
2.  rose->plant
3.  dog->animal
4.  mango->?
            """
        }
    ]
)
print(response["message"]["content"])