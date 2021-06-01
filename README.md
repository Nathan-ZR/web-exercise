# web前端练习作业

### 一、题目

利用Python+flask框架，实现一个代办事情（需要有：编号，代办事情标题，时间 ，状态等字段）列表web应用；

**技术要点：**

1 界面可以选用前端UI框架；可以采用前后端分离的方式实现，也可以混编方式实现；

2 数据库采用MySQL;采用SQLAchemy框架；

![demo](https://raw.githubusercontent.com/wenzhu123/web-exercise/master/Question/demo.gif)

### 二、虚拟环境

1. 解释器安装部分（略）
2. 终端安装此项目所需要的包 其中的mysqlclient  如果安装不成功，则自己去找对应自己解释器版本的whl文件，安装方法百度走起。我的是是3.9.5的解释器

```python
pip install -r requirements
```

友情链接：
[mysqlclient网站](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient "进去之后可以ctrl + F查询mysqlclient，就可以找到了")

### 三、代码结构及部分注释

```python
.
|-- README.md
|-- UpcomingProject 项目文件夹
|   |-- Model 
|   |   |-- UpComingModel.py  数据库操作 使用了sqlalchemy
|   |   |-- __init__.py
|   |-- __init__.py
|   |-- config
|   |   |-- __init__.py
|   |   |-- sqlConfig.py  数据库配置文件
|   |-- do_upcoming.py  flask框架的应用， 定义了很多数据接口
|   |-- static
|   |   -- JS
|   |       -- logic.js  写逻辑的文件
|   |-- templates
|       |-- base.html  模板文件
|       |-- index.html  首页
|-- __init__.py
|-- start.py  程序主入口
|-- requirements.txt  虚拟环境

```


​					