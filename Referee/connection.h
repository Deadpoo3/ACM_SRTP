#ifndef CONNECTION_H
#define CONNECTION_H
#include<QMessageBox>
#include<QSqlDatabase>
#include<QSqlQuery>
#include<QString>

static bool createConnection()
{
    QSqlDatabase db=QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("my.db");
    if(! db.open())
    {
        QMessageBox::critical(0,"Connot open database1",
             "Unable to establish a database connection.",QMessageBox::Cancel);
        return false;
    }
    QSqlQuery query;
    query.exec(QString("create table students(id int primary key,""name varchar,itemquestion int,answerstatus varchar,question varchar)"));
    query.exec(QString("insert into students values(1,'李强',11,'提交','C++的继承')"));
    query.exec(QString("insert into students values(2,'马亮',11,'未提交','JAVA的应用')"));
    query.exec(QString("insert into students values(3,'孙红',12，'未提交','JAVA的解析')"));

    query.exec(QString("create table students(id int primary key,""questionname varchar,input varchar,output varchar,answer varchar,filename varchar,testnum int)"));

    query.exec(QString("create table course(id int primary key,"
                       "name varchar,teacher varchar)"));
    query.exec(QString("insert into course values(10,'数学','王老师')"));
    query.exec(QString("insert into course values(11,'英语','张老师')"));
    query.exec(QString("insert into course values(12,'计算机','白老师')"));
    return true;
}

#endif // CONNECTION_H
