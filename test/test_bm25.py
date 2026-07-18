from services.bm25_search import BM25Search

documents = [
    "YOLO is an object detection model.",
    "Transformers use self attention.",
    "BERT is a language model.",
    "Large Language Models use transformers.",
    "Deep Learning uses neural networks.",
]

search = BM25Search(documents)

results = search.search("transformers")

print("=" * 60)

for idx, score in results:

    print()

    print(f"Document {idx}")

    print(f"Score : {score:.3f}")

    print(documents[idx])
