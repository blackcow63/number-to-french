# number-to-french
A repository containing a packaged application meant to convert numbers to words for them in French

## Features

- Convert individual numbers (e.g., 345 to "trois cent quarante-cinq").
- Handle lists of numbers (e.g., [2, 3, 4] to ["deux", "trois", "quatre"]).
- Works for numbers up to 9,999,999.

## Usage

To use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project directory:
    ```bash
    cd ../number-to-french

3. Run the Python script to convert numbers:
    python -m number_to_french <list_of_numbers>

## Disclaimer about LLM usage
1. I have Copilot installed on my PC, so after I created a structure of the algorithm in converter.py, I could let Copilot fill the methods.
2. To create README file, I prompted ChatGPT: create a README file for a packaged application containing this script [contents of number_to_french/converter.py]. I did an analogous thing for setup.py adn tests/tests_converter.py.