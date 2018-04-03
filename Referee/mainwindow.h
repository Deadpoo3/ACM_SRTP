#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include<QString>
#include<QSqlTableModel>
#include<QTcpSocket>

namespace Ui {
class MainWindow;
class QSqlTableModel;
}



class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();


private slots:
    void openfile();
    void on_pushButton_6_clicked();
    void openfile1();
    void openfile2();
    void openfile3();
    void openfile4();
    void on_pushButton_7_clicked();

    void on_pushButton_8_clicked();

    void on_pushButton_9_clicked();

    void on_pushButton_10_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_14_clicked();

    void on_pushButton_13_clicked();

    void on_pushButton_16_clicked();

    void on_pushButton_11_clicked();

    void on_pushButton_12_clicked();

    void on_pushButton_17_clicked();

    void readit();


    void on_pushButton_18_clicked();

private:
    Ui::MainWindow *ui;
    QString fileName;
    QSqlTableModel *model;
    QTcpSocket* tcpSocket;
};

#endif // MAINWINDOW_H
