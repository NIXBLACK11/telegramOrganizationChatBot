from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        my_string = data.get("my_string")
        response_data = {"response": my_string}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Invalid request method"})



fetch('/my-view/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ my_string: 'Hello world' })
})
.then(response => response.json())
.then(data => console.log(data))
