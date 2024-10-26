# -*- coding: utf-8 -*-
__doc__ = "Runner.py"
__version__ = "0.0.1"

from xy_work.Work import Work


class Runner(Work):
    @property
    def __version__(self) -> str:
        return "0.0.1"

    def get_name(self) -> str:
        return "xy_test_work"

    def __init__(self, *args, **kwargs) -> None:
        xy_work_argparser_description: str = f""">>>>>>>>>>>> {self.get_name()} - v{self.__version__} <<<<<<<<<<<<<"""
        print(xy_work_argparser_description)
        print()
        print("Hello World!!!")
