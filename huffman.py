import heapq
from collections import defaultdict, Counter

def generate_huffman_codes(text: str) -> tuple[dict[str, str], dict[str, int]]:
    """
    Generates Huffman codes for the characters in the input text using a greedy approach.
    Returns a tuple of (character to Huffman code dictionary, character frequency dictionary).
    """
    if not text:
        return {}, {}

    # Step 1: Count character frequencies
    frequency = Counter(text)

    # Step 2: Build a priority queue (min-heap) of (freq, char/tree)
    # heap = [[freq, [char, ""]] for char, freq in frequency.items()]
    heap = []
    for char, freq in frequency.items():
        node = [freq, [char, ""]]
        heap.append(node)
    heapq.heapify(heap)

    # Step 3: Merge nodes until one remains (Huffman tree)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Step 4: Extract the final codes
    huffman_codes = {}
    for char, code in heap[0][1:]:
        huffman_codes[char] = code

    return huffman_codes,frequency

text = "hello"
codes, freqs = generate_huffman_codes(text)

print("Frequencies:", freqs)
print("Huffman Codes:", codes)
