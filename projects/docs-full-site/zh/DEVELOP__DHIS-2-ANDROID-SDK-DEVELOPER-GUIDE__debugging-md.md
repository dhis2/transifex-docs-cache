---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/debugging.md" 
---
# 调试

 <!--DHIS2-SECTION-ID:debugging-->

除了AndroidStudio中的常规调试工具外，[Stetho]（http://facebook.github.io/stetho/）库还允许使用Chrome开发者工具来调试网络流量并浏览数据库。

通过在gradle文件中添加以下依赖项来设置Stetho：

```等级
依赖项{
    实施'com.facebook.stetho：stetho：1.5.0'
    实施'com.facebook.stetho：stetho-okhttp3：1.5.0'
}
```

然后在`D2Configuration`对象中添加一个网络拦截器：

```java
D2Configuration.builder()
    ...
    .networkInterceptors(Collections.singletonList(new StethoInterceptor()))
    ...
    .build();
```

最后在`Application`类中启用初始化Stetho：

```java
if (DEBUG) {
    Stetho.initializeWithDefaults(this);
}
```

此时，您应该可以使用Chrome Inspector工具调试app / sdk：

- 在调试模式下运行测试并设置断点。
- 在Chrome浏览器中，打开[设备检查器]（chrome：// inspect / devices＃devices）。
- 选择远程目标，然后单击检查。将出现一个新窗口，显示Chrome开发人员工具。
- 在“资源> Web SQL”中浏览数据库。
- 在“网络”中浏览网络流量。


