# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "main"
"""
  * @File    :   main.py
  * @Time    :   2024/10/27 18:14:12
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from xy_work.Work import Work


class DemoExtWork(Work):

    def __init__(self):
        self.prog = "xy_work扩展"
        self.description = """>>>>>>>>>>>> ext_work - v1.0.0 <<<<<<<<<<<<<"""


if __name__ == "__main__":
    work = DemoExtWork()
    work.main()
