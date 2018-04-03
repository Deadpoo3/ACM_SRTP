#include "mainwindow.h"
#include "ui_mainwindow.h"
#include"connection.h"
#include<QHBoxLayout>
#include<QGridLayout>
#include<QString>
#include<QFileDialog>
#include<QStringList>
#include<QDebug>
#include<QSqlError>
#include<QSqlDriver>
#include<QSqlField>
#include<QSqlQueryModel>
#include<QSqlTableModel>
#include<QSqlRelationalTableModel>
#include<QMessageBox>
#include<QTableView>
#include<QSqlDatabase>
#include<QSqlQuery>



MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
   ui->setupUi(this);

   model=new QSqlTableModel(this);
   model->setTable("students");
   model->select();
   model->setEditStrategy(QSqlTableModel::OnManualSubmit);
   ui->tableView->setModel(model);
}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_pushButton_6_clicked()
{
   openfile();
}
void MainWindow::openfile()
{
    fileName = QFileDialog::getOpenFileName(this);
    ui->pushButton->setEnabled(true);
    ui->lineEdit->setText(fileName);
}
void MainWindow::openfile1()
{
    fileName = QFileDialog::getOpenFileName(this);
    ui->pushButton->setEnabled(true);
    ui->lineEdit_2->setText(fileName);
}
void MainWindow::openfile2()
{
    fileName = QFileDialog::getOpenFileName(this);
    ui->pushButton->setEnabled(true);
    ui->lineEdit_3->setText(fileName);
}
void MainWindow::openfile3()
{
    fileName = QFileDialog::getOpenFileName(this);
    ui->pushButton->setEnabled(true);
    ui->lineEdit_4->setText(fileName);
}
void MainWindow::openfile4()
{
    fileName = QFileDialog::getOpenFileName(this);
    ui->pushButton->setEnabled(true);
    ui->lineEdit_5->setText(fileName);
}


void MainWindow::on_pushButton_7_clicked()
{
     openfile1();
}

void MainWindow::on_pushButton_8_clicked()
{
     openfile2();
}

void MainWindow::on_pushButton_9_clicked()
{
     openfile3();
}

void MainWindow::on_pushButton_10_clicked()
{
     openfile4();
}

void MainWindow::on_pushButton_2_clicked()
{
    QString filename=ui->lineEdit->text();
    QString filename2=ui->lineEdit_2->text();
    QString questionname=ui->lineEdit_6->text();
    QString input=ui->lineEdit_7->text();
    QString output=ui->lineEdit_8->text();
    QString answer=ui->lineEdit_9->text();
    QString testnum=ui->lineEdit_10->text();
    static int orderid=1;
      QSqlQuery query;
    bool ok=query.exec(QString("insert into students values(orderid,QString::fromUtf8(questionname),QString::fromUtf8(input),QString::fromUtf8(output),QString::fromUtf8(answer),testnum)"));
    query.exec(QString("create table students(id int primary key,""questionname varchar,input varchar,output varchar,answer varchar,filename varchar,testnum int)"));
     if(!ok)
     {
         qDebug("woqu");
     }

}


void MainWindow::on_pushButton_14_clicked()
{
    int curRow=ui->tableView->currentIndex().row();
    ui->tableView->setModel(model);
    //获取选中行、
    model->removeRow(curRow);
    int ok=QMessageBox::warning(this,"Are you sure?"
     ,"Are you sure to delete this one?",QMessageBox::Yes,QMessageBox::No);
    if(ok==QMessageBox::No)
    {
        model->revertAll();//??????????????

    }else{
        model->submitAll();
    }
}
void MainWindow::on_pushButton_16_clicked()
{
    model->submitAll();
}

void MainWindow::on_pushButton_13_clicked()
{
    ui->tableView->setModel(model);
    int rowNum=model->rowCount();
    static int id=5;
    model->insertRow(rowNum);
    model->setData(model->index(rowNum,0),id);
    id++;
    model->submitAll();
}

void MainWindow::on_pushButton_11_clicked()//?????????????????????????????????
{
    QString name=ui->lineEdit_11->text();
    model->setFilter(QString::fromUtf8("name=")+name);
    model->select();
}

void MainWindow::on_pushButton_12_clicked()
{
    model->setTable("students");
    model->select();
}

void MainWindow::on_pushButton_17_clicked()
{
    model->setSort(0,Qt::AscendingOrder);
    model->select();
}

void MainWindow::on_pushButton_18_clicked()
{
    tcpSocket->connectToHost("223.3.81.100",8181);
     connect(tcpSocket,SIGNAL(readyRead()),this,SLOT(readit()));
}
void MainWindow::readit()
{
    QByteArray bb;
    bb.resize(tcpSocket->bytesAvailable());
    tcpSocket->read(bb.data(),bb.size());
    ui->lineEdit_3->setText(bb.data());
}
