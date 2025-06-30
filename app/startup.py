from nicegui import Client, ui
from app import counter


def startup() -> None:
    counter.create()