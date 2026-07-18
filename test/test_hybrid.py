from services.bm25_search import BM25Search
from services.hybrid_search import HybridSearch


class DummySemanticSearch:

    def search(self, query, top_k=5):

        return [(0, 0.95), (2, 0.82), (4, 0.75)]


documents = [
    "YOLO is an object detector.",
    "Transformers use self attention.",
    "Large Language Models.",
    "BERT language model.",
    "Deep Learning networks.",
]

semantic = DummySearchManager.get_search()

bm25 = BM25Search(documents)

hybrid = HybridSearch(semantic, bm25)

results = hybrid.search("transformers")

print("=" * 60)

for index, score in results:

    print(f"{index} -> {score:.3f}")
