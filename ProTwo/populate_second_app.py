import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

## Fake population script
from faker import Faker
from second_app.models import User

fakgen = Faker()

def Add_user(N):
    for entry in range(N):
        first_name = fakgen.first_name()
        last_name = fakgen.last_name()
        email = fakgen.email()

        fake_user = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]

if __name__ == '__main__':
    print("starting to add fake users")
    Add_user(10)
    print("Done adding users")
