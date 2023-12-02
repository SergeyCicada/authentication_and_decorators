import calendar  # для установки времени жизни токена
import datetime  # для установки времени жизни токена

import jwt

secret = 's3cR$eT'  # секретный ключ не меняется в течении жизни всего проекта
algo = 'HS256'  # алгоритм для генерации токена


def generate_token(data):
    """Формируем жизнь токена min30 =
    Сохраняем в ту информацию которую мы будет кодировать в data по ключу exp -
    сохраняем количество секунд с января 1970
    В return обращаемся к библиотеке jwt с методом encode(кодирует информациб в JWT токен, передаём туда данные,
    секретный ключ и алгоритм"""
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30) # берём текущую дату в формате utc + 30min
    data['exp'] = calendar.timegm(min30.timetuple())

    return jwt.encode(data, secret, algorithm=algo)  # JWT = asdasdas.fkgfjasdk.dasfjasdk


def check_token(token):
    try:
        jwt.decode(token, secret, algorithms=[algo])
        return True
    except Exception:
        return False


if __name__ == "__main__":
    data = {
        'username': 'myname',
        'role': 'user'
    }
    token = generate_token(data)
    is_ok = check_token(token)
