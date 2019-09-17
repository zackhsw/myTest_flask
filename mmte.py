import xlrd as xlrd
from flask_sqlalchemy import xrange
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

if __name__ == '__main__':
    user_id = 48
    SECRET_KEY = 'hard to get string'
    # Serializer(current_app.config['SECRET_KEY'], expires_in=expiration).dumps({'user_id': user_id})
    s = Serializer(SECRET_KEY, expires_in=604800)
    t = s.dumps({'user_id': user_id})
    token = t.decode('ascii')
    print(token)
    print('token--+-->', token, '<--+--')

    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    import difflib
    from pypinyin import pinyin, lazy_pinyin
    from simhash import Simhash

    a = "六六六"
    b = "六六啊"
    print("simple ratio---", fuzz.ratio(b, a))
    print("partial ratio---", fuzz.partial_ratio(b, a))
    print("token sort ratio---", fuzz.token_sort_ratio(b, a))
    print("token set ratio---", fuzz.token_set_ratio(b, a))

    print("difflib---", difflib.SequenceMatcher(None, a, b).ratio())

    print("a---", pinyin(a))
    print("a---", lazy_pinyin(a))
    print("b---", pinyin(b))
    print("b---", lazy_pinyin(b))

    a_, b_ = lazy_pinyin(a), lazy_pinyin(b)
    # a_, b_ = pinyin(a), pinyin(b)
    print("simple ratio---", fuzz.ratio(a_, b_))
    print("partial ratio---", fuzz.partial_ratio(a_, b_))
    print("token sort ratio---", fuzz.token_sort_ratio(a_, b_))
    print("token set ratio---", fuzz.token_set_ratio(a_, b_))
    print("difflib---", difflib.SequenceMatcher(None, a_, b_).ratio())

    print("simhash---",Simhash(a).distance(Simhash(b)))
    print("simhash---",Simhash(a).distance(Simhash(a)))


    # import pymysql
    # import pandas as pd
    # from sqlalchemy import create_engine
    #
    # # 建立连接，username替换为用户名，passwd替换为密码，test替换为数据库名
    # conn = create_engine('mysql+pymysql://root:root123@localhost:3306/trace_test', encoding='utf8')
    # # 写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
    # pd.io.sql.to_sql( "ent_basic", conn, if_exists='replace')

    # workbook = xlrd.open_workbook('D:\\搜狗高速下载\\限用农药清单.xlsx')  # 读取excel文件
    # print(workbook.nsheets)  # 获取表单的数量
    # print(workbook.sheets()[1])  # 获取表单的数量
    # for booksheet in workbook.sheets():
    #     for col in xrange(booksheet.ncols):
    #         for row in xrange(booksheet.nrows):
    #             value = booksheet.cell(row, col).value
    #             print(value)
    # fileOutput = open('D:\\搜狗高速下载\\限用农药.json', 'w')
    # # 可以在这里写一些固定的注释代码之类的
    # writeData = "-- @author:Zack\n\n\n"
    # # for booksheet in workbook.sheets():
    # #     writeData = writeData + 'AT' + booksheet.name + ' = {\n'
    # #     for col in xrange(booksheet.ncols):
    # #         for row in xrange(booksheet.nrows):
    # #             value = booksheet.cell(row, col).value
    # #             if row == 0:
    # #                 writeData = writeData + '\t' + '["' + value + '"]' + ' = ' + '{ '
    # #             else:
    # #                 writeData = writeData + '"' + str(booksheet.cell(row, col).value) + '" , '
    # #         else:
    # #             writeData = writeData + '} ,\n'
    # #     else:
    # #         writeData = writeData + '}\n\n'
    # # else:
    # #     fileOutput.write(writeData)
    # #
    # # fileOutput.close()
    #
    # for booksheet in workbook.sheets():
    #     col_num = booksheet.ncols
    #     for row in xrange(booksheet.nrows):
    #         for col in xrange(booksheet.ncols):
    #
    #             value = booksheet.cell(row, col).value
    #             if col ==0:
    #                 writeData = "{" + value + '", \n'
    #             else:
    #                 writeData = writeData + str(booksheet.cell(row,col).value) + '",\n'
    #         else:
    #             writeData = writeData + "}"
    # else:
    #     fileOutput.write(writeData)
    #
    # fileOutput.close()
    # data = {
    #
    # }
