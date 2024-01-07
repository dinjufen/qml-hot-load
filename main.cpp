#include <QGuiApplication>
#include "myqmlengine.h"
#include <QQmlContext>

int main(int argc, char *argv[])
{
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
    QGuiApplication app(argc, argv);
    MyQmlEngine engine;
    engine.rootContext()->setContextProperty("$QmlEngine", &engine);
    const QString strEntry = QString(CURRENT_DIR) + "/main.qml";
    qDebug() << "url: " << strEntry;
    engine.SetEntryQmlFile(strEntry);
    engine.SetQmlPath(QString(CURRENT_DIR) + "/qml");
    return app.exec();
}
