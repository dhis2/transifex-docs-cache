---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/configure-the-gis-app.md"
revision_date: "2021-06-14"
---

# 配置地图应用 { #gis_creating }

## 语境 { #gis_creating_context }

设置地图仅意味着存储组织的坐标
您要在数据库中的地图上显示的单位。座标经常
以专有格式分发，需要将其转换为
DHIS2可以理解的格式。 ESRI shapefile是最常见的
桌面应用程序的地理空间矢量数据格式。你可能会发现
您国家/地区的shapefile [此处]（http://www.diva-gis.org/gdata）或
网络上的许多其他地理空间数据存储库。一些工作
为了在DHIS2 GIS中使用这些坐标，需要完成操作，即
将数据转换为合适的格式并确保名称
包含在地理空间数据中的名称与
他们应该匹配的组织单位。

通过POINT只能编辑具有POINT几何类型的组织单位。
此时的维护应用程序。要修改POLYGON几何形状，请联系
GML导入功能。

To edit the POINT coordinates of an organisation unit, open the Maintenance App and navigate to the Organisation Unit section. Click on the Organisation Unit you would like to view or edit, you can search or filter the list from on the left-hand side of the screen. Once an organisation unit is selected, you can edit the **Latitude** and **Longitude** values to update the POINT coordinates. If the Organisation Unit has a POLYGON geometry, the coordinates cannot be edited.

如果要添加或更新大量单位的坐标，或者
如果您需要更新多边形的几何形状，则应使用自动GML
进口。以下部分说明了如何执行GML导入。

> **重要**
>
> DHIS2 支持的唯一坐标参考系是 EPSG:4326，也称为地理经度/纬度。坐标必须以经度（东/西位置）和纬度（北/南位置）存储。如果您的矢量数据位于与 EPSG 4326 不同的 CRS 中，则您需要先重新投影数据，然后再导入 DHIS2。

## 导入坐标 { #gis_creating_setup }

第1步-简化/概括您的地理数据

地理数据文件中的边界通常也非常准确
对于基于Web的GIS的需求尤其如此。这通常不影响
在本地系统上使用GIS文件时的性能，但这是
通常需要优化基于Web的地理数据
DHIS2的GIS系统。所有地理数据都需要从以下位置下载
服务器并在浏览器中呈现，因此，如果数据过于复杂，
DHIS2 GIS的性能将受到负面影响。这个
优化过程可以描述如下：

坐标：有效的小数位数（例如
23.02937874993774）应缩短为更少的数字（例如23.03）。
尽管这样做会导致地图上出现一些错误，但鉴于
在DHIS2中生成地图的通常比例（\> 1：50,000），损失
精度不应该引起注意。通常不超过四个
小数点后必须有有效数字。，
多边形：除了缩短有效位数之外，
实际点数也应减少到最佳水平。
找到这个最佳水平可能需要一些实验。减少
点的精度以及通过的点数
泛化，将导致多边形退化。但是，之后
进行一些实验，可以得出最佳的概括水平
发现，在视觉上可接受的多边形精度，以及
GIS的性能是最佳的。

对于多边形，我们需要使边界线的详细程度降低
删除一些线点。备份您的shapefile
在你开始之前。一种可能的方法是使用
[MapShaper]（http://www.mapshaper.org/）是一种在线工具，可以
用于概括地理数据。要使用MapShaper，只需上传
您的shapefile到站点。然后，在中央底部看到一个滑块
从0％开始。通常可以将其拖动到大约80％。
在左侧菜单中，您可以选中“显示原始行”以比较
结果，您可能需要尝试使用其他简化方法。
当您对结果感到满意时，请点击右上角的“导出”
角。然后检查名为“ Shapefile-
多边形”，点击“创建”，然后等待下载按钮出现。
现在，将这两个文件下载到本地计算机并覆盖
现有的。使用新的简化版继续进行下一步
shapefile。

第2步-将shapefile转换为GML

The recommended tool for geographical format conversions is called "ogr2ogr". This should be available for most Linux distributions `sudo apt-get install gdal-bin`. For Windows, go to <http://fwtools.maptools.org/>and download "FWTools", install it and open up the FWTools command shell. During the format conversion we also want to ensure that the output has the correct coordinate projection (called EPSG:4326 with geographic longitude and latitude). For a more detailed reference of geographic coordinates, please refer to this [site](http://www.epsg-registry.org/). If you have already reprojected the geographic data to the geographic latitude/longitude (EPSG:4326) system, there is no need to explicitly define the output coordinate system, assuming that `ogr2ogr` can determine the input spatial reference system. Note that most shapefiles are using the EPSG:4326 system. You can determine the spatial reference system by executing the following command.

    ogrinfo -al -so 文件名.shp

假设`ogrinfo`报告的预测为EPSG：27700，
我们可以通过执行以下命令将其转换为EPSG：4326
    命令。

    ogr2ogr -s_srs EPSG：27700 -t_srs EPSG：4326 -f GML filename.gml filename.shp

如果地理数据已经在EPSG：4326中，则只需进行转换
通过执行以下命令将shapefile转换为GML。

    ogr2ogr -f GML 文件名.gml 文件名.shp

您将在shapefile所在的文件夹中找到创建的GML文件。

第3步-准备GML文件

不幸的是，GML文件尚未准备好导入。在其中打开
强大的文本编辑器，例如Geany（Linux）或Notepad ++（Windows）。 GML是
基于XML的格式，这意味着您将识别常规XML
标签层次结构。在GML文件中，组织单位表示为
\ <gml:featureMember\>。在功能成员内部，我们通常会发现很多
属性，但是我们只是要导入它们的坐标。

In order to import geospatial data from the feature members of the GML input, DHIS2 must match each of them with an organisation unit in its database. The feature member element must, in other words, contain a reference to its corresponding organisation unit. The reference itself must be one of three possible DHIS2 identifiers: **uid**, **code** or **name**. The identifier of choice must be provided as a property for each feature member element. The importer will look for a property with the local name of either _Uid_, _Code_ or _Name_, e.g. "ogr:Name" or "anyPrefix:Code".

如果您的功能成员已经包含标识符的属性，则您
希望使用（例如区域名称）可以使用搜索和替换
在文本编辑器中将这些元素重命名为DHIS2将识别的名称
（请参见下表）。这通常是适用的工作流程
使用名称作为标识符时（源shapefile甚至GML
通常会包含其定义的每个区域的名称）。

 <table>
 <caption>GML导入支持的组织单位标识符</caption>
 <thead>
 <tr class="header">
 <th>匹配优先级</th>
 <th>标识符</th>
 <th>有效拼写</th>
 <th>保证唯一的</th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> 1 </td>
 <td> Uid </td>
 <td>uid，Uid，UID</td>
 <td>是</td>
 </tr>
 <tr class="even">
 <td> 2 </td>
 <td>代码</td>
 <td>代码，代码，代码</td>
 <td>否</td>
 </tr>
 <tr class="odd">
 <td> 3 </td>
 <td>名称</td>
<td> 名称，名称，名称</td>
 <td>否</td>
 </tr>
 </tbody>
 </table>

In the case of renaming properties one would usually find a tag named something like "ogr:DISTRICT_NAME", "ogr:NAME_1" and rename it to "ogr:Name". If using the _code_ or _uid_ identifiers on the other hand, looking up the correct values in the DHIS2 database and going through the GML file, adding the properties for each corresponding feature member might be necessary. In any of the cases it is important to realize that the identifier used must **uniquely** identify an organisation unit (e.g. if there are two organisation units in the database of the same name or code, these cannot be matched properly on either). As _uid_ is the only guaranteed-to-be-unique identifier it is the most robust choice. However, as matching on name is usually easier (given that the name is already part of your data), a viable approach to solving uniqueness conflicts can be to match any non-uniquely named organisation units on a different identifier (uid, preferably) and the rest on their names.

如上表所示，有一个匹配的优先级，即
为同一功能成员提供了两个或多个标识符，
匹配将在最高优先级的标识符上执行。另请注意
GML中可以使用的有效属性。命名空间前缀
不重要，因为仅使用本地名称。

执行 GML 文件准备时的一个常见陷阱是语法或元素命名错误。因此，请确保 GML 文件的所有属性都以正确对应的标签启动和终止。还要确保属性遵循给定的属性名称的有效拼写。识别属性应该看起来像例如\<ogr:Name\>莫扬巴区\</ogr:Name\>、\<somePrefix:uid\>x7uuia898nJ\</somePrefix:uid\> 或 \<CODE\>OU_12345\</CODE\>。另一个常见错误是不确保标识符完全匹配，尤其是在使用 _name_ 属性时。所有匹配均根据精确值执行，这意味着源 GML 文件中的“Moyamba”不会与数据库中的“Moyamba District”进行匹配。

简要查看标识符，并将其与
数据库中的相应值。如果它们看起来相当不错，
现在是时候在import-export模块中进行预览了。

转到服务->导入导出，选择“预览”，选择GML文件
然后点击“导入”。寻找新的/更新的组织单位。我们的
目的是向已经存在的组织单位添加坐标
在数据库中，因此我们需要尽可能多的更新和0个新更新。那些
列为新的将被创建为根单元并弄乱组织
DHIS2中的单位树。如果有任何列出为新的，请单击数字和
有问题的组织单位将显示在下面的列表中。如果有
与“”中的单位部门名称相比，有任何轻微的拼写错误
数据库-修复它们并再次进行预览。否则，请点击
列表下方的“全部放弃”按钮，然后“全部导入”按钮
在列表上方。

如果导入过程成功完成，您现在应该可以
利用DHIS2 GIS中的地理数据。如果没有，请检查日志
寻找提示并查找常见错误，例如：

\-名称在GML文件中重复。数据库中的名称列为
唯一，并且不接受两个具有相同名称的组织单位。

\-数据库中organizationalunit表中的“ shortname”列
varchar定义太小。将其增加到100。

\-GML文件中的特殊名称字符。确保将它们转换为
适当的XML等效项或转义序列。

\-输入GML格式错误，标签不匹配
