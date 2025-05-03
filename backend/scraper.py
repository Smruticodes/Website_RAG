# backend/scraper.py
import nest_asyncio
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

nest_asyncio.apply()

async def fetch_html(session, url, retries=3):
    for attempt in range(1, retries+1):
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with session.get(url, timeout=timeout) as resp:
                resp.raise_for_status()
                return await resp.text()
        except (aiohttp.ServerDisconnectedError, aiohttp.ClientError) as e:
            print(f"[{attempt}/{retries}] error fetching {url}: {e}")
            if attempt == retries:
                return ""      
            await asyncio.sleep(1)  

async def crawl(session, url, base_url, text_content, image_urls):
    if url in visited_urls:
        return
    visited_urls.add(url)

    html = await fetch_html(session, url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    for text in soup.stripped_strings:
        text_content.append(text)
    for img in soup.find_all("img", src=True):
        image_urls.append(urljoin(url, img['src']))

    for a in soup.find_all("a", href=True):
        link = urljoin(url, a['href'])
        if urlparse(link).netloc == urlparse(base_url).netloc:
            await crawl(session, link, base_url, text_content, image_urls)

async def main(start_url):
    text_content, image_urls = [], []
    connector = aiohttp.TCPConnector(force_close=True, enable_cleanup_closed=True)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        await crawl(session, start_url, start_url, text_content, image_urls)

    with open(f"backend/{start_url.split('//')[1].split('/')[0]}.txt", "w", encoding="utf-8") as f:
        f.write("Text Content:\n" + "\n".join(text_content))
        f.write("\n\nImage URLs:\n" + "\n".join(image_urls))
    print("Scraping complete.")

if __name__ == "__main__":
    import sys
    asyncio.run(main(sys.argv[1]))
