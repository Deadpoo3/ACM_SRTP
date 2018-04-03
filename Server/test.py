import pymysql, re

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='python',
)
cur = conn.cursor()
cur.execute("select S.url from submit S where S.name=%s", ['du'])
aa = str(cur.fetchall())
aa = re.findall('\'(.+?)\'', aa)
ss = ""
for i in range(0, len(aa)):
    ss += aa[i]
print(ss)
