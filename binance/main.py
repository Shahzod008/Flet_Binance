import asyncio
from flet import Page, Text, ListView, TextButton, ButtonStyle, AppBar, FontWeight, TextStyle, app
from flet_core import IconButton, icons

from pasrer import main_parser


async def main(page: Page):

    async def main_page():
        page.clean()
        page.update()
        page.appbar = AppBar(title=Text(value="Binance", color="Yellow", style=TextStyle(letter_spacing=5),
                                        weight=FontWeight.BOLD))
        page.add(await list_view())

    async def index_page(e, title, price, change, description, capitalization, trading_volume):
        page.clean()
        cd = [title, price, change, description, capitalization, trading_volume]
        page.appbar = AppBar(
            title=Text(title, style=TextStyle(letter_spacing=5), weight=FontWeight.BOLD),
            leading=IconButton(icons.ARROW_BACK, on_click=lambda _: asyncio.run(main_page())),
            bgcolor=page.bgcolor)

        page.add(Text(f"{cd}"))
        page.update()

    async def list_view():
        lv = ListView(expand=True, spacing=10)
        cryptos = await main_parser()
        for crypto in cryptos:
            title = crypto["title"]
            description = crypto["description"]
            price = crypto["price"]
            change = crypto["change"]
            capitalization = crypto["capitalization"]
            trading_volume = crypto["trading_volume"]

            lv.controls.append(
                TextButton(
                    text=f"{title} - {description}", style=ButtonStyle(color="white"),
                    height=50,
                    on_click=lambda e, tit=title, pri=price, ch=change, descript=description, capital=capitalization,
                                    trading=trading_volume:
                    asyncio.run(index_page(e, tit, pri, ch, descript, capital, trading)))
            )

        return lv

    await main_page()

if __name__ == "__main__":
    app(target=main)
