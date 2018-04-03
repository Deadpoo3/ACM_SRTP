#include "mainwindow.h"
#include <QApplication>
#include<QSqlDatabase>
#include<QStringList>
#include<QDebug>
#include<QSqlQuery>
#include"connection.h"
#include<QTextCodec>
#include<QCoreApplication>
#include<QtXml>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
   // QTextCodec::toUnicode(QTextCodec::codecForName("UTF-8"));
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
    if(!createConnection())
        return 1;
  // QCoreApplication a(argc,argv);
   //QCoreApplication doc;
  // QDomProcessingInstruction instruction;

    MainWindow w;
    w.show();

    return a.exec();
}
