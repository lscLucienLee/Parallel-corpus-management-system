# 平行语料管理系统

***

## 1.人员信息

​    项目负责人：
陈怀宇 2801829435@qq.com 

​    成员列表：
​        
1.李思成 lsclucienlee@gmail.com
​        
2.丁隽 1302554864@qq.com
​        
3.严子涵 1115494135@qq.com
​        
4.赵展 1391766596@qq.com

***

## 2.项目介绍

本项目是一个平行语料管理系统，支持机器翻译系统开发人员管理海量平行语料。平行语料是构建机器翻译系统或其他多语言自然处理系统的基础，该系统可以方便地管理语料库，从而提高翻译的质量和效率。

## 功能列表

1. 创建语料库：用户可以通过上传、录入、选择已有语料等方式创建语料库。

2. 更新语料库：支持对平行语料库进行更新，可以通过人工或者机器翻译等途径进行更新。

3. 合并语料库：可以将语料库进行合并，确保合并结果正确。

4. 拆分语料库：支持对数据进行拆分，方便用户只获取部分语料进行处理或者分享语料。

5. 过滤语料库：对语料库中对应不正确、翻译不当的语料进行修改删除，以优化语料库质量。

6. 去重语料库：支持通过算法去重检测来消除重复数据，以优化处理速度。

7. 规范化语料库：支持对数据进行标准化、统一化、一致性处理，以方便多语言处理和语料库管理。

8. 浏览/查询：提供多参数快捷查询和多样化的浏览方式，方便用户查看数据和搜索信息。

9. 分析统计：支持对语料库中不同词句出现的频度数据进行分析和统计，以方便分数据分布等信息。

10. 翻译结果自动评价：通过自动化脚本对翻译结果进行初步判断，并生成评价结果以协助用户校对与修改。

11. 翻译结果人工评价：提供前端人工评价功能，用户可以对机翻结果进行人工评价，最后生成评价结果。

12. 对齐：支持通过数据处理和比较，自动将平行语料库中的相应语段进行词句匹配，或者人工修正，以便于下一步的机器翻译训练等操作。

## 技术栈

本项目采用前后端分离的架构设计，主要技术栈如下：

- Django
- MySQL
- HTML
- CSS
- JS
- Python

## 期望效果

本项目目标是提供一个高效、方便、安全且易用的平行语料管理系统，以帮助开发人员管理和利用海量的平行语料，提高机器翻译的质量和效率。我们希望通过这个项目的开发，为开发者提供一个优质的、易用的解决方案。

***

## 3.项目特性

本项目有以下几个特性：

1. 易用性：本项目采用Django框架，具有良好的用户交互性。后端采用Node.js + Express构建，具有良好的可拓展性和维护性。

2. 高效性：本项目采用了MySQL作为数据库，支持高效的数据访问和多样化的数据处理，也提供了多种查询和统计方式。

3. 灵活性：本项目支持多种文件格式的上传、下载

***

## 4.系统架构

![image](https://github.com/lscLucienLee/Parallel-corpus-management-system/blob/main/%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84.png)
  
（系统架构图）


本项目的系统架构主要分为两大部分，前端交互界面和后端功能实现。


前端：主要是包括
- 界面层：Web端的交互界面的设计，能支持各项功能
- 网络层：和后端的接口交互、信息的收发，以确保用户需求的实现


后端：主要是包括
- 功能层：与前端接进行交互，提供各项用户需求的具体实现和接口，例如创建（在本地创建一个 新的数据库用户，或者语料库，并且返回数据库内容列表等）、分析统计（对用户指定的内容进行分析，并且给前端返回结果，用于展示）
- 数据层：利用MySQL数据库来存储用户信息，和相应的语料库，作为操作和处理的基础
