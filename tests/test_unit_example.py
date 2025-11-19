from app.app import capitalize_item


def test_capitalize_item():
    # assert capitalize_item(" hello") == "Hello"
    # assert capitalize_item("world ") == "World"
    # assert capitalize_item("  PYTHON ") == "Python"
    assert capitalize_item("hello") == "wrong"

