#2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

import pymysql

#数据库连接
mydb = pymysql.connect('localhost', 'root', 'gloriasxy630', 'homework')

#游标对象
mycursor = mydb.cursor()

#若表已存在，则删除
mycursor.execute('DROP TABLE IF EXISTS messageboard')

#新建messageboard表
sql1 = """CREATE TABLE messageboard (
        ID INT NOT NULL,
        COMMENT CHAR(50),
        USER_NAME CHAR(20),
        DATE CHAR(30),
        IS_DELETE INT
        )"""

#添加记录
sql2 = "INSERT INTO messageboard(ID, COMMENT, USER_NAME, DATE, IS_DELETE) VALUES (1, 'I love Python!', 'Gloria', '2020-5-20 20:46:13', 0)"
sql3 = "INSERT INTO messageboard(ID, COMMENT, USER_NAME, DATE, IS_DELETE) VALUES (2, 'Python loves me!', 'FZS', '2020-5-21 15:34:26', 1)"
sql4 = "INSERT INTO messageboard(ID, COMMENT, USER_NAME, DATE, IS_DELETE) VALUES (3, 'Work hard, play hard.', 'SXY', '2020-5-22 09:12:45', 0)"
#删除记录
sql5 = "DELETE FROM MESSAGEBOARD WHERE IS_DELETE = 0"
#修改记录
sql6 = "UPDATE MESSAGEBOARD SET USER_NAME = 'FZSPIG' WHERE USER_NAME = 'FZS'"
#查询记录
sql7 = "SELECT * FROM MESSAGEBOARD WHERE USER_NAME = 'Gloria'"

try:
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    mycursor.execute(sql3)
    mycursor.execute(sql4)
    #mycursor.execute(sql5)
    mycursor.execute(sql6)
    mycursor.execute(sql7)
    results = mycursor.fetchall()
    for row in results:
        id = row[0]
        comment = row[1]
        user_name = row[2]
        date = row[3]
        is_delete = row[4]
    print("id = {0}, comment = {1}, user_name = {2}, date = {3}, is_delete = {4}".format(id, comment, user_name, date, is_delete))

    mydb.commit()
except Exception as error:
    print("error:{0}".format(error))
    mydb.rollback()

mydb.close()

