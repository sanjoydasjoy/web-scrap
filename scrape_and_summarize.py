import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Headers to simulate a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
}


def get_headlines():
    """Scrape top article links from Hacker News."""
    url = "https://news.ycombinator.com/"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.select(".titleline > a")
        articles = []
        for link in links[:10]:
            title = link.get_text(strip=True)
            href = link.get('href')
            articles.append({'title': title, 'url': href})
        return articles
    except Exception as e:
        print(f"Error fetching headlines: {e}")
        return []


def get_article_text(url):
    """Try to extract main text from article page."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')

        paragraphs = soup.find_all('div', class_='article-content')
        if paragraphs:
            text = ' '.join(p.get_text(strip=True) for p in paragraphs)
        else:
            text = ' '.join(p.get_text(strip=True) for p in soup.find_all('p'))
        return text.strip()
    except Exception as e:
        print(f"Error fetching article {url}: {e}")
        return None


def summarize_text(text):
    """Summarize using Groq's LLaMA3-8B model."""
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize the following news article in 3 concise bullet points:\n{text[:3500]}"
                }
            ],
            "temperature": 0.5,
            "max_tokens": 300,
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"Error summarizing article with Groq: {e}")
        return None


def main():
    articles = get_headlines()
    print(f"Found {len(articles)} articles")
    for article in articles:
        print(f"\n🔹 Title: {article['title']}")
        print(f"🔗 Link: {article['url']}")
        text = get_article_text(article['url'])
        print(f"📄 Fetched article text length: {len(text) if text else 'None'}")

        if not text or len(text) < 200:
            print("[!] Skipping: Article too short or content not extracted.")
            continue

        summary = summarize_text(text)
        if summary:
            print("📌 Summary:")
            print(summary)
        else:
            print("[!] Skipping: Could not generate summary.")
        time.sleep(1)


if __name__ == "__main__":
    main()
