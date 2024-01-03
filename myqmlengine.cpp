#include "myqmlengine.h"
#include <QDebug>

MyQmlEngine::MyQmlEngine(QObject *parent) : QQmlApplicationEngine(parent)
{

}

void MyQmlEngine::clearCache()
{
    qDebug() << "Clear Cache";
    this->trimComponentCache();
    this->clearComponentCache();
}
