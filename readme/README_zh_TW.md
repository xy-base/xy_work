<!--
 * @Author: yuyangit yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: yuyangit yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:50:03
 * @FilePath: /xy_work/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_work

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

通用工作模組.

## 程式碼庫

- <a href="https://github.com/xy-base/xy_work.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-base/xy_work.git" target="_blank">Gitee位址</a>

## 安裝

```bash
# bash
pip install xy_work
```

## 使用
```python

```bash
# bash
xy_work -h
# usage: xy_work [-h] [-c [{project,runner}]]
#
# >>>>>>>>>>>> xy_work - v1.0.1 <<<<<<<<<<<<<
#
# options:
#  -h, --help            show this help message and exit
#  -c [{project,runner}], --command [{project,runner}]
#                        命令: -----project => 项目 -----runner => 运行启动器
# 请输入 -c/--command 命令参数

xy_work -n xy_test_work -c project
# 创建项目 [ xy_test_work ] 成功!!!
# 项目路径 ==>>> /mnt/bs-media/Workspace/project/opensource/xy-base/xy_work/test/xy_test_work

cd xy_test_work

xy_work -c runner
# >>>>>>>>>>>> xy_test_work - v0.0.1 <<<<<<<<<<<<<
# Hello World!!!

```

## 許可證
xy_work 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```