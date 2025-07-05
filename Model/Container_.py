from datetime import date
from typing import List, Union, Optional

class Container:
    zone : str
    containerId : str
    width : int
    height : int
    depth : int
    space : "ContainerSpace"
    def __init__(
        self,
        zone: str,
        containerId: str,
        width: int,
        height: int,
        depth: int
    ):

        from .ContainerSpace_ import ContainerSpace
        self.zone = zone
        self.containerId = containerId
        self.width = width
        self.height = height
        self.depth = depth
        self.space = ContainerSpace(
            height=self.height,
            width=self.width,
            depth=self.depth
        )
