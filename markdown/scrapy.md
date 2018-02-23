# scrapy 入门


## 安装

pip install scrapy

[error:cl.exe](https://stackoverflow.com/questions/43980405/cl-exe-failed-no-such-file-or-directory-when-installing-scrapy)

## scrapy command
Scrapy 1.5.0 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
 - bench：Run quick benchmark test
 - check：Check spider contracts
 - crawl：Run a spider
 - edit：Edit spider
 - fetch：Fetch a URL using the Scrapy downloader
 - genspider：Generate new spider using pre-defined templates
 - fetch：Fetch a URL using the Scrapy downloader
 - list：List available spiders
 - parse：Parse URL (using its spider) and print the results
 - runspider：Run a self-contained spider (without creating a project)
 - settings：Get settings values
 - shell：Interactive scraping console
 - startproject：Create new project
 - version：Print Scrapy version
 - view：Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command

## 流程 

### 创建爬虫工程

```python
scrapy startproject movie
```

### 创建爬虫程序

```python
cd movie
scrapy genspider meiju meiju.com
```

### 文件说明

 - scrapy.cfg 项目的配置信息，主要为scrapy命令行提供一个基础的配置信息
 - items.py 设置数据存储模板，用于结构化数据，类似于Django的model
 - pipelines.py 数据处理行为，接受到爬虫传递过来的数据
 - settings.py 配置文件，如：递归的层数、并发数、延迟下载
 - spiders目录 爬虫目录，如：创建文件，编写爬虫规则，一般创建爬虫文件时，以网站域名命名。

