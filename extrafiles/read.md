# Project 3: Reddit Comment Scraper

This project is designed to scrape and process comments from a specific Reddit post using the PRAW (Python Reddit API Wrapper) library. The project is structured to follow best practices for code organization and modularity.

## Project Structure

The project consists of the following components:

- `modules/` directory: Contains Python modules for different functionalities.
    - `reddit_api.py`: Module for interacting with the Reddit API.
    - `comment_processing.py`: Module for processing comments.
    - `__init__.py`: Empty file to indicate that the directory is a Python package.

- `run.py`: The main Python script that coordinates the execution of the project. It takes a Reddit post URL as a command-line argument and uses the modules to retrieve and process comments.

- `Data/` directory: Contains subdirectories for raw and processed data.
    - `raw/`: Stores the unprocessed or raw data.
    - `processed/`: Stores the processed comment data.

## Usage

To use this project, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this GitHub repository to your local machine.

3. Navigate to the project directory:


4. Run the main script `run.py` with a valid Reddit post URL as a command-line argument. Replace `https://www.reddit.com/r/movies/comments/155ag1m/official_discussion_oppenheimer_spoilers/


5. The script will retrieve comments from the Reddit post and save them to the `Data/processed/` directory as a text file.

## Dependencies

This project relies on the following Python libraries:

- `praw`: The Python Reddit API Wrapper. You can install it using pip:

