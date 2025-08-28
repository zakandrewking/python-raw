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
    dark = ui.dark_mode(value=None)
    ui.label("Hello, NiceGUI!")
    with ui.row():
        ui.link("Open item 123", "/items/123?q=foo")
        ui.link("API root", "/api")
    ui.separator()
    ui.label("Carbon capture methods")
    columns = [
        {"name": "method", "label": "Method", "field": "method", "sortable": True},
        {"name": "approach", "label": "Approach", "field": "approach", "sortable": True},
        {"name": "maturity", "label": "Maturity", "field": "maturity", "sortable": True},
        {"name": "storage", "label": "Storage/Use", "field": "storage", "sortable": True},
    ]
    rows = [
        {
            "id": 1,
            "method": "Point-source (post-combustion)",
            "approach": "Amine solvent absorption from flue gas",
            "maturity": "Commercial",
            "storage": "Geologic storage; EOR",
        },
        {
            "id": 2,
            "method": "Pre-combustion",
            "approach": "Shift syngas to CO2 + H2; capture CO2",
            "maturity": "Commercial (industrial)",
            "storage": "Geologic storage",
        },
        {
            "id": 3,
            "method": "Oxy-fuel combustion",
            "approach": "Burn in O2 to produce concentrated CO2",
            "maturity": "Pilot/Demo",
            "storage": "Geologic storage",
        },
        {
            "id": 4,
            "method": "Direct Air Capture (DAC)",
            "approach": "Solid/liquid sorbent capture from ambient air",
            "maturity": "Early commercial",
            "storage": "Geologic storage; utilization",
        },
        {
            "id": 5,
            "method": "BECCS",
            "approach": "Capture CO2 from biomass energy/fermentation",
            "maturity": "Pilot/Early",
            "storage": "Geologic storage",
        },
        {
            "id": 6,
            "method": "Mineralization",
            "approach": "React CO2 with minerals or concrete",
            "maturity": "Pilot/Early",
            "storage": "Solid carbonates (in/ex-situ)",
        },
        {
            "id": 7,
            "method": "Ocean alkalinity enhancement",
            "approach": "Increase seawater alkalinity to draw down CO2",
            "maturity": "Research/Pilot",
            "storage": "Dissolved bicarbonate/carbonate",
        },
        {
            "id": 8,
            "method": "Soil carbon sequestration",
            "approach": "Land management to increase soil carbon",
            "maturity": "Mature (MRV evolving)",
            "storage": "Soil organic carbon",
        },
        {
            "id": 9,
            "method": "Afforestation/Reforestation",
            "approach": "Biological CO2 uptake via biomass growth",
            "maturity": "Mature",
            "storage": "Biomass/soils",
        },
    ]
    ui.table(columns=columns, rows=rows, row_key="id")


ui.run_with(app)
