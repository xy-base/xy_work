<!--
 * @Author: yuyangit yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: yuyangit yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:50:18
 * @FilePath: /xy_work/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_work

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

General working module.

## Source Code Repositories

| [Github](https://github.com/xy-base/xy_work.git)         | [Gitee](https://gitee.com/xy-opensource/xy_work.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_work.git)          |
| ----------- | -------------|---------------------------------------|

## Installation

##### 1.General

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

##### 2.Extension

```python
# main.py

from xy_work.Work import Work

class DemoExtWork(Work):

    def __init__(self):
        self.prog = "xy_work扩展"
        self.description = f""">>>>>>>>>>>> ext_work - v1.0.0 <<<<<<<<<<<<<"""

if __name__ == "__main__":
    work = DemoExtWork()
    work.main()

```

```bash
# bash
python main.py -h
# usage: xy_work扩展 [-h] [-c [COMMAND]] [-n [NAME]]

# >>>>>>>>>>>> ext_work - v1.0.0 <<<<<<<<<<<<<

# options:
#   -h, --help            show this help message and exit
#   -c [COMMAND], --command [COMMAND]
#                         命令: -----project => 项目 -----runner => 运行启动器
#   -n [NAME], --name [NAME]
#                         项目名称 仅支持英文(当[command=project])
```

##### 3.Configuration Customization

> [Sample (xy_test_work)](../samples/xy_test_work/)

## License
xy_work is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  
![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```