from django.shortcuts import render
from django.http import Http404

def index(request):
    """
    View function for the home page.
    
    Args:
        request: The HTTP request object
        
    Returns:
        Rendered template 'index.html'
    """
    return render(request, 'index.html')

def test_404(request):
    """
    Test view that raises a 404 error.
    
    Args:
        request: The HTTP request object
        
    Raises:
        Http404: Always raises a 404 error for testing purposes
    """
    raise Http404("Page de test 404")

def test_500(request):
    """
    Test view that raises a 500 error by performing a division by zero.
    
    Args:
        request: The HTTP request object
        
    Returns:
        This function never returns as it raises a ZeroDivisionError
    """
    division_by_zero = 1 / 0
    return render(request, 'index.html')
