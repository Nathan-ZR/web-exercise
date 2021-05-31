# web前端练习作业

### 一、题目

[题目链接](http://note.youdao.com/noteshare?id=cf98c1239d6cf56936c11583f95d23c9&amp;sub=7FCC6795E228458E88CE7A034B481610)

[![2mMNQg.png](https://z3.ax1x.com/2021/05/31/2mMNQg.png)](https://imgtu.com/i/2mMNQg)

### 二、虚拟环境

1. 解释器安装部分（略）
2. 终端安装此项目所需要的包 其中的mysqlclient  如果安装不成功，则自己去找对应自己解释器版本的whl文件，安装方法百度走起。我的是是3.9.5的解释器

```python
pip install -r requirements
```

友情链接：
[mysqlclient网站](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient "进去之后可以ctrl + F查询mysqlclient，就可以找到了")

### 三、代码结构

1. start.py

   程序的总入口

2. UpComingProject/
&emsp;&emsp;&emsp;config/&nbsp;
&emsp;&emsp;&emsp;&emsp;sqlConfig.py   **数据库的配置文件**&nbsp;
&emsp;&emsp;&emsp;Model/&nbsp;
&emsp;&emsp;&emsp;&emsp;_ _ init _ _.py  **初始化了session**&nbsp;
&emsp;&emsp;&emsp;&emsp;UpComingModel.py **数据库操作 使用sqlalchemy**&nbsp;
&emsp;&emsp;&emsp;static/&nbsp;
&emsp;&emsp;&emsp;&emsp;JS/&nbsp;
&emsp;&emsp;&emsp;&emsp;&emsp;logic.js  **写逻辑的js文件**&nbsp;
&emsp;&emsp;&emsp;templates/&nbsp;
&emsp;&emsp;&emsp;&emsp;base.html&nbsp;
&emsp;&emsp;&emsp;&emsp;index.html&nbsp;
&emsp;&emsp;&emsp;do_upcoming.py  **flask框架的应用， 定义了很多数据接口**&nbsp;
					