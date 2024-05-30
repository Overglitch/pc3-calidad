from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.greeter.Greeter import Greeter

scenarios('../features/greeter.feature')


@pytest.fixture
def greeter():
    return Greeter()


@given(parsers.parse('a Greeter'))
def a_new_greeter():
    pass


@when(parsers.parse('I give my name as "{name}"'))
def i_give_my_name_as(greeter, name):
    greeter.my_name(name)


@then(parsers.parse('The greeter says Hello "{name}"'))
def the_greeter_says_hello(greeter, name):
    assert greeter.greet() == 'Hello ' + name


@when(parsers.parse("I don't provide a name"))
def no_name_provided(greeter):
    pass


@then(parsers.parse('the greeter says "{message}"'))
def please_provide_a_name(greeter, message):
    assert greeter.greet() == message
