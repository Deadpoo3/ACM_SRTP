#!/usr/bin/python
# ! -*- coding: utf8 -*-

import lorun
import os
import pymysql

RESULT_STR = [
    'Accepted',
    'Presentation Error',
    'Time Limit Exceeded',
    'Memory Limit Exceeded',
    'Wrong Answer',
    'Runtime Error',
    'Output Limit Exceeded',
    'Compile Error',
    'System Error'
]


def compileSrc(src_path):
    if os.system('gcc %s -o m' % src_path) != 0:
        print('compile failure!')
        return False
    return True


def runone(p_path, in_path, out_path):
    fin = open(in_path)
    ftemp = open('temp.out', 'w')

    runcfg = {
        'args': ['./m'],
        'fd_in': fin.fileno(),
        'fd_out': ftemp.fileno(),
        'timelimit': 1000,  # in MS
        'memorylimit': 20000,  # in KB
    }

    rst = lorun.run(runcfg)
    fin.close()
    ftemp.close()
    if rst['result'] == 0:
        ftemp = open('temp.out')
        fout = open(out_path)
        crst = lorun.check(fout.fileno(), ftemp.fileno())
        fout.close()
        ftemp.close()
        os.remove('temp.out')
        if crst != 0:
            return {'result': crst}

    return rst


def judge(src_path, td_path, td_total,id,name,question):
    if not compileSrc(src_path):
        return
    for i in range(td_total):
        in_path = os.path.join(td_path, '%d.in' % i)
        out_path = os.path.join(td_path, '%d.out' % i)
        if os.path.isfile(in_path) and os.path.isfile(out_path):
            rst = runone('./m', in_path, out_path)
            rst['result'] = RESULT_STR[rst['result']]
            print(rst)
        else:
            print('testdata:%d incompleted' % i)
            os.remove('./m')
            exit(-1)
    os.remove('./m')
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
    )
    cur = conn.cursor()
    cur.exec("insert into submit VALUES (%s,%s,%s,%s,%s,%s,%s)", [id, name, question, rst, 'yes', 'yes', src_path])


# if __name__ == '__main__':
#     import sys
#     judge('/home/romanov/Yuan/main.c','/home/romanov/Test/',2)
