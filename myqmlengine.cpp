#include "myqmlengine.h"
#include <QDebug>
#include <QFile>
#include <QDir>
#include <QFileInfo>

static void getAllFilePath(QStringList& fileList, const QString& strDirPath) {
    QFileInfo info(strDirPath);
    if (!info.exists()) {
        return;
    }
    if (info.isFile()) {
        fileList.append(strDirPath);
        return;
    }
    QDir dir(strDirPath);
    const auto& list = dir.entryInfoList(QDir::Filter::NoDot | QDir::Filter::NoDotAndDotDot | QDir::Filter::Dirs | QDir::Filter::Files);
    foreach (const auto& info, list) {
       if (info.isFile()) {
           fileList.append(info.absoluteFilePath());
       } else {
           getAllFilePath(fileList, info.absoluteFilePath());
       }
    }
}

MyQmlEngine::MyQmlEngine(QObject *parent) : QQmlApplicationEngine(parent), m_loader(nullptr)
{

}

void MyQmlEngine::SetQmlPath(const QString& strPath) {
    getAllFilePath(m_fileList, strPath);
    m_watcher.addPaths(m_fileList);
    connect(&m_watcher, &QFileSystemWatcher::fileChanged, this, [this](const QString& url){
        qDebug() << "changed file: " << url;
        if (m_loader) {
            QMetaObject::invokeMethod(m_loader, "refresh");
        }
        m_watcher.removePaths(m_fileList);
        m_watcher.addPaths(m_fileList);
    });
}

void MyQmlEngine::SetEntryQmlFile(const QString& strFile) {
    this->load(strFile);
    const auto rootObject = this->rootObjects().first();
    if (rootObject) {
        m_loader = rootObject->findChild<QObject*>("sourceLoader");
    }    
}

void MyQmlEngine::clearCache()
{
    qDebug() << "Clear Cache";
    this->trimComponentCache();
    this->clearComponentCache();
}
