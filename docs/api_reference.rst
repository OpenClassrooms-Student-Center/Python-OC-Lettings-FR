Code Reference
=============

This section documents all classes, functions, and methods available in the OC Lettings Site application.

Lettings Application
--------------------

The lettings app manages rental properties and their addresses.

Models
~~~~~~

.. autoclass:: lettings.models.Address
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects, id, pk, letting

.. autoclass:: lettings.models.Letting
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects, id, pk, address_id

Views
~~~~~

.. automodule:: lettings.views
   :members:

Profiles Application
--------------------

The profiles app manages user profiles with additional information.

Models
~~~~~~

.. autoclass:: profiles.models.Profile
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects, id, pk, user_id

Views
~~~~~

.. automodule:: profiles.views
   :members:

Main Site (oc_lettings_site)
---------

Views
~~~~~

.. automodule:: oc_lettings_site.views
   :members:
