Application Views and URL Endpoints
===================================

This section describes the main views and URL patterns of the OC Lettings application.

Main Views
----------

The application provides several key views to navigate through the platform:

Home Page View
^^^^^^^^^^^^^^

**URL**: ``/``

The home page serves as the entry point to the application, with links to lettings and profiles.

.. code-block:: python

   # oc_lettings_site/views.py
   def index(request):
       """Home page view"""
       return render(request, 'index.html')

Lettings Views
--------------

Views for browsing property lettings.

Lettings Index
^^^^^^^^^^^^^^

**URL**: ``/lettings/``

Displays a list of all available lettings.

.. code-block:: python

   # lettings/views.py
   def index(request):
       """Display the list of all lettings"""
       lettings_list = Letting.objects.all()
       context = {'lettings_list': lettings_list}
       return render(request, 'lettings/index.html', context)

Letting Details
^^^^^^^^^^^^^^^

**URL**: ``/lettings/<int:letting_id>/``

Shows details for a specific letting.

.. code-block:: python

   # lettings/views.py
   def letting(request, letting_id):
       """Display the details of a specific letting"""
       letting = Letting.objects.get(id=letting_id)
       context = {'letting': letting}
       return render(request, 'lettings/letting.html', context)

Profile Views
-------------

Views for browsing user profiles.

Profiles Index
^^^^^^^^^^^^^^

**URL**: ``/profiles/``

Displays a list of all profiles.

.. code-block:: python

   # profiles/views.py
   def index(request):
       """Display the list of all profiles"""
       profiles_list = Profile.objects.all()
       context = {'profiles_list': profiles_list}
       return render(request, 'profiles/index.html', context)

Profile Details
^^^^^^^^^^^^^^^

**URL**: ``/profiles/<str:username>/``

Shows details for a specific profile.

.. code-block:: python

   # profiles/views.py
   def profile(request, username):
       """Display the details of a specific profile"""
       user = User.objects.get(username=username)
       profile = Profile.objects.get(user=user)
       context = {'profile': profile}
       return render(request, 'profiles/profile.html', context)