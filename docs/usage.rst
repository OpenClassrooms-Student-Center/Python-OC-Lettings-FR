Usage
=====

Navigation through the OC Lettings Site application
---------------------------------------------------

Main pages:

- Home page: `/`

- Lettings listings: `/lettings/`

- Individual letting details: `/lettings/<int:letting_id>/`

- User profiles listings: `/profiles/`

- Individual profile details: `/profiles/<int:profile_id>/`

Admin page:
- Admin interface: `/admin/`

Use Cases
---------

**Use Case 1: Browse rental listings**

1. User visits the homepage
2. User clicks on "Lettings"
3. System displays all available lettings
4. User clicks on a specific letting title
5. System shows detailed information (address, city, zip code)

**Use Case 2: View user profiles**

1. User navigates to Profiles section
2. System displays list of registered users
3. User clicks on a username
4. System shows profile details (favorite city)

**Use Case 3: Manage data (Admin)**

1. Administrator logs into /admin/
2. Admin can create, edit, or delete lettings and profiles
3. Changes are immediately reflected on the public site



.. note::
   This project is actually deployed on Render and can be accessed at the following URL:
   `OC Lettings Site on Render <https://oc-lettings-site-latest-05t2.onrender.com/>`_.
