import pandas as pd

# Load input data from "Input.xlsx"
input_file = "Input.xlsx"
input_df = pd.read_excel(input_file)

# Load sentiment analysis results from "sentiment_analysis_results.csv"
sentiment_file = "sentiment_analysis_results.xlsx"
sentiment_df = pd.read_excel(sentiment_file)

merged_df =pd.concat([input_df,sentiment_df], axis=1)

# Reorder the columns based on the specified output variables
output_variables = [
    'URL_ID',
    'URL',
    'Positive Score',
    'Negative Score',
    'Polarity Score',
    'Subjectivity Score',
    'Avg Sentence Length',
    'Percentage of Complex Words',
    'Fog Index',
    'Avg Number of Words per Sentence',
    'Complex Word Count',
    'Word Count',
    'Syllable per Word',
    'Personal Pronouns',
    'Avg Word Length'
]
merged_df = merged_df[output_variables]

# Save the merged DataFrame to a new Excel file
output_file = "Output Data Structure.xlsx"
merged_df.to_excel(output_file, index=False)

print("Merged output saved to", output_file)
