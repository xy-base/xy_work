<!--
 * @Author: yuyangit yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: yuyangit yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:50:18
 * @FilePath: /xy_work/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_work

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

General working module.

## Source Code Repositories

- <a href="https://github.com/xy-base/xy_work.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-base/xy_work.git" target="_blank">Gitee</a>

## 安装

```bash
# bash
pip install xy_work
```

## How to use

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

## License
xy_work is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```