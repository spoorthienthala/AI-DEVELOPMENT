import ollama
msgs=[]
while True:
    question=input("You: ")
    if question.lower()=="exit":
        break
    msgs.append({
        "role":"user",
        "content":question
    })
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    answer=response["message"]["content"]
    msgs.append({
        "role":"assistant",
        "content":answer
    })
    print("-----chat History------\n")
    for msg in msgs:
        print(msg["role"],":",msg["content"])