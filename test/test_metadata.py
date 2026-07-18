from services.metadata_store import MetadataStore

store = MetadataStore()

store.add(
    {
        "title": "Attention Is All You Need",
        "page": 1,
        "chunk": 1,
        "source": "attention.pdf",
    }
)

store.add({"title": "BERT", "page": 4, "chunk": 2, "source": "bert.pdf"})

store.save()

print("=" * 50)

print("Stored:", store.size())

print()

print(store.get(0))

print()

print(store.get(1))
