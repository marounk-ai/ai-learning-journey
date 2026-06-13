# text_analyzer.py
# Analyze a block of text for word frequency and basic stats
# Week 2 — AI Learning Journey

def analyze_text(text):
    """Return basic statistics about a block of text."""
    
    words = text.lower().split()
    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    
    # Count word frequencies using a dict
    frequency = {}
    for word in words:
        # Strip punctuation from word edges
        clean_word = word.strip(".,!?;:\"'()")
        if clean_word:  # skip empty strings
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    
    # Find top 5 words
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:5]
    
    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentence_count": sentence_count,
        "top_words": top_words,
    }

def main():
    print("Text Analyzer")
    print("-" * 30)
    print("Paste your text below. Enter a blank line when done.")
    print()
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    if not lines:
        print("No text provided.")
        return
    
    text = " ".join(lines)
    stats = analyze_text(text)
    
    print("\n--- Results ---")
    print(f"Words     : {stats['word_count']}")
    print(f"Characters: {stats['char_count']}")
    print(f"Sentences : {stats['sentence_count']}")
    print("\nTop 5 words:")
    for word, count in stats["top_words"]:
        print(f"  {word:<20} {count} times")

if __name__ == "__main__":
    main()