
unique_words = set()

while True:
    
    word = input("Enter a word (or a duplicate word to end): ").strip().lower()
    
    
    if word in unique_words:
        print(f"\nDuplicate word found: '{word}'")
        print(f"Number of unique words: {len(unique_words)}")
        print("Unique words:", ", ".join(unique_words))
        break
    
    
    unique_words.add(word)
    print(f"Added: '{word}'")