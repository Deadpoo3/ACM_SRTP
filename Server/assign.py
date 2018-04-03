import pymysql
def getUNum():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
    )
    cur = conn.cursor()
    cur.execute("select count(id) from user ")
    aa=cur.fetchall()[0][0]
    cur.close()
    conn.commit()
    conn.close()
    return aa

def getR():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
    )
    cur=conn.cursor()
    cur.execute("select count(id) from referee")
    rr=cur.fetchall()[0][0]
    bb=cur.execute("select num from referee where id=%s",[rr])
    res=1
    if bb==5:
        insertR = "insert into referee values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(insertR, (rr + 1,0,0,0,0,0,0))
        res=rr+1
    else:
        res=rr
    cur.close()
    conn.commit()
    conn.close()
    return res
def register(username,passwd):
    aa=getUNum()
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
    )
    cur = conn.cursor()
    re=getR()
    aaa=aa+1
    print(aaa)
    cur.execute("insert into user values(%s,%s,%s,%s)",[aaa,username,passwd,re])
    cur.execute("select num from referee where id=%s",[re])
    Rnum=cur.fetchall()[0][0]
    cur.execute("update referee set num = %s",Rnum)
    cur.close()
    conn.commit()
    conn.close()