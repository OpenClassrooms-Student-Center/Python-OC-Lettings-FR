from faker import Faker
from django.contrib.auth.models import User

from profiles.models import Profile
from .models import Letting, Address

fake = Faker()


def create_fake_user():
    username = fake.user_name()  # Générer un nom d'utilisateur aléatoire
    email = fake.email()  # Générer une adresse e-mail aléatoire
    password = fake.password()  # Générer un mot de passe aléatoire

    return User.objects.create_user(
        username=username, email=email, password=password
    )


def create_fake_address():
    number = fake.building_number()
    street = fake.street_name()
    city = fake.city()
    state = fake.country()
    zip_code = fake.postcode()
    country_iso_code = fake.country_code()

    return Address.objects.create(
        number=number,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        country_iso_code=country_iso_code,
    )


def create_fake_letting():
    address = create_fake_address()
    title = fake.name()

    return Letting.objects.create(title=title, address=address)


def create_fake_profile():
    user = create_fake_user()
    favorite_city = fake.city()

    return Profile.objects.create(user=user, favorite_city=favorite_city)
