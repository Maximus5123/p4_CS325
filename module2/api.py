# modules/reddit_api.py

# Import the 'praw' module, which is used to interact with the Reddit API
import praw

# Function to get a Reddit post by URL
def get_reddit_post(url, client_id, client_secret, user_agent):
    # Create a Reddit instance with the provided credentials and user agent
    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)
    
    # Fetch the Reddit submission (post) using the specified URL
    post = reddit.submission(url=url)
    
    # Return the retrieved post
    return post
