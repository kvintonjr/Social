import csv
import os
from datetime import datetime
from newsapi import NewsApiClient
import openai

# --- API Keys ---
# IMPORTANT: In a real application, you should not hardcode API keys.
# They should be stored securely, for example, in environment variables.
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


# --- Functions ---

def get_top_headline():
    """
    Fetches the top news headline from NewsAPI.org for the US.
    """
    try:
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        top_headlines = newsapi.get_top_headlines(language='en', country='us')

        if top_headlines['status'] == 'ok' and top_headlines['articles']:
            return top_headlines['articles'][0]['title']
        else:
            return "No headlines found"
    except Exception as e:
        print(f"An error occurred while fetching news: {e}")
        return "Error fetching news"

def generate_post(headline):
    """
    Generates a social media post using OpenAI's GPT model.
    """
    if "Error" in headline or "No headlines" in headline:
        return "Could not generate a post due to an issue with fetching the trend."

    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        prompt = f"Write a short, engaging social media post about the following news headline. Include relevant hashtags. Headline: '{headline}'"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful social media assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred while generating the post: {e}")
        return "Error generating post"

# --- Main script ---

# 1. Get the top trend (headline)
print("Fetching top news headline...")
TREND = get_top_headline()
print(f"Trend found: {TREND}")

# 2. Generate the social media post
print("Generating social media post...")
POST_CONTENT = generate_post(TREND)
print(f"Post generated: {POST_CONTENT}")

# 3. Save to CSV
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CSV_FILE = "posts.csv"
file_exists = os.path.isfile(CSV_FILE)
row = [TREND, POST_CONTENT, TIMESTAMP]
header = ["Trend", "Post", "Timestamp"]

print(f"Saving to {CSV_FILE}...")
with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(header)
    writer.writerow(row)

print("Successfully saved post to CSV.")
