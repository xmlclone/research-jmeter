- [基础概念](#基础概念)
  - [多request相互之间的影响](#多request相互之间的影响)
- [插件](#插件)

# 基础概念

## 多request相互之间的影响

1. 先看单个request的情形(demo1/demo1.jmx)

![](imgs/m1.png)

> 10s总共完成了6782个请求，tps大致为6782/10，和图上基本一致。

2. 另外一个单个requst(demo1/demo2.jmx)

![](imgs/m2.png)

3. 合并后(demo1/demo3.jmx)

![](imgs/m3.png)

> 10s每个接口分别完成了95次请求，那么每个接口的tps大致为95/10，和图上基本一致，此时f2影响到了f1本身的性能表现(仅针对于tps受到了影响，rt响应时间并没有受到影响)


# 插件

https://jmeter-plugins.org/install/Install/