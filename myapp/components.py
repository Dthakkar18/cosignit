# NOTE: not using this rn (or ever ig idk atm)

from reactpy import component, html
from .models import Member
from asgiref.sync import sync_to_async

@component
def header(recipient: str):
    #member = Member.objects.get(firstName="John").firstName
    #user = await sync_to_async(str)(Member.objects.get(firstName="John").firstName)
    layout = html.div(
        html.h1(f"Hello {recipient}!"),
        html.h2("Dthakkar18"),
        html.form()
    )
    return layout
