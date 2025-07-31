from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scrape(request):
    results = []
    if request.method == 'POST':
        target_url = request.POST.get('target_url')
        try:
            resp = requests.get(target_url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(resp.text, 'html.parser')
            for a in soup.find_all('a'):
                text = a.get_text(strip=True)
                href = a.get('href')
                if text and href:
                    results.append({'text': text, 'href': href})
        except Exception as e:
            results = [{'text': f"Error: {str(e)}", 'href': '#'}]
    return render(request, 'scraper/index.html', {'results': results})