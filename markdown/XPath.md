# <center>XPath</center>

## 术语

### 节点

- 元素
- 属性
- 文本
- 命名空间
- 处理指令
- 注释
- 文档（根）节点 

### 基本值

基本值无父或无子节点

### 项目

基本值或者节点

### 节点关系

父、子、同胞、先辈、后代

## 选取节点

|表达式|描述|
|-|-|
|nodename|选取此节点的所有子节点|
|/|从根节点选取|
|//|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
|.|选取当前节点|
|..|选取当前节点的父节点|
|@|选取属性|


|路径表达式|结果|
|-|-|
|bookstore|选取 bookstore 元素的所有子节点。|
|/bookstore|选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！|
|bookstore/book|选取属于 bookstore 的子元素的所有 book 元素。|
|//book|选取所有 book 子元素，而不管它们在文档中的位置。|
|bookstore//book|选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。|
|//@lang|选取名为 lang 的所有属性。|

### 谓语

用来查找某个特定的节点或者包含某个指定的节点。
谓语被嵌在方括号中。

|路径表达式|结果|
|-|-|
|/bookstore/book[1]|选取属于bookstore子元素的第一个book元素|
|/bookstore/book[last()]|选取属于bookstore子元素的最后一个book元素|
|/bookstore/book[last()-1]|选取属于bookstore子元素的倒数第二个book元素|
|/bookstore/book[position()<3|选取最前面的两个属于bookstore元素的子元素的book元素|
|//title[@lang]|选取所有拥有名为lang的属性的title元素|
|//title[@lang='eng'|选取所有title元素，且这些元素拥有值为eng的lang属性|
|/bookstore/book[price>35.00]|选取bookstore元素的所有book元素，且其中的price元素的值须大于35.00|
|/bookstore/book[price>35.00]/title|选取bookstore元素中的book元素的所有title元素，且其中的price元素的值须大于35.00

### 选取未知节点

XPath通配符可用来选取未知的xml元素

|通配符|描述|
|-|-|
|*|匹配任何元素节点|
|@*|匹配任何属性节点|
|node()|匹配任何类型的节点|

### 选取若路径

通过在路径表达式中使用“|”运算符，可以选取若干路径。

|路径表达式|结果|
|-|-|
|//book/title丨//book/price|选取book元素的所有title和price元素|
|//title丨//price|选取文档中的所有title和price元素|
|/bookstore/book/title丨//price | 选取属于bookstore元素的book元素的所有title元素，以及文档中所有的price元素|

## XPath Axes(轴)

|轴名称|结果|
|-|-|
|ancestor|选取当前节点的所有先辈（父、祖父等）|
|ancestor-or-self|选取当前节点的所有先辈（父、祖父等）以及当前节点本身|
|attribute|选取当前节点的所有属性|
|child|选取当前节点的所有子元素|
|descendant|选取当前节点的所有后代元素（子、孙等）
|descendant|选取当前节点的所有后代元素（子、孙等）以及当前节点本身|
|following|选取文档中当前节点的结束标签之后的所有节点|
|namespace|选取当前节点的所有命名空间节点|
|parent|选取当前节点的父节点|
|preceding|选取文档中当前节点的开始标签之前的所有节点|
|preceding-sibling|选取当前节点之前的所有同级节点|
|self|选取当前节点|

### 位置路径表达式

 - 绝对位置路径：/step/step/...
 - 相对位置路径：step/step/...

### 步（step）包括

- 轴（axis）
- 节点测试（node-test)
- 零个或者更多谓语（predicate）

#### 步的语法

轴名称::节点测试[谓语]