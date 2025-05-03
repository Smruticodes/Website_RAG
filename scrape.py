import nest_asyncio
import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

nest_asyncio.apply()
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 …"

visited_urls = set()

async def fetch_html(session, url, retries=3):
    for attempt in range(1, retries+1):
        try:
            # set a 30-second timeout and force aiohttp to close the connection
            timeout = aiohttp.ClientTimeout(total=30)
            async with session.get(url, timeout=timeout) as resp:
                resp.raise_for_status()
                return await resp.text()
        except (aiohttp.ServerDisconnectedError, aiohttp.ClientError) as e:
            print(f"[{attempt}/{retries}] error fetching {url}: {e}")
            if attempt == retries:
                return ""      # give up and return empty
            await asyncio.sleep(1)  # back off before retry

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
    # force_close=True makes each TCP connection be torn down promptly
    connector = aiohttp.TCPConnector(force_close=True, enable_cleanup_closed=True)
    headers = {"User-Agent": os.environ["USER_AGENT"]}

    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        await crawl(session, start_url, start_url, text_content, image_urls)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Text Content:\n" + "\n".join(text_content))
        f.write("\n\nImage URLs:\n" + "\n".join(image_urls))
    print("Done.")

if __name__ == "__main__":
    asyncio.run(main("https://www.occamsadvisory.com/"))
