# Hugging Face GPT-2 Text Generation

This project demonstrates how to use the Hugging Face Inference API with the GPT-2 model for text generation and includes a word frequency analysis tool.

## Features
- Generate text using the GPT-2 model.
- Analyze word frequencies from a text file.
- Adjustable parameters for customization.

## Requirements
- Python 3.7 or later
- `requests` library
- (Optional) Virtual environment

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set up a virtual environment (optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get a Hugging Face API key for text generation**:
   - Sign up at [Hugging Face](https://huggingface.co/).
   - Generate an API token in your account settings.
   - Add the token to the `API_KEY` variable in `question1.py`.

## Usage
### 1. Text Generation (`question1.py`)
1. Modify the input prompt in `question1.py` (`input_prompt` variable).
2. Run the script:
   ```bash
   python question1.py
   ```
3. Example output:
   ```
   Input: Life is a box of
   Generated Text: Life is a box of chocolates that are given to people in various stages of their illness...
   ```

### 2. Word Frequency Analysis (`question2.py`)
1. Update the URL in `question2.py` to point to the text file you want to analyze.
2. Run the script:
   ```bash
   python question2.py
   ```
3. Example output:
   ```
   Words ranked from 10th to 20th by frequency:
   word1: 42
   word2: 38
   ...
   ```

## Parameters
### Text Generation
- `max_new_tokens`: Maximum length of generated text (default: 50).
- `num_return_sequences`: Number of results to return (default: 1).
- `temperature`: Controls creativity of output (default: 0.8).

### Word Frequency Analysis
- `Input URL`: Location of the text file.
- `Rank Range`: Words ranked by frequency (default: 10th to 20th).

## License
This project is available under the MIT License.

## Credits
- Hugging Face for the GPT-2 model and API.
- Python for the tools and libraries.
