#Никола Трайковски 18-я коргота.
import pytest
from sender_stand_request import create_order, get_order

from data import create_order_data


@pytest.fixture(scope='module')
def order():
    order_response = create_order(create_order_data)
    return order_response


def test_create_order(order):
    assert 'track' in order, "Ответ не содержит трек-номер"
    assert isinstance(order['track'], int), "Трек-номер должен быть целым числом"


def test_get_order(order):
    track_number = order['track']
    order_info = get_order(track_number)

    assert 'order' in order_info, "Ответ не содержит информацию о заказе"
    assert order_info['order']['firstName'] == create_order_data['firstName'], "Имя в заказе не совпадает"
    assert order_info['order']['lastName'] == create_order_data['lastName'], "Фамилия в заказе не совпадает"



if __name__ == "__main__":
    pytest.main()