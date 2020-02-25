from django.shortcuts import render

# Create your views here.

# request is a HttpRequestObject which is created when page is loaded
# contains info about : the request itself meaning method [get/post] and params if needed
def hello_world(request):
    return render(request, 'hello_world.html', {})
