#include <QGuiApplication>
#include "myqmlengine.h"
#include <QFileSystemWatcher>
#include <QQmlContext>

int main(int argc, char *argv[])
{
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
    QGuiApplication app(argc, argv);
//    QFileSystemWatcher *watcher = new QFileSystemWatcher(&app);
//    watcher->addPath("C:/Users/Administrator/code/my/cpp/qmltest/qml");
//    QObject::connect(watcher, &QFileSystemWatcher::fileChanged, [](const QString &path){
//        qDebug() << "file changed: " << path;
//    });
    MyQmlEngine engine;
    engine.rootContext()->setContextProperty("$QmlEngine", &engine);
    if (argc <= 1) {
        return -1;
    }
    const QUrl url(argv[1]);
    qDebug() << "url: " << url;
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);
    return app.exec();
}
