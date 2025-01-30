# Импортируем модуль sender_request, содержащий функции для отправки HTTP-запросов к API.
import sender_requests

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Функция для получения трека заказа 
def get_new_order_track():
    # Создать новый заказ 
    body = data.order_body.copy()
    response = sender_requests.post_new_order(body)

    # Запомнить трек заказа 
    return response.json()["track"]

def positive_assert():
    response = sender_requests.get_order_by_track(get_new_order_track())

    assert response.status_code == 200

def test_create_order_get_success_response():
    positive_assert()