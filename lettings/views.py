from django.shortcuts import render
from .models import Letting


class LettingsViews:
    def index(self):
        """
        Render the index page with a list of all lettings.

        Args:
            request: The HTTP request object.

        Returns:
            The rendered HTML response.

        """
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(self, 'lettings/index.html', context)

    def letting(self, letting_id):
        """
        Render the letting page for a specific letting.

        Args:
            request: The HTTP request object.
            letting_id: The ID of the letting.

        Returns:
            The rendered HTML response.

        """
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(self, 'lettings/letting.html', context)



