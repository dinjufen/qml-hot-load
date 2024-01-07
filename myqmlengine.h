#ifndef MYQMLENGINE_H
#define MYQMLENGINE_H

#include <QQmlApplicationEngine>
#include <QFileSystemWatcher>
#include <QString>
#include <QStringList>

class MyQmlEngine : public QQmlApplicationEngine
{
    Q_OBJECT
public:
    explicit MyQmlEngine(QObject *parent = nullptr);

    void SetQmlPath(const QString& strPath);

    void SetEntryQmlFile(const QString& strFile);

    Q_INVOKABLE void clearCache();

private:
    QFileSystemWatcher m_watcher;
    QStringList m_fileList;
    QObject* m_loader;
};

#endif // MYQMLENGINE_H
