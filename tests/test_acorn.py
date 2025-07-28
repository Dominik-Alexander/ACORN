from acorn import greeter


def test_greet():
    assert greeter.greet("World") == "Hello, World!"
