# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Settings"
"""
  * @File    :   Settings.py
  * @Time    :   2024/10/28 09:09:51
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from pathlib import Path
from xy_work.Settings.Settings import Settings as xy_s
from xy_work.Settings.Section.Runner import Runner

from .Section.Backup import Backup
from .Section.Project import Project


class TestSettings(xy_s):
    backup: Backup | None = None
    project: Project | None = None

    GLOBAL_CFG_SETTINGS_PATH_KEY = "__xy_backup_work_cfg_path_key"
    default_cfg_relative_path: Path = Path("config/xy_backup_work.toml")

    def reload(self, settings_cfg_path: Path):
        print("TestSettings reload")
        self.project = self.make_section(Project)
        self.backup = self.make_section(Backup)
        self.runner = self.make_section(Runner)
