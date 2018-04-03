import pymysql
from time import ctime
import re, threading

def Ulogin(username, password):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
    )
    cur = conn.cursor()
    aa = cur.execute('select count(id) from user where name=%s', username)
    print(aa)
    if aa == 0:
        print("The user is not exist")
        cur.close()
        conn.commit()
        conn.close()
        return '0'
    elif aa == 1:
        bb = cur.execute('select count(id) from user where name=%s AND password=%s', [username, password])
        if bb == 0:
            print('The password is not correct')
            cur.close()
            conn.commit()
            conn.close()
            return '1'
        if bb == 1:
            print('Login successfully')
            cc = cur.execute('select id from user where name=%s', username)
            cur.close()
            conn.commit()
            conn.close()
            return 'yes,'




                # def Rlogin(id,password):
                #     conn = pymysql.connect(
                #         host='localhost',
                #         port=3306,
                #         user='root',
                #         passwd='root',
                #         db='python',
                #     )
                #     cur = conn.cursor()
                #     aa = cur.execute('select count(id) from referee where id=%s',id)
                #     print (aa)
                #     if aa==0:
                #         print("The referee is not exist")
                #         cur.close()
                #         conn.commit()
                #         conn.close()
                #         return '0'
                #     elif aa==1:
                #         bb=cur.execute('select count(id) from referee where id=%s AND passwd=%s',[id,password])
                #         if bb==0:
                #             print ('The password is not correct')
                #             cur.close()
                #             conn.commit()
                #             conn.close()
                #             return '1'
                #         if bb==1:
                #             print ('Login successfully')
                #             cc=cur.execute('select id from referee where id=%s',id)
                #             cur.close()
                #             conn.commit()
                #             conn.close()
                #             return '2'
