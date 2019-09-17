from app import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

if __name__ == '__main__':
    # user_id = 38
    # SECRET_KEY = 'hard to get string'
    # Serializer(current_app.config['SECRET_KEY'], expires_in=expiration).dumps({'user_id': user_id})
    # s = Serializer(SECRET_KEY, expires_in=604800)
    # t = s.dumps({'user_id': user_id})
    # token = t.decode('ascii')
    # print('push v7')
    # print('push v8')
    # print('push v9')
    # print('push v17')
    # print('push v19')
    # print(token, '添加改变----')
    # print('token--+-->', token, '<--+--')
    # app.run(host='0.0.0.0', port=5000)
    s = "asdasdsdfsdfdfgdfgasdf"
    str_stack = []
    num, max_num = 0, 0
    max_str = ''
    for i in s:
        if i not in str_stack:
            str_stack.append(i)
            num += 1
            continue

        if num > max_num:
            max_num = num
        num = 1
        print(str_stack)
        str_stack.clear()
        str_stack.append(i)
        print('end',str_stack)
    print(max_num)