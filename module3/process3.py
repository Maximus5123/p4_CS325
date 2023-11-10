# processing2.py

# Function to process a list of data
def process_data(data):
    processed_data = []
    for item in data:
        # Process each item and add it to processed_data
        processed_item = item + " Processed"  # You should replace this with your actual processing logic
        processed_data.append(processed_item)
    
    return processed_data

# Function to save processed data to a text file
def save_processed_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            # Write each processed item to the file
            file.write(f'{item}\n')

