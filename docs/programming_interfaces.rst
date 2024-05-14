*******************************************
Description of the programming interfaces.
*******************************************

The OC Lettings project exposes various interfaces that enable developers to interact with different aspects of the application and its functionalities.

Interface Types
--------------------
**1. User Interface (UI) Components:**

Users interact with the application through a web-based graphical interface. This includes forms, buttons, navigation menus, and other interactive elements.

**2. Service Interfaces (APIs):**

The application provides RESTful APIs for external integrations. These APIs allow developers to perform operations such as creating, reading, updating, and deleting data resources.

**3. Data Interfaces:**

Developers can access and manipulate data within the system using database access methods and data exchange formats supported by the application.

Functionality and Behavior
---------------------------

The programming interfaces support the following functionalities:

- User Management:

APIs for user authentication, registration, and profile management.
Methods to retrieve user information and update user profiles.

- Property Listings:

Interfaces to manage property listings, including CRUD operations for creating, updating, and retrieving property details.

- Address Management:

APIs for handling address information associated with property listings.

Methods and Parameters
----------------------

**index(request)**

Renders the index page with a list of lettings or profiles.

- Description:

This view retrieves a list of lettings or profiles from the database and renders the corresponding HTML template (index.html or profiles/index.html).

- Arguments:

request (HttpRequest): The HTTP request object.

- Returns:

HttpResponse: The rendered HTML response containing the index page with the list of lettings or profiles.

**letting(request, letting_id)**

Renders the letting details page based on the specified letting ID.

- Description:

This view retrieves the letting object with the specified ID from the database and renders the letting.html template with the letting details.

- Arguments:

request (HttpRequest): The HTTP request object.
letting_id (int): The ID of the letting to display.

- Returns:

HttpResponse: The rendered HTML response containing the letting details page.

**profile(request, username)**

Renders the profile page for a specific user based on the username.

- Description:

This view retrieves the profile associated with the given username from the database and renders the profiles/profile.html template with the profile details.

- Arguments:

request (HttpRequest): The HTTP request object.

**username (str):**

The username of the user whose profile is being viewed.

- Returns:

HttpResponse: The rendered HTML response containing the profile page.

These views utilize Django's ORM (Letting.objects.get(), Profile.objects.all()) to fetch data from the database and pass the retrieved data to corresponding HTML templates (index.html, letting.html, profiles/index.html, profiles/profile.html) using the render() function.

Endpoint URLs (for Web APIs)
----------------------------
**For web-based APIs, the following endpoint URLs are available:**

GET /api/users/{user_id}: Retrieve user details by user ID.

POST /api/properties: Create a new property listing.

PUT /api/properties/{property_id}: Update an existing property.

Error Handling
--------------
The programming interfaces handle errors and exceptions gracefully, providing informative error messages and appropriate HTTP status codes to indicate the status of API requests.


By documenting these programming interfaces, developers can gain insights into how to effectively integrate with and utilize the capabilities offered by the OC Lettings application. This documentation facilitates seamless development and interaction with the provided interfaces, enabling efficient application development and integration efforts.