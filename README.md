# AI-Powered Social Media Post Generator

This system automatically fetches top news headlines and uses an AI language model (OpenAI's GPT) to generate relevant social media posts. The output is saved to a local `posts.csv` file.

## Features

-   **Trend Research:** Fetches the latest top headlines from the US using the News API.
-   **AI Post Generation:** Uses OpenAI's GPT-3.5-turbo to write a social media post based on the headline.
-   **CSV Output:** Saves the trend, generated post, and a timestamp to a `posts.csv` file.

## Setup

1.  **Prerequisites:** Make sure you have Python 3 installed on your system.

2.  **Install Dependencies:** Clone or download the project, navigate to the project directory in your terminal, and install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Keys:** This project requires two API keys.
    *   **News API:** Get a free API key from [newsapi.org](https://newsapi.org/register).
    *   **OpenAI:** Get an API key from [platform.openai.com](https://platform.openai.com/api-keys).

4.  **Configure the Script:** Open the `run.py` file and replace the placeholder API keys with your actual keys:
    ```python
    # run.py
    NEWS_API_KEY = "YOUR_NEWS_API_KEY"
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    ```
    **Note:** For a real application, it is strongly recommended to use environment variables to keep your API keys secure, rather than hardcoding them in the script.

## How to Use

Once the setup is complete, simply run the script from your terminal:
```bash
python run.py
```
The script will fetch the latest headline, generate a post, and append it to the `posts.csv` file.

## Project Structure

-   `run.py`: The main script that orchestrates the trend fetching and post generation.
-   `requirements.txt`: A list of the Python libraries required for the project.
-   `posts.csv`: The output file where the generated posts are stored.
