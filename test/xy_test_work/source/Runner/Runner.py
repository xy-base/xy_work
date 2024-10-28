# -*- coding: utf-8 -*-
__doc__ = "Runner.py"
__version__ = "0.0.1"

from xy_work.Work import Work
from Settings.TestSettings import TestSettings


class Runner(Work):
    settings = TestSettings()

    @property
    def __version__(self) -> str:
        return "0.0.1"

    def get_name(self) -> str:
        return "xy_test_work"

    def __init__(self, *args, **kwargs) -> None:
        self.settings.load(self.settings.default_cfg_relative_path)
        xy_work_argparser_description: str = (
            f""">>>>>>>>>>>> {self.get_name()} - v{self.__version__} <<<<<<<<<<<<<"""
        )
        print(xy_work_argparser_description)
        print()
        print(f"开始备份文件 {type(self.settings.project)}")
