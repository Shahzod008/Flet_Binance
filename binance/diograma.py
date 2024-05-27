# # import flet as ft
# #
# # data_1 = [
# #     ft.LineChartData(
# #         data_points=[
# #             ft.LineChartDataPoint(1, 1), ft.LineChartDataPoint(2, 2), ft.LineChartDataPoint(3, 3),
# #             ft.LineChartDataPoint(4, 4), ft.LineChartDataPoint(5, 5), ft.LineChartDataPoint(6, 6),
# #             ft.LineChartDataPoint(7, 7), ft.LineChartDataPoint(8, 8), ft.LineChartDataPoint(9, 9),
# #             ft.LineChartDataPoint(10, 10), ft.LineChartDataPoint(11, 11), ft.LineChartDataPoint(12, 12),
# #             ft.LineChartDataPoint(13, 13), ft.LineChartDataPoint(14, 14), ft.LineChartDataPoint(15, 15),
# #
# #         ],
# #         stroke_width=1,
# #     ),
# # ]
# #
# #
# # def main(page: ft.Page):
# #     chart = ft.LineChart(data_series=data_1, expand=True)
# #
# #     page.add(chart)
# #
# #
# # ft.app(main)
# #
# #
# # import flet as ft
# #
# #
# # def main(page: ft.Page):
# #     page.appbar = ft.AppBar()
# #     page.add(ft.Text("Body!"))
# #
# #
# # ft.app(target=main)
#
#
# import asyncio
# from flet_core import Text, ListView, TextButton, ButtonStyle, AppBar, FontWeight, TextStyle, IconButton, icons
# from flet import Page, app
# import aiohttp
# from bs4 import BeautifulSoup
#
#
# async def main_parser():
#     url = "https://www.binance.com/ru/markets/overview"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
#     }
#
#     async with aiohttp.ClientSession(headers=headers) as session:
#         async with session.get(url) as response:
#             html_content = await response.text()
#             soup = BeautifulSoup(html_content, 'html.parser')
#
#     def get_text_or_default(element, default=""):
#         return element.text if element else default
#
#     crypto_containers = soup.find_all('div', class_='css-vlibs4')
#     cryptos = []
#     for container in crypto_containers:
#         data = {
#             "Название": get_text_or_default(container.find('div', class_='subtitle3 text-t-primary css-vurnku')),
#             "Описание": get_text_or_default(
#                 container.find('div', class_='body3 line-clamp-1 truncate text-t-third css-vurnku')),
#             "Цена": get_text_or_default(container.find('div', class_='body2 items-center css-18yakpx')),
#             "Изменение": get_text_or_default(container.find('div', class_='subtitle3 css-191zdd8')),
#             "Рыночная капитализация": get_text_or_default(
#                 container.find_all('div', class_='body2 text-t-primary css-18yakpx')[0] if len(
#                     container.find_all('div', class_='body2 text-t-primary css-18yakpx')) > 0 else None),
#             "Объем торгов": get_text_or_default(
#                 container.find_all('div', class_='body2 text-t-primary css-18yakpx')[1] if len(
#                     container.find_all('div', 'body2 text-t-primary css-18yakpx')) > 1 else None),
#         }
#         cryptos.append(data)
#     return cryptos
#
#
# async def main(page: Page):
#     page.window_height = 700
#     page.window_width = 400
#     page.bgcolor = "black"
#     page.window_resizable = False
#
#     async def main_page():
#         page.clean()
#         page.update()
#         page.appbar = AppBar(
#             title=Text(value="Binance", color="Yellow", style=TextStyle(letter_spacing=5), weight=FontWeight.BOLD),
#             bgcolor=page.bgcolor)
#         page.add(await list_view())
#         page.update()
#
#     async def index_page(e, price):
#         page.clean()
#         page.appbar = AppBar(
#             leading=IconButton(icons.ARROW_BACK, on_click=lambda _: asyncio.create_task(main_page())),
#             title=Text(e.control.text.split('-')[1],
#                        style=TextStyle(letter_spacing=5),
#                        weight=FontWeight.BOLD),
#             bgcolor=page.bgcolor)
#         page.add(Text(price))
#         page.update()
#
#     async def list_view():
#         lv = ListView(expand=True, spacing=10)
#         cryptos = await main_parser()
#         for crypto in cryptos:
#             price = crypto["Цена"]
#             lv.controls.append(
#                 TextButton(
#                     text=f"{crypto['Название']} - {crypto['Описание']}",
#                     style=ButtonStyle(color="white"),
#                     height=50,
#                     on_click=lambda e, p=price: asyncio.create_task(index_page(e, p))
#                 )
#             )
#         return lv
#
#     await main_page()
#
#
# if __name__ == "__main__":
#     app(target=main)




import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)