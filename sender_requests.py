# Настройки подключения и путь к документации
import configuration

# Отправка HTTP-запросов, взаимодействие с веб-сервисами
import requests

# Заголовки и тело запроса
import data

# Отправка POST-запроса на создание заказа /api/v1/orders
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body, 
                         headers=None) # headers=data.headers

response_post_new_order = post_new_order(data.order_body) # Вызов функции с телом запроса

print("response_post_new_order: ", response_post_new_order.status_code)
print("response_post_new_order.json(): ", response_post_new_order.json())  # Тело ответа в формате JSON

# Отправка GET-запроса на получение заказа по его номеру /v1/orders/track?t=123456
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track),
                         json=None,  
                         headers=None) 
