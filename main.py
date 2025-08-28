from typing import Union

from fastapi import FastAPI
from nicegui import ui

app = FastAPI()


@app.get("/api")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@ui.page("/")
def ui_page():
    ui.label("Hello, NiceGUI!")
    with ui.row():
        ui.link("Open item 123", "/items/123?q=foo")
        ui.link("API root", "/api")


ui.run_with(app)
