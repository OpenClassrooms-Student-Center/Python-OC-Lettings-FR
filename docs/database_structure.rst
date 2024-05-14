*******************************************************
Description of the database structure and data models.
*******************************************************

This project uses the SQLite3 database to maintain a flexible and adaptive structure without excessive constraints. The database is structured with four distinct tables: letting, address, profile, and user.

**letting :**

- id (integrer (auto increment))
- title (varchar(256))
- address_id (linked to the address table) (integrer)

**address :**

- id (integrer (auto increment))
- number (integrer unsigned)
- street (varchar(64))
- city (varchar(64))
- state (varchar(2))
- zip_code (integrer unsigned)
- country_iso_code (varchar(3))

**profile :**

- id (integrer (auto increment))
- favorite_city (varchar(64))
- user_id (linked to the user table) (integrer)

**user :**

- id (integrer (auto increment))
- password (varchar(128))
- last_login (datetime)
- is_superuser (bool)
- username (varchar(150))
- first_name (varchar(30))
- email (varchar(254))
- is_staff (bool)
- is_active (bool)
- date_joined (datetime)
- last_name (varchar(150))

These four tables are grouped into two models (with the user model managed by Django's authentication) as follows:

**Lettings :**

- letting
- address

**Profiles :**

- profile

Using these models, the application effectively handles and organizes rental and user data, streamlining information retrieval and manipulation.