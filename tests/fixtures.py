import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.fixture
def create_admin_user(django_user_model):
    return django_user_model.objects.create_superuser('root', '', '123')



@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")

