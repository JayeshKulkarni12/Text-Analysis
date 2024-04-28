import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textstat import gunning_fog, syllable_count
import os

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Directory containing extracted text files
extracted_text_directory = "C:/Users/jayes/Desktop/extracted_articles"

# List to store sentiment analysis results
sentiment_results = []

# Function to compute additional parameters
def compute_additional_parameters(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    num_sentences = len(sentences)
    num_words = len(words)
    
    # Average sentence length
    avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0
    
    # Percentage of complex words
    complex_words = [word for word in words if syllable_count(word) > 2]
    percentage_complex_words = (len(complex_words) / num_words) * 100 if num_words > 0 else 0
    
    # Fog index
    fog_index = gunning_fog(text)
    
    # Average number of words per sentence
    avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
    
    # Complex word count
    complex_word_count = len(complex_words)
    
    # Syllable per word
    syllables_per_word = sum(syllable_count(word) for word in words) / num_words if num_words > 0 else 0
    
    # Personal pronouns
    stop_words = set(stopwords.words('english'))
    personal_pronouns = sum(1 for word in words if word.lower() in {'i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'}.difference(stop_words))
    personal_pronouns_ratio = personal_pronouns / num_words if num_words > 0 else 0
    
    # Average word length
    avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0
    
    return avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, num_words, syllables_per_word, personal_pronouns_ratio, avg_word_length

# Iterate through each text file and perform sentiment analysis
for filename in os.listdir(extracted_text_directory):
    if filename.endswith(".txt"):
        # Read text from file
        with open(os.path.join(extracted_text_directory, filename), 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Perform sentiment analysis
        scores = sid.polarity_scores(text)
        
        # Compute additional parameters
        additional_parameters = compute_additional_parameters(text)
        
        # Combine sentiment analysis scores and additional parameters
        result = {
            "Title": filename,
            "Positive Score": scores["pos"],
            "Negative Score": scores["neg"],
            "Polarity Score": scores["compound"],
            "Subjectivity Score": scores["compound"],  # Assuming compound score as subjectivity score
            "Avg Sentence Length": additional_parameters[0],
            "Percentage of Complex Words": additional_parameters[1],
            "Fog Index": additional_parameters[2],
            "Avg Number of Words per Sentence": additional_parameters[3],
            "Complex Word Count": additional_parameters[4],
            "Word Count": additional_parameters[5],
            "Syllable per Word": additional_parameters[6],
            "Personal Pronouns": additional_parameters[7],
            "Avg Word Length": additional_parameters[8]
        }
        
        # Append sentiment analysis results to the list
        sentiment_results.append(result)

# Convert sentiment results to a DataFrame
sentiment_df = pd.DataFrame(sentiment_results)

# Save sentiment analysis results to a CSV file
output_file = "sentiment_analysis_results.xlsx"
sentiment_df.to_excel(output_file, index=False)

print("Sentiment analysis results saved to", output_file)
