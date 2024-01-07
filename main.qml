import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: root
    width: 1440
    height: 720
    visible: true
    title: qsTr("Hello World")

    property string url: "qml/ItemA.qml"

    Loader {
        id: loader
        objectName: "sourceLoader"
        source: url
        onLoaded: {
            loader.width = item.width
            loader.height = item.height
        }
        function refresh() {
            loader.source = ""
            $QmlEngine.clearCache()
            loader.source = url
        }
    }

    Button {
        text: "Refresh"
        onClicked: loader.refresh()
    }

}
