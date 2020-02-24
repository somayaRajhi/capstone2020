'''
Module.
'''
from c20_server.numbers import Numbers

def test_get_value_return_():
    '''
    Test.
    '''
    numbers = Numbers()
    assert numbers.get_value() == 100
