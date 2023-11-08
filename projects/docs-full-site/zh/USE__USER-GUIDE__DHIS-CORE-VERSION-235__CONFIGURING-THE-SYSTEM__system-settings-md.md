---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/commonmark/en/content/user/system-settings.md"
---

# 系统设置

 <!--DHIS2-SECTION-ID:settings-->

## 常规设置

 <!--DHIS2-SECTION-ID:system_general_settings-->

<table>
<caption>General settings</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Setting</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Maximum number of analytics records</strong></p></td>
<td><p>Increase this number to provide more records from the analytics.</p>
<p>The default value is 50,000.</p>
<blockquote>
<p><strong>Warning</strong></p>
<p>Use the setting <strong>Unlimited</strong> carefully, it might result in a very high load on your server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>Maximum number of SQL view records</strong></p></td>
<td><p>Set the maximum number of records in a SQL view.</p>
<p>The default value is Unlimited.</p>
</tr>
<tr class="odd">
<td><p><strong>Cache strategy</strong></p></td>
<td><p>Decides for how long reports analytics responses should be cached.</p>
<p>If you use the scheduled, nightly analytics update, you may want to select <strong>Cache until 6 AM tomorrow</strong>. This is because data in reports change at that time, and you can safely cache data up to the moment when the analytics tables are updated.</p>
<p>If you are loading data continuously into the analytics tables, select <strong>No cache</strong>.</p>
<p>For other cases select the amount of time you want the data to be cached.</p></td>
</tr>
<tr class="even">
<td><p><strong>Infrastructural indicators</strong></p></td>
<td><p>Defines an indicator group where the member indicators should describe data about the organisation units' infrastructure.</p>
<p>You can view the infrastructural data in the <strong>GIS</strong> app: right-click a facility and click <strong>Show information</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Infrastructural data elements</strong></p></td>
<td><p>Defines a data element group where the member data elements should describe data about the organisation units' infrastructure.</p>
<p>Infrastructural data elements can be population, doctors, beds, Internet connectivity and climate.</p>
<p>You can view the infrastructural data in the <strong>GIS</strong> app: right-click a facility and click <strong>Show information</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Infrastructural period type</strong></p></td>
<td><p>Sets the frequency for which the data elements in the infrastructural data elements group are captured.</p>
<p>This will typically be yearly. When viewing the infrastructural data you will be able to select the time period of the data source.</p>
<p>You can view the infrastructural data in the <strong>GIS</strong> app: right-click a facility and click <strong>Show information</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Default relative period for analysis</strong></p></td>
<td><p>Setting this value will determine which relative period is selected as the default in the analytics apps.</p></td>
</tr>
<tr class="even">
<td><p><strong>Feedback recipients</strong></p></td>
<td><p>Defines a user group where the members will receive all messages sent via the feedback function in the <strong>Dashboard</strong> app.</p>
<p>This will typically be members of the super user team who are able to support and answer questions coming from end-users.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Max offline organisation unit levels</strong></p></td>
<td><p>Defines how many levels in the organisation unit hierarchy will be available offline in the organisation unit tree widget.</p>
<p>Under normal circumstances you can leave this on the lowest level, which is default is the default setting.</p>
<p>It can be useful to set it to a higher level to reduce initial load time in cases where you have a large number of organisation units, typically more than 30 000.</p></td>
</tr>
<tr class="even">
<td><p><strong>Data analysis std dev factor</strong></p></td>
<td><p>Sets the number of standard deviations used in the outlier analysis performed on the captured data in the <strong>Data Entry</strong> app.</p>
<p>The default value is 2. A high value will catch less outlier values than a low value.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Phone number area code</strong></p></td>
<td><p>The area code for the area in which your deployment is located.</p>
<p>Used for sending and receiving SMS. Typically, this is a country code.</p>
<p><em>+260</em> (country code for Zambia)</p></td>
</tr>
<tr class="even">
<td><p><strong>Enable multi-organisation unit forms</strong></p></td>
<td><p>Enables support to enter data forms for multiple organisation units at the same time in the <strong>Data Entry</strong> app.</p>
<p>If you've enabled this setting, you can in the <strong>Data Entry</strong> app, click on the parent organisation unit for the children that you want to enter data for, and the data set list will include data sets that are assigned to the children of that parent.</p></td>
</tr>
<tr class="odd">
<td><strong>Acceptance required before approval</strong></td>
<td>When this setting is selected, acceptance of data will be required first before submission to the next approval level is possible.</td>
</tr>
</tbody>
</table>

## 分析设置

 <!--DHIS2-SECTION-ID:system_analytics_settings-->

 <table>
 <caption>分析设置</caption>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>设置</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>分析的默认相对周期</strong> </p> </td>
 <td> <p>定义的相对时间由默认的分析应用程序使用：<strong>数据可视化</strong>，<strong>事件报告</strong>，<strong>事件展台</strong>，<strong> GIS </strong>和<strong>透视表</strong>应用。打开这些应用程序时，将自动选择相对时间段。 </p>
 <p>推荐设置：用户中最常用的相对时间段。 </p> </td>
 </tr>
 <tr class="even">
     <td> <p> <strong>隐藏每日时段</strong> </p> </td>
     <td> <p>在分析工具中隐藏每日时段</p> </td>
 </tr>
 <tr class="odd">
     <td> <p> <strong>隐藏每周时段</strong> </p> </td>
     <td> <p>在分析工具中隐藏每周时段</p> </td>
 </tr>
 <tr class="even">
     <td> <p> <strong>隐藏每月期间</strong> </p> </td>
     <td> <p>在分析工具中隐藏月度</p> </td>
 </tr>
 <tr class="odd">
     <td> <p> <strong>隐藏每两个月的周期</strong> </p> </td>
     <td> <p>在分析工具中隐藏双月周期</p> </td>
 </tr>
 <tr class="even">
 <td> <strong>会计年度相对开始月份</strong> </td>
 <td>定义分析应用程序中相对财务年度应从哪个月（4月，7月或10月）开始。 </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>可缓存性</strong> </p> </td>
 <td> <p>设置是否应为公共或私有可见性提供分析数据响应。 </p>
 <p> <strong>私有</strong>：DHIS2服务器与最终用户之间具有缓存功能的任何节点或服务器都无法缓存网页。如果所提供的页面可以包含或确实包含敏感信息，这将很有用。这意味着，每次需要网页时，要么从DHIS2服务器获取一个新页面，要么DHIS2服务器缓存该页面。除DHIS2服务器外，没有其他服务器可以缓存页面。 </p>
 <p> <strong>公共</strong>：DHIS2服务器与最终用户之间具有缓存能力的任何节点或服务器都可以缓存网页。这样可以重新传输到DHIS2服务器的流量，并有可能加快后续页面的加载速度。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong> Analytics缓存模式</strong> </p> </td>
 <td> <p>支持两种不同的模式：</p>
 <p> <strong>渐进式</strong>：这与用于分析的新渐进式缓存功能有关。启用后，它将覆盖分析请求的全局缓存策略。此模式将触发所有分析请求的HTTP和数据层缓存。启用此模式时，<em>缓存因子</em>是强制性的。 </p>
 <p> <strong>固定</strong>：将根据<em>缓存策略中定义的时间段缓存请求。 </em> </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>缓存因子</strong> </p> </td>
 <td> <p>选择一个缓存因子值。仅当分析缓存模式已设置为<em>渐进式</em>时，此字段才可用。 </p>
 <p>它显示一个整数列表，其中每个整数代表一个绝对缓存因子。该整数将在内部用于计算每个分析请求的最终到期时间。缓存因子越高，请求将被缓存的时间越长。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>在分析中隐藏未批准数据的最大年限</strong> </p> </td>
 <td> <p>设置时间分析是否应遵守数据的批准级别以及在多长时间内应遵守数据的批准级别。通常，默认情况下会认为已有数年历史的数据已被批准。为了加快分析请求的速度，您可以选择忽略历史数据的实际批准级别。 </p>
 <p> <strong>永远不要检查批准</strong>：不会隐藏任何数据，无论其数据批准状态如何。 </p>
 <p> <strong>检查所有数据的批准</strong>：将始终检查批准状态。 </p>
 <p>其他选项，例如<strong>最近3年</strong>：将检查批准状态中是否存在3年以下的数据；较旧的数据将不会被检查。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>分析数据缓存的阈值</strong> </p> </td>
 <td> <p>设置是否仅启用早于指定年限的缓存数据。 </p>
 <p>这允许在不缓存的情况下直接返回最新数据，同时出于性能方面的考虑，为较早的数据提供缓存版本。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>分析表导出中的尊重类别选项开始和结束日期</strong> </p> </td>
 <td> <p>此设置控制分析是否应过滤与具有开始和结束日期的类别选项相关联但与在类别选项有效期内的时间段无关的数据。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>将分析置于维护模式</strong> </p> </td>
 <td>将DHIS2的分析和Web API置于维护模式。这意味着将为所有请求返回&quot;503服务不可用&quot;。
 <p>当您需要在服务器上执行维护（例如在服务器在生产环境中运行时重建索引）以减少负载并更有效地执行维护时，此功能很有用。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>跳过分析表中的零数据值</strong> </p> </td>
 <td> <p>在分析表中不包含任何为零的聚合数据值。如果汇总数据值为零并已存储（数据元素配置为存储零值），则这可以减小分析表的大小，并加快分析表的构建和访问。 </p> </td>
 </tr>
 </tbody>
 </table>

## 服务器设定

 <!--DHIS2-SECTION-ID:system_server_settings-->

 <table>
 <caption>服务器设置</caption>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>设置</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>数据库服务器CPU的数量</strong> </p> </td>
 <td> <p>设置数据库服务器的CPU核心数。 </p>
 <p>当数据库托管在与应用程序服务器不同的服务器上时，这使系统能够以最佳性能运行，因为DHIS2中的分析与可用核心数成线性比例。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>系统通知电子邮件地址</strong> </p> </td>
 <td> <p>定义将接收系统通知的电子邮件地址。 </p>
 <p>有关分析表生成等流程失败的通知将在此处发送。这对于应用程序监视很有用。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong> Google Analytics（通用分析）密钥</strong> </p> </td>
 <td> <p>设置Google UA密钥，以通过Google Analytics（分析）平台为您的DHIS2实例提供使用情况分析。应该注意的是，当前，DHIS2中并非所有应用程序都支持Google Analytics（分析），因此您的用户的某些活动可能不会出现在此平台中。 </p>
 <p>您可以通过<a href="http://google.com/analytics" class="uri"> http://google.com/analytics </a>了解更多有关Google Analytics（分析）的信息。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong> Google Maps API密钥</strong> </p> </td>
 <td> <p>定义Google Maps API的API密钥。这用于显示DHIS2中的地图。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong> Bing Maps API密钥</strong> </p> </td>
 <td> <p>定义Bing Maps API的API密钥。这用于显示DHIS2中的地图。 </p> </td>
 </tr>
 </tbody>
 </table>

## 外观设置

 <!--DHIS2-SECTION-ID:system_appearance_settings-->

<table>
<caption>Appearance settings</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Setting</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Select language</strong></p></td>
<td>
    <p>Sets the language for which you can then enter translations of the following settings:</p>
    <ul>
        <li><p><strong>Application introduction</strong></p></li>
        <li><p><strong>Application title</strong></p></li>
        <li><p><strong>Application notification</strong></p></li>
        <li><p><strong>Application left-side footer</strong></p></li>
        <li><p><strong>Application right-side footer</strong></p></li>
    </ul>
    <blockquote>
        <p><strong>Note</strong></p>
        <p>Before each of these settings can accept a translated value, they first need to have a default/fallback value. This value can be set by selecting <em>System default (fallback)</em> in this dropdown.</p>
    </blockquote>
</td>
</tr>
<tr class="even">
<td><p><strong>Application title</strong></p></td>
<td><p>Sets the application title on the top menu.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Application introduction</strong></p></td>
<td><p>Sets an introduction of the system which will be visible on the top-left part of the login page.</p></td>
</tr>
<tr class="even">
<td><p><strong>Application notification</strong></p></td>
<td><p>Sets a notification which will be visible on the front page under the login area.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Application left-side footer</strong></p></td>
<td><p>Sets a text in the left-side footer area of the login page.</p></td>
</tr>
<tr class="even">
<td><p><strong>Application right-side footer</strong></p></td>
<td><p>Sets a text in the right-side footer area of the login page.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Style</strong></p></td>
<td><p>Sets the style (look-and-feel) of the system.</p>
<p>The user can override this setting in the <strong>Settings</strong> app: <strong>User settings</strong> &gt; <strong>Style</strong>.</p>
<blockquote>
<p><strong>Note</strong></p>
<p>Due to technical reasons, it's not possible to change the color of the newest version of the header bar. The apps with the newest header bar will retain the blue header bar.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>Start page</strong></p></td>
<td><p>Sets the page or app which the user will be redirected to after log in.</p>
<p>Recommended setting: the <strong>Dashboard</strong> app.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Help page link</strong></p></td>
<td><p>Defines the URL which users will see when they click <strong>Profile</strong> &gt;<strong>Help</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Flag</strong></p></td>
<td><p>Sets the flag which is displayed in the left menu of the <strong>Dashboard</strong> app.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Interface language</strong></p></td>
<td><p>Sets the language used in the user interface.</p>
<p>The user can override this setting in the <strong>Settings</strong> app: <strong>User settings</strong> &gt; <strong>Interface language</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Database language</strong></p></td>
<td><p>Sets the language used in the database.</p>
<p>The user can override this setting in the <strong>Settings</strong> app: <strong>User settings</strong> &gt; <strong>Database language</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Property to display in analysis modules</strong></p></td>
<td><p>Sets whether you want to display the metadata objects' names or short names in the analytics apps: <strong>Data Visualizer</strong>, <strong>Event Reports</strong>, <strong>Event Visualizer</strong>, <strong>GIS</strong> and <strong>Pivot Table</strong> apps.</p>
<p>The user can override this setting in the <strong>Settings</strong> app: <strong>User settings</strong> &gt; <strong>Property to display in analysis modules</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Default digit group separator to display in analysis modules</strong></p></td>
<td><p>Sets the default digit group separator in the analytics apps: <strong>Data Visualizer</strong>, <strong>Event Reports</strong>, <strong>Event Visualizer</strong>, <strong>GIS</strong> and <strong>Pivot Table</strong> apps.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Require authority to add to view object lists</strong></p></td>
<td><p>If you select this option, you'll hide menu and index page items and links to lists of objects if the current user doesn't have the authority to create the type of objects (privately or publicly).</p></td>
</tr>
<tr class="even">
<td><p><strong>Custom login page logo</strong></p></td>
<td><p>Select this option and upload an image to add your logo to the login page.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Custom top menu logo</strong></p></td>
<td><p>Select this option and upload an image to add your logo to the left in the top menu.</p></td>
</tr>
</tbody>
</table>

## 电子邮件设定

 <!--DHIS2-SECTION-ID:system_email_settings-->

<table>
<caption>Email settings</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Setting</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Host name</strong></p></td>
<td><p>Sets the host name of the SMTP server.</p>
<p>When you use Google SMTP services, the host name should be <em>smtp.gmail.com</em>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Port</strong></p></td>
<td><p>Sets the port to connect to the SMTP server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>User name</strong></p></td>
<td><p>The user name of the user account with the SMTP server.</p>
<p>mail@dhis2.org</p></td>
</tr>
<tr class="even">
<td><p><strong>Password</strong></p></td>
<td><p>The password of the user account with the SMTP server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>TLS</strong></p></td>
<td><p>Select this option if the SMPT server requires TLS for connections.</p></td>
</tr>
<tr class="even">
<td><p><strong>Email sender</strong></p></td>
<td><p>The email address to use as sender when sending out emails.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Send me a test email</strong></p></td>
<td><p>Sends a test email to the current user logged into DHIS2.</p></td>
</tr>
</tbody>
</table>

## 访问设置

 <!--DHIS2-SECTION-ID:system_access_settings-->

 <table>
 <caption>访问设置</caption>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>设置</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>自我注册帐户用户角色</strong> </p> </td>
 <td> <p>定义应该为自注册用户帐户赋予哪个用户角色。 </p>
 <p>要启用用户自注册：从列表中选择任何用户角色。自我注册表格的链接将显示在登录页面上。 </p>
 <blockquote>
 注意</strong> </p> <p> <strong>
 <p>要启用自我注册，还必须选择<strong>自我注册帐户组织单位</strong>。 </p>
 </blockquote>
 <p>要禁用用户的自注册：选择<strong>禁用自注册</strong>。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>自助注册帐户组织单位</strong> </p> </td>
 <td> <p>定义哪个组织单位应与自注册用户相关联。 </p>
 <blockquote>
 注意</strong> </p> <p> <strong>
 <p>要启用自我注册，还必须选择<strong>自我注册帐户用户角色</strong>。 </p>
 </blockquote> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>不需要reCAPTCHA进行自注册</strong> </p> </td>
 <td> <p>定义是否要使用reCAPTCHA进行用户自注册。默认情况下启用。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>启用用户帐户恢复</strong> </p> </td>
 <td> <p>定义用户是否可以恢复自己的密码。 </p>
 <p>启用此设置后，将在首页上显示帐户恢复表单的链接。 </p>
 <blockquote>
 注意</strong> </p> <p> <strong>
 <p>用户帐户恢复要求您已经配置了电子邮件设置（SMTP）。 </p>
 </blockquote> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>多次尝试登录失败后临时锁定用户帐户</strong> </p> </td>
 <td> <p>定义在15分钟的时间内连续五次失败的登录尝试后，系统是否应锁定用户帐户。 </p>
 <p>帐户将被锁定15分钟，然后用户可以尝试再次登录。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>允许用户授予自己的用户角色</strong> </p> </td>
 <td> <p>定义用户在创建新用户时是否可以将自己拥有的用户角色授予其他用户。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>允许在添加或更新期间将对象分配给相关对象</strong> </p> </td>
 <td> <p>定义在创建或编辑元数据对象时是否应允许用户将对象分配给相关对象。 </p>
 <p>您可以允许用户在创建或编辑组织单位时将组织单位分配给数据集和组织单位组集。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>要求更改用户帐户密码</strong> </p> </td>
 <td> <p>定义是否应每3、6或12个月强制用户更改一次密码。 </p>
 <p>如果不想强制用户更改密码，请选择<strong>从不</strong>。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <strong>启用密码过期警报</strong> </td>
 <td>设置后，用户密码即将到期时，将收到通知。 </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>密码中的最小字符</strong> </p> </td>
 <td> <p>定义用户密码中必须包含的最少字符数。 </p>
 <p>您可以选择8（默认），10、12或14。</p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong> CORS白名单</strong> </p> </td>
 <td> <p>将一组URL列入白名单，这些URL可以从另一个域访问DHIS2 API。每个网址应在单独的行中输入。跨域资源共享（CORS）是一种机制，它允许从提供第一资源的域之外的另一个域请求网页上的受限资源（例如javascript文件）。 </p> </td>
 </tr>
 </tbody>
 </table>

## 日历设定

 <!--DHIS2-SECTION-ID:system_calendar_settings-->

 <table>
 <caption>日历设置</caption>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>设置</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>日历</strong> </p> </td>
 <td> <p>定义系统将使用的日历。 </p>
 <p>系统支持以下日历：科普特，埃塞俄比亚，格里高利，伊斯兰（Lunar Hijri），ISO 8601，朱利安语，尼泊尔语，波斯语（Solar Hijri）和泰语。 </p>
 <blockquote>
 注意</strong> </p> <p> <strong>
 <p>这是系统范围的设置。单个DHIS2实例中不能有多个日历。 </p>
 </blockquote> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>日期格式</strong> </p> </td>
 <td> <p>定义系统将使用的日期格式。 </p> </td>
 </tr>
 </tbody>
 </table>

## 资料汇入设定

 <!--DHIS2-SECTION-ID:system_data_import_settings-->

数据导入设置适用于可以启用的其他控件
验证通过Web API导入的汇总数据。他们
对应视为冲突的事项提供可选约束
在导入期间。将约束应用于每个单独的数据值
在导入中。

 <table>
 <caption>数据导入设置</caption>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>设置</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>需要期间以匹配数据集的期间类型</strong> </p> </td>
 <td> <p>要求数据值的周期与分配了数据值的数据元素的数据集具有相同的周期类型。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>需要类别选项组合以匹配数据元素的类别组合</strong> </p> </td>
 <td> <p>要求数据值的类别选项组合成为数据值的数据元素的类别组合的一部分。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>要求组织单位匹配数据集的分配</strong> </p> </td>
 <td> <p>要求将数据值的组织单位分配给数据值的数据元素所分配到的一个或多个数据集。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>要求属性选项组合以匹配数据集的类别组合</strong> </p> </td>
 <td> <p>要求数据值的属性选项组合是数据值的数据元素所分配到的数据集的类别组合的一部分。 </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> <strong>要求指定类别选项组合</strong> </p> </td>
 <td> <p>要求指定数据值的类别选项组合。 </p>
 <p>默认情况下，如果未指定，它将退回到默认类别选项组合。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>需要指定属性选项组合</strong> </p> </td>
 <td> <p>需要指定数据值的属性选项组合。 </p>
 <p>默认情况下，如果未指定，它将回退到默认属性选项组合。 </p> </td>
 </tr>
 </tbody>
 </table>

## 同步设定

以下设置用于数据和元数据
同步。

> **注意**
>
>有关如何配置元数据同步的更多信息，
>请参阅[配置元数据
>同步]（https://docs.dhis2.org/master/zh/user/html/metadata_sync.html）

<table>
<caption>Synchronization settings</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Setting</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Remote server URL</strong></p></td>
<td><p>Defines the URL of the remote server running DHIS2 to upload data values to.</p>
<p>It is recommended to use of SSL/HTTPS since user name and password are sent with the request (using basic authentication).</p>
<p>The system will attempt to synchronize data once every minute.</p>
<p>The system will use this setting for metadata synchronization too.</p>
<blockquote>
<p><strong>Note</strong></p>
<p>To enable data and metadata synchronization, you must also enable jobs for <strong>Data synchronization</strong> and <strong>Metadata synchronization</strong> in the <strong>Scheduler</strong> app.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>Remote server user name</strong></p></td>
<td><p>The user name of the DHIS2 user account on the remote server to use for data synchronization.</p>
<blockquote>
<p><strong>Note</strong></p>
<p>If you've enabled metadata versioning, you must make sure that the configured user has the authority &quot;F_METADATA_MANAGE&quot;.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>Remote server password</strong></p></td>
<td><p>The password of the DHIS2 user account on the remote server. The password will be stored encrypted.</p></td>
</tr>
<tr class="even">
<td><p><strong>Enable versioning for metadata sync</strong></p></td>
<td><p>Defines whether to create versions of metadata when you synchronize metadata between central and local instances.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Don't sync metadata if DHIS versions differ</strong></p></td>
<td><p>The metadata schema changes between versions of DHIS2 which could make different metadata versions incompatible.</p>
<p>When enabled, this option will not allow metadata synchronization to occur if the central and local instance(s) have different DHIS2 versions. This apply to metadata synchronization done both via the user interface and the API.</p>
<p>The only time it might be valuable to disable this option is when synchronizing basic entities, for example data elements, that have not changed across DHIS2 versions.</p></td>
</tr>
<tr class="even">
<td><p><strong>Best effort</strong></p></td>
<td><p>A type of metadata version which decides how the importer on local instance(s) will handle the metadata version.</p>
<p><em>Best effort</em> means that if the metadata import encounters missing references (for example missing data elements on a data element group import) it ignores the errors and continues the import.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Atomic</strong></p></td>
<td><p>A type of metadata version which decides how the importer on local instance(s) will handle the metadata version.</p>
<p><em>Atomic</em> means all or nothing - the metadata import will fail if any of the references do not exist.</p></td>
</tr>
</tbody>
</table>

## OAuth2客户端

 <!--DHIS2-SECTION-ID:system_oauth2_settings-->

您可以在 **系统设置 **中创建，编辑和删除OAuth2客户端
应用程序。

1.  打开 **系统设置 **应用，然后单击 **OAuth2客户端 **。

2.  点击添加按钮。

3.  输入 **名称 **， **客户ID **和 **客户密码 **。

4.  选择 **授权类型 **。

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Grant type</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Password</strong></p></td>
    <td><p>TBA</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Refresh token</strong></p></td>
    <td><p>TBA</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Authorization code</strong></p></td>
    <td><p>TBA</p></td>
    </tr>
    </tbody>
    </table>

5.  输入**重定向URI **。如果您有多个URI，请使用
    一条线。
