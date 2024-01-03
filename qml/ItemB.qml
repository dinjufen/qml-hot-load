import QtQuick 2.15

Item {
    width: 400;height: 300;
    property string text: "Hello World";
    Rectangle {
        x: 100; y: 50;
        height: 100
        width: height * 2

        color: "blue"
        MouseArea {
            anchors.fill: parent
            onClicked: console.log("123123")
        }
    }

    Rectangle {
        x: 100; y: 120;
        height: 180
        width: height * 2
        color: "red"
    }

    Text {
        x: 100; y: 100;
        text: text
    }
}
