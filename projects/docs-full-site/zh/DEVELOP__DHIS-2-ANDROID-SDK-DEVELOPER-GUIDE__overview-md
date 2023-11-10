---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/overview.md" 
---
# 总览

 <!--DHIS2-SECTION-ID:overview-->

DHIS2 Android SDK是一个库，它抽象了与DHIS2 Web API交互的复杂性。它旨在作为为DHIS2构建Android应用程序的起点，涵盖了任何Android应用程序应执行的一些任务，例如元数据和数据同步。

主要目标：

- **摘要DHIS2网络API **。无需对服务器执行api查询。 SDK包含与网络api交互的方法。
- **离线办公**。它实现了DHIS2模型的简化版本，该模型保留在本地数据库（SQLite）中。它确保执行数据输入任务所需的所有元数据可随时用于构建数据输入表单。可用连接时，数据将保存在本地并上传到服务器。
- **确保DHIS2兼容性**。它封装了DHIS2版本之间的更改，因此该应用程序不必关心它们。如果SDK进行了一些更改以适应新的DHIS2版本，则该应用程序可以在编译时安全地检测到这些更改。

## 技术概述

 <!--DHIS2-SECTION-ID:technology_overview-->

该SDK使用最低Android API版本中允许的简化功能子集以Java 8编写。 SDK使用某些Android特定的组件，例如库来创建页面列表（LiveData，PagedList）或访问文件系统。因此，目前** SDK仅可在Android环境中运行**。

它使用[RxJava]（https://github.com/ReactiveX/RxJava）促进某些方法的异步处理。尽管它是可选的，但我们建议您采用这种方法来确保非阻塞调用。

SDK内部使用的其他库包括：[Dagger]（https://github.com/google/dagger）用于依赖性注入，[Jackson]（https://github.com/FasterXML/jackson）用于JSON解析，[用于API通信的翻新版（https://square.github.io/retrofit/）和[OkHttpClient]（https://square.github.io/okhttp/）或[SQLBrite]（https://github.com/ square / sqlbrite）进行数据库迁移。


