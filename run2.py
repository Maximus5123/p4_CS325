import openai
import os
import time

# Set your OpenAI API key
api_key = "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"

# Define a function to analyze the sentiment of a comment
def analyze_sentiments(comments):
    sentiments = []
    for comment in comments:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Analyze the sentiment of the following comment: '{comment}'",
                max_tokens=50,
                api_key=api_key
            )
            sentiment = response.choices[0].text.strip()
            sentiments.append((comment, sentiment))
        except openai.error.RateLimitError:
            print("Exceeded rate limit. Pausing for a minute before continuing.")
            time.sleep(60)  # Wait for 60 seconds (adjust as needed)
    return sentiments
    # Extract the sentiment from the API response
    sentiment = response.choices[0].text.strip()

    return sentiment

# Provide the full path to your input file
file_path = r"C:\Users\Iammu\OneDrive\Desktop\websrap3\Data\CS325_p3\Data\processed\processed_data.txt"

# Output file path
output_file_path = r"C:\Users\Iammu\OneDrive\Desktop\websrap3\Data\CS325_p3\Data\processed\sentiment_analysis.txt"

# Now you can open and read the file with the 'utf-8' encoding
with open(file_path, "r", encoding="utf-8") as file:
    comments = file.read().splitlines()

# Analyze the sentiment of each comment and save the results to an output file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for i in range(0, len(comments), 3):
        comment_group = comments[i:i+3]
        results = analyze_sentiments(comment_group)
        for result in results:
            output_file.write(f"Comment: {result[0]}\n")
            output_file.write(f"Sentiment: {result[1]}\n\n")
            output_file.flush()  # Ensure writing to the file
        time.sleep(60)  # Wait for a minute between groups of comments


