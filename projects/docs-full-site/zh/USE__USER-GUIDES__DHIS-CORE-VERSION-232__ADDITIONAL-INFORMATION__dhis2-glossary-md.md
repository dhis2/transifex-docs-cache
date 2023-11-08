---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.32/src/commonmark/en/content/user/dhis2-glossary.md"
revision_date: '2018-09-26'
---

# DHIS2词汇表 { #dhis2_glossary } 

 <!--DHIS2-SECTION-ID:dhis2_glossary-->

  - 聚合
    在DHIS2的上下文中，聚合是指数据元素如何
    结合在特定的层次关系中。作为一个
    例如，特定地区的所有医疗机构
    贡献给特定地区的总价值
    题。内部支持不同的聚合运算符
    DHIS2，例如SUM，AVERAGE和COUNT。

  - 分析工具
    分析是指处理和准备数据的过程
    已以更大的格式输入到DHIS2中
    适用于检索指标和汇总数据。当数据是
    输入DHIS2，它以一种针对以下情况优化的格式存储
    写入数据。但是，当数据需要处理成
    指标或汇总（例如，从几个月到季度），
    高效地以不同格式转换和存储此数据
    针对只读操作进行了优化。的分析系统
    DHIS2被分析应用程序广泛使用（GIS，数据透视表，
    活动报告等）。

    重要的是要记住，因为
    输入DHIS2的文件必须处理成分析格式，
    分析应用中显示的数据仅代表数据
    这是上次运行分析时系统中存在的。如果
    之后输入数据，则需要运行分析
    再次将这些数据显示在分析应用中。

  - 汇总数据
    在DHIS2的上下文中，汇总数据是指这两个数据
    从其他衍生的元素或指标
    分层数据源。例如，汇总设施数据
    将由所有患有以下疾病的患者的总数得出
    参加该设施的特定服务。聚集区
    数据将来自所有设施的总计
    包含在特定区域中。

  - 应用程序接口
    应用程序编程接口是有关如何
    不同的软件组件应相互交互。的
    DHIS2 API（或WebAPI）可用于将DHIS2与其他接口
    软件，以生成报告或自定义数据输入表单。

  - 批准书
    批准可用于控制广告的可见性和可编辑性
    数据。从最低报告级别提交数据时，它可以
    由下一个更高级别批准。该批准具有两个作用：

    1.  在以下位置的数据输入屏幕中不再能够编辑数据
        较低的水平。

    2.  根据已启用的系统设置，
        数据将在批准级别上可见。

    例如，在设施级别输入数据，然后
    提交批准。数据在
    区级别，数据将被锁定在数据条目中
    设施级别的屏幕。它也将在
    区域用户的分析应用程序。

<!-- end list -->

  - 双月刊
    指两个月的时间段，例如1月1日至2月28日。

<!-- end list -->

  - 类别
    类别是类别选项的组。用于
    组合以分解数据元素。类别通常是
    单一类型的概念，例如“年龄”或“性别”。

  - 类别组合
    类别组合用于分解数据元素。作为一个
    例如，数据元素“已确诊的疟疾病例数”
    可以细分为以下类别：“年龄”和
    “性别”。反过来，这些类别中的每一个都将包含几个
    类别选项，例如针对性别的“男”和“女”
    类别。类别组合可以包含一个或多个
    类别。

  - 类别组合选项
    类别组合选项由所有
    组成类别的类别选项的不同组合
    组合。例如，两个类别“性别”和“年龄”可能
    具有“男性” /“女性”和“ \ <5 years"/"\> 5年”等选项。
    类别组合选项将包括：

    （男性/ \ <5岁）

    （男/ \> 5岁）

    （女性/ \ <5岁）

    （女/ \> 5岁）

  - 类别选项
    类别选项是归类为原子元素
    类别。

  - 逗号分隔值
    逗号分隔的值是存储在表格中的一系列表格数据
    纯文本格式。它们通常与DHIS2一起用于导出和
    导入数据值。

<!-- end list -->

  - 数据字典
    可以交换的数据元素和指标的集合
    与其他DHIS2系统。通常用于定义一组数据
    设置DHIS2系统时的注意事项和指示灯。

  - 数据交换格式
    在DHIS2的上下文中，“数据交换格式”是指XML
    实现数据和元数据之间的传输的模式
    脱机的DHIS2实例以及不同实例之间
    支持DXF模式的应用程序。

  - 数据库
    DHIS2中的一组数据库表，其中包含已处理的数据
    基于聚合生成的元素和指标值
    规则以及计算的数据元素和指标公式。数据库
    表用于分析和报告生成。通常，用户
    不应直接使用未汇总的数据值，而应
    具有从数据集市导出以进行分析得出的值。

  - 数据元素
    数据元素是DHIS2的基本构建块。它是一个
    具有明确含义的数据的原子单位。本质上是
    实际观察或记录的数据值是
    进一步以许多尺寸为特征。例如
    数据元素“获得完全免疫的儿童人数”是指
    接受这项特殊服务的儿童人数。数据
    元素总是与期间以及组织相关联
    单元。它们可以可选地链接到其他尺寸。

  - 数据元素组
    数据元素组用于对多个数据元素进行分类
    根据常见主题，例如“免疫”或“ ART”。
    通常，它们在报告和分析期间用于
    相关数据元素一起分析。

  - 数据元素组集
    数据元素组用于对多个数据元素进行分类
    组成一个共同的主题。

  - 尺寸
    维度用于在分析过程中对数据元素进行分类。
    维度提供了一种根据以下内容对数据进行分组和过滤的机制
    共同特点。通常，相关的数据元素可能是
    在分析过程中使用维进行汇总或过滤。
    维度可以是层次结构的成员。例如“期间”
    维度可以细分为“日-\>月-\>季度-\>年”。

  - DXF

<!-- end list -->

  - 健康管理信息系统
    通常，用于记录的电子数据库系统
    有关服务提供，疾病发生率，人类的汇总数据
    资源数据和其他用于评估绩效的信息
    提供卫生服务。通常，HMIS不包含
    电子病历系统的高度详细的数据或
    个别患者数据。

<!-- end list -->

  - 指示符
    指标的除数。可以由多个数据组成
    元素与指标公式的使用。

    这显然是一个非常笼统的例子。分子和
    指标本身可以由各种数据元素组成，
    因子和四个基本操作数（加法，乘法，
    除法和减法）。

<!-- end list -->

  - 分子
    指标的红利。可以由多个数据组成
    要素和因素与指标公式的使用。

<!-- end list -->

  - 组织单位
    组织单位通常是一个地理单位，存在
    在层次结构中。例如，在美国，“乔治亚州”
    将被视为组织单位级别的组织单位
    的“国家”。组织单位还可以用于指定
    行政单位，例如医院内的病房。的
    组织单位维度实质上指定了“哪里”
    发生特定数据值。

  - 组织单位级别
    指组织层次结构中的级别。通常，
    国家在不同的级别进行管理，例如1）国家
    2）州3）县4）卫生设施。在DHIS2的背景下，
    医疗机构通常是最低的组织单位级别。数据是
    从最低的组织单位级别到最高的组织向上聚集。

<!-- end list -->

  - 期
    周期是由开始日期组成的特定时间间隔
    和结束日期。例如，“ 2011年1月”指的是时间
    2011年1月1日至2011年1月31日的时间间隔。

<!-- end list -->

  - 唯一标识符
    唯一标识符（UID）是字母和
    DHIS2用于标识特定资源的数字。 UID开始
    带有字母，并紧跟10个字母或数字。

# {＃AlSaid2010}

 <!--DHIS2-SECTION-ID:AlSaid2010--> Said Salah Eldin Al Said健康
苏丹的信息系统奥斯陆大学，2010年
 <http://urn.nb.no/URN:NBN:no-27062>

 <!--DHIS2-SECTION-ID:Berg2007--> Eivind Anders Berg的挑战
在越南实施健康信息系统
奥斯陆2007 <http://urn.nb.no/URN:NBN:no-15021>

 <!--DHIS2-SECTION-ID:BraaHedeberg2002-->JørnBraa Calle Hedberg奋斗
南非基于地区的健康信息系统
信息社会18113-127 2002
 <http://search.ebscohost.com/login.aspx?direct=true&db=aph&AN=6705438&site=ehost-live>

 <!--DHIS2-SECTION-ID:BraaNetworksAction2004--> Eric; BraaJørn;蒙泰罗
Sundeep Sahay行动网络：可持续健康信息系统
整个发展中国家的MIS季刊2004年3月28日
 <http://aisel.aisnet.org/misq/vol28/iss3/3/>

 <!--DHIS2-SECTION-ID:Brucker2007-->ØyvindFBrucker国际化和
本地化-来自HISP的案例研究奥斯陆大学，2007年
 <http://urn.nb.no/URN:NBN:no-15774>

 <!--DHIS2-SECTION-ID:Damitew2005--> Hirut Gebrekidan Damitew Netsanet
Haile Gebreyesus的可持续性和健康信息的最佳利用
系统奥斯陆大学2005 <http://urn.nb.no/URN:NBN:no-11506>

 <!--DHIS2-SECTION-ID:Jacucci06exploringtensions--> Ved Anfinsen Edoardo
Jacucci Cover Inger S在信息系统中的探索张力
标准化来自挪威和南部医疗保健的两个案例研究
非洲2006 <http://folk.uio.no/edoardo/MatNatAvh_Jacucci_rettet.pdf>

 <!--DHIS2-SECTION-ID:Gjendem2008--> Anders Gjendem招聘，培训，
交流和开源奥斯陆大学，2008年
 <http://urn.nb.no/URN:NBN:no-19821>

 <!--DHIS2-SECTION-ID:Gjerull2006--> Nils Fredrik Gjerull开源软件
发展中国家的发展奥斯陆大学2006
 <http://urn.nb.no/URN:NBN:no-13117>

 <!--DHIS2-SECTION-ID:Heldre2006--> Thor Helge Heldre对健康的研究
坦桑尼亚的信息系统试点项目奥斯陆大学2006
 <http://urn.nb.no/URN:NBN:no-12362>

 <!--DHIS2-SECTION-ID:Jacobsen2006--> Petter Jacobsen设计与开发
DHIS的全球报告解决方案的介绍奥斯陆大学，2006年
 <http://urn.nb.no/URN:NBN:no-12659>

 <!--DHIS2-SECTION-ID:BraaStandards2007--> Arthur Heywood Woishet Mohammed
VincentShawJørnBraa Ole Hanseth开发健康信息系统
在发展中国家：灵活的标准策略MIS Q 31 1 2007
 <http://heim.ifi.uio.no/~vshaw/Files/Published%20Papers%20included%20in%20Kappa/4_Braa_Flexible%20standards.pdf>

 <!--DHIS2-SECTION-ID:BraaSahayPowerToUsers--> Sundeep SahayJørnBraa
集成的健康信息体系结构-用户权力矩阵
出版社384 2012

 <!--DHIS2-SECTION-ID:Lewis2005--> John Lewis的设计与开发
GIS在基础医疗领域的应用
奥斯陆2005 <http://urn.nb.no/URN:NBN:no-11504>

 <!--DHIS2-SECTION-ID:Mangset2005--> Lars Mangset DHIS-2-全球
分布式开发过程奥斯陆大学2005
 <http://urn.nb.no/URN:NBN:no-10640>

 <!--DHIS2-SECTION-ID:Ngoma2007--> Caroline Ngoma的栽培策略
桑给巴尔健康管理信息系统的实施
奥斯陆大学2007 <http://urn.nb.no/URN:NBN:no-16911>

 <!--DHIS2-SECTION-ID:Nguyen2007--> Thanh Ngoc Nguyen OSS用于医疗保健
发展中国家奥斯陆大学2007
 <http://urn.nb.no/URN:NBN:no-17859>

 <!--DHIS2-SECTION-ID:Saeb2009--> E.K. Golly-Kobrissa R.T.莱特斯塔德·奥·布拉
J.Saeb J. Kossi在塞拉利昂整合卫生信息系统
379-391 2009

 <!--DHIS2-SECTION-ID:ShawComplexityInspried2009--> Vincent Shaw复杂性
启发式方法来共同开发医院管理信息
系统开发2009
 <http://folk.uio.no/vshaw/Files/VShaw%20Kappa%20Final%20Version/2_V_Shaw%20Intro%20Chapter_no%20annex.pdf>

 <!--DHIS2-SECTION-ID:Staring_Titlestad_2008--> Knut Staring O H Titlestad
作为免费软件进行开发：扩展基于Commons的对等生产
致南ICIS 2008会议论文集50 2008
 <http://aisel.aisnet.org/icis2008/50>

>本文探讨了基于公地的同伴生产的概念
>（CBPP）中的公共卫生信息系统
>南。基于对全球全球网络调查结果的分析
>软件开发和实施，这是一种
>本地用户参与分布式开发的重要性是
>呈现。通过实际的例子，我们讨论了
>旨在提高公众水平的软件生产CBPP模型
>南方卫生部门，并提出雪花的概念
>拓扑。

 <!--DHIS2-SECTION-ID:Store2007--> Margrethe商店探索挑战
在开源项目中提供文档奥斯陆大学
2007 <http://urn.nb.no/URN:NBN:no-15782>

 <!--DHIS2-SECTION-ID:Storset2010--> Leif Arne Storset健康集成
管理信息系统奥斯陆大学2010
 <http://urn.nb.no/URN:NBN:no-25666>

 <!--DHIS2-SECTION-ID:ShawScaling2007--> Jorn Braa Vincent Shaw Shegaw Anagaw
尼日利亚和埃塞俄比亚的Mengiste卫生信息系统扩展-
考虑选项2007
 <http://heim.ifi.uio.no/~vshaw/Files/Published%20Papers%20included%20in%20Kappa/6_Shaw_IFP9.4%20Scaling%20of%20HIS_Considering%20the%20Options.pdf>

 <!--DHIS2-SECTION-ID:Vo2009--> Kim Anh ThiVo健康挑战
发展中国家的信息系统计划：成功和
失败奥斯陆大学2009年<http://urn.nb.no/URN:NBN:no-23652>

 <!--DHIS2-SECTION-ID:Overland2010--> JanHenrikØverland开源
改善发展中国家GIS实施的方法
奥斯陆大学2010 <http://urn.nb.no/URN:NBN:no-24751>

 <!--DHIS2-SECTION-ID:Overland2006--> LarsHelgeØverland全球软件
奥斯陆大学发展与地方能力建设2006
 <http://urn.nb.no/URN:NBN:no-13609>
