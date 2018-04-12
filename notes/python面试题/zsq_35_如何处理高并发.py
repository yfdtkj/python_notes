#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_35_如何处理高并发
# @time: 2018/4/12 5:11
"""
1、什么是高并发？
    高并发是指通过设计保证系统能够同时并行处理很多请求
2、解决高并发的的几个重要环节：使用高性能的服务器、
高性能的数据库、高效率的编程语言、还有高性能的Web容器。
3、高并发相关的4个指标：响应时间、吞吐量、每秒响应请求数、并发用户数
4、提高系统并发能力的两种方式：垂直扩展和水平扩展
垂直扩展：
    1、提升单机硬件性能（cpu、内存、固态硬盘、网卡）
    2、提升单机架构性能（缓存--减少IO，异步--增加吞吐量）
水平扩展：增加服务器数量，线性扩充系统性能。但是水平扩展对服务器的架构设计是有
要求的
5、常见的互联网分布式系统架构的6层：
    1、客户端层
    2、反向代理层
    3、站点应用层
    4、服务层
    5、数据-缓存层
    6、数据-数据库层"""























