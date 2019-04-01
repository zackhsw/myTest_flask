from app import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
if __name__ == '__main__':
    user_id = 38
    SECRET_KEY = 'hard to get string'
    # Serializer(current_app.config['SECRET_KEY'], expires_in=expiration).dumps({'user_id': user_id})
    s = Serializer(SECRET_KEY, expires_in=604800)
    t = s.dumps({'user_id': user_id})
    token = t.decode('ascii')
    print('push v7')
    print('push v8')
    print('push v9')
    print('push v10')
    print(token,'添加改变----')
    print('token--+-->', token,'<--+--')
    app.run()
