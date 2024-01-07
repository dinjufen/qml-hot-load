# qml-hot-load
A QML hot load demo

## 原理
1. 监听文件变化
2. 清除QML缓存
3. 重新加载QML文件
4. 注意：为了实时效果，只能从本地路径加载qml文件，而不能从qrc加载，实际开发中可以做区分
##