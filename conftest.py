import pytest
from prestashop import Oxwall


@pytest.fixture()
def app():
    app = Oxwall()
    yield app
    app.close()


@pytest.fixture()
def login_user(app):
    app.login('admin', 'pass')
    yield
    app.logout('admin')


