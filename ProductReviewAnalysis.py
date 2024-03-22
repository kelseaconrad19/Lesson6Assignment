# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase, so they stand out.
# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
def review_tally(list_of_reviews, pos_list, neg_list):
    pos_words = [wd.lower() for wd in pos_list]
    neg_words = [wd.lower() for wd in neg_list]

    review_counts = []

    for r in list_of_reviews:
        pos_count = 0
        neg_count = 0
        words_in_review = r.lower().split()

        for wd in words_in_review:
            if wd in pos_words:
                pos_count += 1
            elif wd in neg_words:
                neg_count += 1

        review_counts.append((pos_count, neg_count))

        pos_count += 1

    return review_counts


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
words = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for word in words:
        if word in review:
            beginning = review.find(word)
            end = beginning + len(word) + 1
            w = review[beginning:end]
            revised_word = w.upper()
            final_review = review.replace(w, revised_word)
            tally = review_tally(reviews, positive_words, negative_words)
            print(f"{final_review} {tally}")
