from nicegui import ui
from books import render_books_dashboard
from expenses import render_expenses_dashboard

@ui.page("/livros")
def books_dashboard_page():
    render_books_dashboard()
    with ui.left_drawer() as drawer:
        ui.link("Dashboard", "/").classes("block py-2")
        ui.link("Despesas", "/despesas").classes("block py-2")
        ui.link("Livros", "/livros").classes("block py-2")

@ui.page("/despesas")
def books_dashboard_page():
    render_expenses_dashboard()
    with ui.left_drawer() as drawer:
        ui.link("Dashboard", "/").classes("block py-2")
        ui.link("Despesas", "/despesas").classes("block py-2")
        ui.link("Livros", "/livros").classes("block py-2")

@ui.page("/")
def navigation_menu():
    with ui.row().classes("gap-4 items-center"):
        ui.label("Menu").classes("text-lg font-bold")
    with ui.left_drawer() as drawer:
        ui.link("Dashboard", "/").classes("block py-2")
        ui.link("Despesas", "/despesas").classes("block py-2")
        ui.link("Livros", "/livros").classes("block py-2")

ui.run(title="Dashboard Livros", port=8080)
