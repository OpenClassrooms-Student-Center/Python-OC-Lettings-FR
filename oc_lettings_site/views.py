from django.shortcuts import render

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo consectetur
def index(request):
    return render(request, 'index.html')
