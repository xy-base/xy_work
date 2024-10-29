# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Project"
"""
  * @File    :   Project.py
  * @Time    :   2024/10/28 10:20:55
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from pathlib import Path
from xy_work.Settings.Section.Project import Project as xyProject


class Project(xyProject):
    backup_path: Path | None = None
    data_path: Path | None = None

    def _load(self):
        super()._load()
        ##################### fetch_path ###############
        self.backup_path = self._fetch_path("backup_path", Path("../workspace/backup"))
        self.data_path = self._fetch_path("data_path", Path("../data/data.txt"))
