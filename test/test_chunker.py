from services.chunker import TextChunker

chunker = TextChunker(chunk_size=100, overlap=20)

sample_text = """
Artificial Intelligence is transforming the world.
""" * 300

chunks = chunker.chunk(sample_text)

print("=" * 60)
print(f"Total Chunks : {len(chunks)}")
print("=" * 60)

for i, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk[:200])
