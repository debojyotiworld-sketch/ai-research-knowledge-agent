import requests 
from bs4 import BeautifulSoup
from urllib.parse import quote


def web_search(query, max_results=10):
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select(".result")[:max_results]:
        title = result.select_one(".result__title")
        link = result.select_one(".result__a")
        snippet = result.select_one(".result__snippet")

        if not title or not link:
            continue

        results.append({
            "title": title.get_text(" ", strip=True),
            "url": link.get("href"),
            "snippet": snippet.get_text(" ", strip=True) if snippet else ""
        })

    return results


results = web_search(query)

for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['title']}")
    print(result["url"])
    print(result["snippet"])