# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.5.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x02\xa7\
i\
mport QtQuick 2.\
15\x0d\x0aimport QtQui\
ck.Window 2.15\x0d\x0a\
import QtQuick.C\
ontrols 2.15\x0d\x0a\x0d\x0a\
Window {\x0d\x0a    id\
: root\x0d\x0a    widt\
h: 1440\x0d\x0a    hei\
ght: 720\x0d\x0a    vi\
sible: true\x0d\x0a   \
 title: qsTr(\x22He\
llo World\x22)\x0d\x0a\x0d\x0a \
   property stri\
ng url: \x22qml/Ite\
mA.qml\x22\x0d\x0a\x0d\x0a    L\
oader {\x0d\x0a       \
 id: loader\x0d\x0a   \
     objectName:\
 \x22sourceLoader\x22\x0d\
\x0a        source:\
 url\x0d\x0a        on\
Loaded: {\x0d\x0a     \
       loader.wi\
dth = item.width\
\x0d\x0a            lo\
ader.height = it\
em.height\x0d\x0a     \
   }\x0d\x0a        fu\
nction refresh()\
 {\x0d\x0a            \
loader.source = \
\x22\x22\x0d\x0a            \
$QmlEngine.clear\
Cache()\x0d\x0a       \
     loader.sour\
ce = url\x0d\x0a      \
  }\x0d\x0a    }\x0d\x0a\x0d\x0a  \
  Button {\x0d\x0a    \
    text: \x22Refre\
sh\x22\x0d\x0a        onC\
licked: loader.r\
efresh()\x0d\x0a    }\x0d\
\x0a\x0d\x0a}\x0d\x0a\
\x00\x00\x02\x0d\
i\
mport QtQuick 2.\
15\x0d\x0a\x0d\x0aItem {\x0d\x0a  \
  width: 400;hei\
ght: 300;\x0d\x0a    p\
roperty string t\
ext: \x22Hello Worl\
d\x22;\x0d\x0a    Rectang\
le {\x0d\x0a        x:\
 100; y: 50;\x0d\x0a  \
      height: 10\
0\x0d\x0a        width\
: height * 2\x0d\x0a\x0d\x0a\
        color: \x22\
blue\x22\x0d\x0a        M\
ouseArea {\x0d\x0a    \
        anchors.\
fill: parent\x0d\x0a  \
          onClic\
ked: console.log\
(\x22123123\x22)\x0d\x0a    \
    }\x0d\x0a    }\x0d\x0a\x0d\x0a\
    Rectangle {\x0d\
\x0a        x: 100;\
 y: 120;\x0d\x0a      \
  height: 180\x0d\x0a \
       width: he\
ight * 2\x0d\x0a      \
  color: \x22red\x22\x0d\x0a\
    }\x0d\x0a\x0d\x0a    Tex\
t {\x0d\x0a        x: \
100; y: 100;\x0d\x0a  \
      text: text\
\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x02\x0f\
i\
mport QtQuick 2.\
15\x0d\x0a\x0d\x0aItem {\x0d\x0a  \
  width: 400;hei\
ght: 300;\x0d\x0a    p\
roperty string t\
ext: \x22Hello Worl\
d\x22;\x0d\x0a    Rectang\
le {\x0d\x0a        x:\
 100; y: 50;\x0d\x0a  \
      height: 10\
0\x0d\x0a        width\
: height * 2\x0d\x0a\x0d\x0a\
        color: \x22\
lightblue\x22\x0d\x0a    \
    MouseArea {\x0d\
\x0a            anc\
hors.fill: paren\
t\x0d\x0a            o\
nClicked: consol\
e.log(\x22234\x22)\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
\x0d\x0a    Rectangle \
{\x0d\x0a        x: 10\
0; y: 120;\x0d\x0a    \
    height: 140\x0d\
\x0a        width: \
height * 2\x0d\x0a    \
    color: \x22red\x22\
\x0d\x0a    }\x0d\x0a\x0d\x0a    T\
ext {\x0d\x0a        x\
: 100; y: 100;\x0d\x0a\
        text: te\
xt\x0d\x0a    }\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x09\
\x0c\x15\xf9|\
\x00I\
\x00t\x00e\x00m\x00B\x00.\x00q\x00m\x00l\
\x00\x09\
\x0c\x14\xf9|\
\x00I\
\x00t\x00e\x00m\x00A\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8c\xe1\xc49_\
\x00\x00\x00:\x00\x00\x00\x00\x00\x01\x00\x00\x04\xbc\
\x00\x00\x01\x8c\xe1\xff\x19\xe1\
\x00\x00\x00\x22\x00\x00\x00\x00\x00\x01\x00\x00\x02\xab\
\x00\x00\x01\x8c\xca\xc9\xa7l\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
