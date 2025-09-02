from django.shortcuts import render, get_object_or_404
from .models import Letting

def index(request):
    """
    View function for the lettings list page.
    
    Args:
        request: The HTTP request object    
    Returns:
        template 'lettings/index.html' with a list of all lettings
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)

def letting(request, letting_id):
    """
    View function for displaying a specific letting's details.
    
    Args:
        request: The HTTP request object
        letting_id: The ID of the letting to display
        
    Returns:
        template 'lettings/letting.html' with the requested letting's details
        
    Raises:
        Http404: If the letting with the given ID doesn't exist
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
