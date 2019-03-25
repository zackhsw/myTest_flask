import xlrd as xlrd
from flask_sqlalchemy import xrange
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

if __name__ == '__main__':
    user_id = 11
    SECRET_KEY = 'hard to get string'
    # Serializer(current_app.config['SECRET_KEY'], expires_in=expiration).dumps({'user_id': user_id})
    s = Serializer(SECRET_KEY, expires_in=604800)
    t = s.dumps({'user_id': user_id})
    token = t.decode('ascii')
    print(token)
    print('token--+-->', token, '<--+--')

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
    data = {

    }