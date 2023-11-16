from reactpy_django import Component, html

@Component
def hello_world(recipient: str):
    return html.h1(f"Hello {recipient}!")