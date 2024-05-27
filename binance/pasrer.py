import asyncio
from bs4 import BeautifulSoup
import httpx


async def main_parser():
    url = "https://www.binance.com/ru/markets/overview"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text

    soup = BeautifulSoup(html_content, features='html.parser')

    def get_text_or_default(element, default=""):
        return element.text if element else default

    crypto_containers = soup.find_all(name='div', class_='css-vlibs4')
    cryptos = []
    for container in crypto_containers:
        data = {
            "title": get_text_or_default(
                container.find(
                    'div',
                    class_='subtitle3 text-t-primary css-vurnku'
                )
            ),
            "description": get_text_or_default(
                container.find(
                    'div',
                    class_='body3 line-clamp-1 truncate text-t-third css-vurnku'
                )
            ),
            "price": get_text_or_default(
                container.find(
                    'div',
                    class_='body2 items-center css-18yakpx'
                )
            ),
            "change": get_text_or_default(
                container.find(
                    'div',
                    class_='subtitle3 css-191zdd8'
                )
            ),
            "capitalization": get_text_or_default(
                container.find_all(
                    'div',
                    class_='body2 text-t-primary css-18yakpx')[0] if len(
                    container.find_all(
                        'div',
                        class_='body2 text-t-primary css-18yakpx'
                    )
                ) > 0 else None
            ),
            "trading_volume": get_text_or_default(
                container.find_all(
                    'div',
                    class_='body2 text-t-primary css-18yakpx')[1] if len(
                    container.find_all(
                        'div',
                        class_='body2 text-t-primary css-18yakpx'
                    )
                ) > 1 else None
            ),
        }
        cryptos.append(data)

    return cryptos

if __name__ == "__main__":
    asyncio.run(main_parser())
