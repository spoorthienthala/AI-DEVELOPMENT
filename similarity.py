from sentence_transformers import util,SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
sentences=[
    "I love playing khabaddi",
    "I enjoying playing soccer",
    "i like eating momos"
]
sentence_embedding=model.encode(sentences)
print(sentence_embedding[0])
similarity1=util.cos_sim(sentence_embedding[0],sentence_embedding[2])
print(similarity1.item())

