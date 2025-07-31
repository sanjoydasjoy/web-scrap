Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Ran tool
Read file: scrape_and_summarize.py
Here is a detailed README for your repository, covering project purpose, structure, setup, and usage:

---

# Django-Compatible News Scraping & Summarization

This repository provides:
- A Django web app for scraping links from arbitrary web pages via a simple form.
- A standalone Python script for scraping the latest news headlines, fetching article content, and summarizing them using an LLM API (Groq/OpenAI).

---

## Features

### 1. Django Web Scraper App
- **Form-based UI**: Enter any URL to scrape all links from that page.
- **Results**: Displays all found links and their text.
- **Extensible**: Ready to be integrated with more advanced scraping or summarization logic.

### 2. Standalone Summarizer Script
- **Scrapes headlines** from a news aggregator (e.g., Hacker News).
- **Fetches article content** for each headline.
- **Summarizes** each article using the Groq LLaMA3-8B API (or can be adapted for OpenAI).
- **Console output**: Prints title, link, and summary for each article.

---

## Folder Structure

```
.
├── core/                    # Django project settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── scraper/                 # Django app for scraping
│   ├── __init__.py
│   ├── urls.py              # App-level URL patterns
│   ├── views.py             # Scraping logic and view
│   ├── templates/
│   │   └── scraper/
│   │       └── index.html   # Main template for the scraper UI
│   └── __pycache__/
├── db.sqlite3               # SQLite database (auto-generated)
├── manage.py                # Django management script
├── scrape_and_summarize.py  # Standalone news scraping & summarization script
├── venv/                    # Python virtual environment (optional, recommended)
└── .env                     # (Not committed) API keys and secrets
```

---

## Setup & Installation

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd Django-compatible-scraping
```

### 2. Create and activate a virtual environment (recommended)

```sh
python -m venv venv
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install django requests beautifulsoup4 python-dotenv
```

### 4. Set up environment variables

Create a `.env` file in the project root for API keys (for the script):

```
GROQ_API_KEY=your_groq_api_key_here
# or for OpenAI:
# OPENAI_API_KEY=your_openai_api_key_here
```

---

## Running the Django Web App

1. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

2. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

3. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - You can also use `/news/`, `/newest/`, or `/from/` as alternate entry points.

---

## Using the Standalone Script

The script `scrape_and_summarize.py` scrapes news headlines, fetches article content, and summarizes each article.

**To run:**

```sh
python scrape_and_summarize.py
```

- Make sure your `.env` file contains the correct API key.
- The script prints each article's title, link, and a 3-bullet summary to the console.

---

## Customization & Extending

- **Django App**: You can extend the view to scrape more than just links, or integrate the summarization logic.
- **Script**: Adapt the script to use OpenAI or other LLM APIs, or change the news source.
- **Templates**: Modify `scraper/templates/scraper/index.html` for a custom UI.

---

