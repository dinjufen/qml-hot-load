#ifndef MYQMLENGINE_H
#define MYQMLENGINE_H

#include <QQmlApplicationEngine>

class MyQmlEngine : public QQmlApplicationEngine
{
    Q_OBJECT
public:
    explicit MyQmlEngine(QObject *parent = nullptr);

    Q_INVOKABLE void clearCache();
};

#endif // MYQMLENGINE_H
