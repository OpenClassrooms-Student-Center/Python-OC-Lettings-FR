Structure of the OC Lettings Application
========================================

Applications
------------

OC Lettings is composed of three Django applications:

- **Lettings**: Manages the letting listings.
- **Profiles**: Handles user profiles.
- **OC_Lettings_Site**: Contains the project settings and URL configurations.

Models
------

The project includes three models:

1. **Address**:
    - Used to store address details.

2. **Letting**:
    - Represents a letting listing.
    - Has a `OneToOneField` relationship with the `Address` model.

3. **Profile**:
    - Represents a user profile.
    - Has a `OneToOneField` relationship with Django's built-in `User` model.
