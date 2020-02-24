from c20_server.numbers import Numbers

def test_get_value_return_():
    numbers = Numbers()
    assert numbers.get_value() == 100
