import secrets
import string


def get_short_url(url: str, length: int = 8):
    '''Функция принимает адрес и возвращает его короткий вариант'''
    alphabet = string.ascii_letters + string.digits
    short_url = ''.join(secrets.choice(alphabet) for _ in range(length))
    return short_url
