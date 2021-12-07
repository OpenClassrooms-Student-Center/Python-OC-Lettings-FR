from django.shortcuts import render

# Create your views here.
# Aenean leo magna, vestibulum et
from lettings.models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# esque justos. In ,m lorem. Seunim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
