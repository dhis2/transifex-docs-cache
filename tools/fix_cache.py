import os
import re
import sys
from google.cloud import translate_v2 as translate

# Set up the Google Cloud Translation client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.google_service_account_key.json'
translate_client = translate.Client()

def detect_language(text):
    result = translate_client.detect_language(text)
    return result['language']

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def remove_ignored_elements(text):
    # Remove header metadata (YAML front matter)
    text = re.sub(r'^---.*?---\s*', '', text, flags=re.DOTALL | re.MULTILINE)
    # Remove text in curly brackets
    text = re.sub(r'\{[^}]*\}', '', text)
    # remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove markdown links and image paths
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    #remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # remove any special words that start with "F_" or "M_"
    text = re.sub(r'\b[F|M]_\w+\b', '', text)
    return text

def split_text_into_blocks(text):
    # Use regular expressions to split text into markdown blocks
    block_pattern = re.compile(r'(\#.*?\n|```.*?```|\n\n+|^[\>\*\+\-\d\.].*?$)', re.DOTALL | re.MULTILINE)
    raw_blocks = block_pattern.split(text)
    # Combine lines to form complete blocks
    cleaned_blocks = []
    current_block = []

    for line in raw_blocks:
        if re.match(r'^\s*$', line):
            if current_block:
                cleaned_blocks.append("\n".join(current_block).strip())
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        cleaned_blocks.append("\n".join(current_block).strip())

    # Remove empty blocks or blocks that only contain symbols (e.g. #, *, -, >)
    cleaned_blocks = [block for block in cleaned_blocks if re.search(r'\w', block)]
    cleaned_blocks = [block for block in cleaned_blocks if not re.match(r'^[\>\*\+\-\d\.#].*$', block)]

    return cleaned_blocks

def calculate_language_percentage(file_path, target_language):
    text = read_file(file_path)
    text = remove_ignored_elements(text)
    blocks = split_text_into_blocks(text)
    total_blocks = len(blocks)
    if total_blocks == 0:
        return 0
    # check only the first two characters of the detected language code
    target_language_blocks = sum(1 for block in blocks if detect_language(block)[:2] == target_language)

    # for debug purposes list the blocks that are not in the target language
    if 0:
        for block in blocks:
            if detect_language(block)[:2] != target_language:
                print(f"Block in {detect_language(block)}: {block}")

    percentage = (target_language_blocks / total_blocks) * 100
    return percentage

def main(folder_path, target_language):
    # Get all .md files in the specified folder
    md_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('-md')]
    
    for md_file in md_files:
        percentage = calculate_language_percentage(md_file, target_language)
        print(f"# {md_file} - ({target_language}): {percentage:.2f}%")
        # if the percentage of the target language is less than 100% then delete the cache file
        if percentage < 100:
            if os.path.exists(md_file):
                os.remove(md_file)
                print(f"Deleted cache file: {md_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path> <language_code>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    target_language = sys.argv[2]

    if not os.path.isdir(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        sys.exit(1)
    
    main(folder_path, target_language)