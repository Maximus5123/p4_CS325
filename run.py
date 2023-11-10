# run.py
# Import necessary modules
import os
import sys
from module2.api import get_reddit_post  # Import a function for getting a Reddit post
from module1.processing import retrieve_comments, save_comments_to_file  # Import functions for processing and saving comments
from module3.process3 import process_data, save_processed_data  # Import functions for processing and saving processed data

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Check if the command-line arguments include a URL
    if len(sys.argv) < 2:
        print("Usage: python3 run.py URL")
        sys.exit(1)

    # Get the Reddit post URL from the command-line arguments
    post_url = sys.argv[1]

    # Define Reddit API credentials
    client_id = '4iuS6Vi6nMblW8NXKFudrQ'
    client_secret = '4kkKBJ4_rkD4Bh6ijoiAqQd1MPoTYQ'
    user_agent = 'Maximus<red>'

    # Get the Reddit post data using the specified URL and API credentials
    post = get_reddit_post(post_url, client_id, client_secret, user_agent)

    # Retrieve comments from the Reddit post
    comments = retrieve_comments(post)

    # Process the retrieved comments
    processed_data = process_data(comments)

    # Define the output directory and file path
    output_dir = os.path.join("Data", "processed")
    output_file = os.path.join(output_dir, "processed_data.txt")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the processed data to a text file
    save_processed_data(processed_data, output_file)

    # Print a message indicating where the processed data was saved
    print("Processed data saved to", output_file)

