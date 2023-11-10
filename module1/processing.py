# processing.py

# Function to retrieve comments from a Reddit post
def retrieve_comments(post):
    comment_list = []
    
    # Access the comments and load all comments
    post.comments.replace_more(limit=5)  # This loads all the comments
    comments = post.comments.list()
    
    # Append comments to the comment_list
    for comment in comments:
        output = comment.body
        comment_list.append(output)
    
    return comment_list

# Function to save comments to a text file
def save_comments_to_file(comment_list, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for comment in comment_list:
            # Write each comment to the file
            file.write(f'{comment}\n')

