# Cache File Language Validator

This script validates cached markdown files by checking if their content matches the expected target language. If any file contains content in a different language, its cache file will be deleted.

## Prerequisites

- Python 3.x
- Google Cloud Translation API credentials
- Required Python packages:
  ```bash
  pip install google-cloud-translate
  ```

## Setup

1. Place your Google Cloud service account key file in the same directory as the script:
   - Name it `.google_service_account_key.json`
   - Or modify the path in the script to match your key file location

## Usage

Run the script from the command line with two required arguments:

```bash
python fix_cache.py <folder_path> <language_code>
```

### Arguments

- `folder_path`: Path to the directory containing the cached markdown files
- `language_code`: Two-letter language code (e.g., 'en' for English, 'es' for Spanish)

### Example

```bash
python fix_cache.py ./cache/markdown es
```

## How It Works

1. The script scans the specified folder for files ending in '-md'
2. For each file, it:
   - Removes non-content elements (YAML front matter, HTML tags, code blocks, etc.)
   - Splits the remaining text into blocks
   - Uses Google Cloud Translation API to detect the language of each block
   - Calculates the percentage of blocks matching the target language
   - Deletes the cache file if less than 100% of the content matches the target language

## Output

The script will print:
- The filename and percentage of content matching the target language
- Confirmation messages for any deleted cache files

Example output:
```bash
# ./cache/markdown/article-md - (es): 85.50%
Deleted cache file: ./cache/markdown/article-md
```

## Notes

- The script ignores various markdown elements to focus on actual content:
  - YAML front matter
  - HTML comments and tags
  - Code blocks
  - Special identifiers starting with "F_" or "M_"
  - Markdown links and images
- Language detection is performed on text blocks rather than the entire file at once
- The script requires valid Google Cloud credentials with access to the Translation API
