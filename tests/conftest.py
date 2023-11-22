import pytest

@pytest.fixture(scope='session')
def email():
    yield 'testwww@test.ru'

@pytest.fixture(scope='session')
def email_pretty():
    yield 'evgeniy_cheremisenko_3_777@test.ru'
@pytest.fixture(scope='session')
def password():
    yield 'Ebc2786'

@pytest.fixture(scope='session')
def password_pretty():
    yield '111111'

@pytest.fixture(scope='session')
def user():
    yield 'testtester'