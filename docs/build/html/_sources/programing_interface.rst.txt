Programing Interface description
================================

URL routes
----------
Here are all the routes for each Django app :

`oc_lettings_site` app
^^^^^^^^^^^^^^^^^^^^^^

==========   =============
Route        Description
==========   =============
/            Home page
/lettings/   Lettings list
/profiles/   Profiles list
/admin/      Admin page
==========   =============

`lettings` app
^^^^^^^^^^^^^^

===========================    ===================
Route                          Description
===========================    ===================
/lettings/                     Lettings index page
/lettings/<int:letting_id>/    Letting detail
===========================    ===================

`profiles` app
^^^^^^^^^^^^^^

===========================    ===================
Route                          Description
===========================    ===================
/profiles/                     Profiles index page
/profiles/<int:profile_id>/    Profile detail
===========================    ===================

Django views
------------
Each app has its views.py module according to the routes previously described.

================   ========   =====================
Django App         View       Template rendered
================   ========   =====================
oc_lettings_site   index      index.html
lettings           index      lettings/index.html
lettings           lettings   lettings/letting.html
profiles           index      profiles/index.html
profiles           profiles   lettings/profile.html
================   ========   =====================

In addition, in each application view, we check if an error has occurred (404 or 500) and, if an error occurs, the view renders an error template.

Templates rendering
-------------------
Each view renders templates with Django render method.

Each Django app has a template folder with one template for each view previously described and one for each possible error.

Database interaction
--------------------
In all views, database access is achieved through an SQL query applied on the required model. The primary use case
involves calling the methods 'objects.all()' or `objects.get()` as shown below for example :

.. code::

    lettings_list = Letting.objects.all()

.. code::

    profile = Profile.objects.get(user__username=username)
