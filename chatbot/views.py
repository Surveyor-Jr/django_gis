import json
from django.shortcuts import render


def api_request(request):
    """
    A view to decode and encode the response for the Chatbot
    """
    # if request.method == 'POST':
    x = {
        "data":[
            {
                "message":"Hi I was built with Python"
            }
        ]
    }
        # sorting result in asscending order by keys:
    sorted_string = json.dumps(x)
    return render(request, 'chatbot/api_endpoint.html', context={
            'result': sorted_string
        })
