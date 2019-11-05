import MySQLdb

# 打开数据库连接
conn = MySQLdb.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='root123',
                       db="flask_news",
                       )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show databases;")
cursor.execute("use database_name;")
cursor.execute("show tables;")
cursor.execute("select * from tables_name")

# 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
for item in data:
    print(item)

# 关闭数据库连接
cursor.close()