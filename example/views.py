# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body style="background-color:gray">
            <h1>Hello from Vercel by Artux!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
