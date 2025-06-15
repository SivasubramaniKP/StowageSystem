from datetime import date
from typing import List, Union, Optional
from ContainerSpace import ContainerSpace

class Container:
    zone : str
    containerId : str
    width : int
    height : int
    depth : int
    space : ContainerSpace
    def __init__(
        self,
        zone: str,
        containerId: str,
        width: int,
        height: int,
        depth: int
    ):
        self.zone = zone
        self.containerId = containerId
        self.width = width
        self.height = height
        self.depth = depth
        self.space = ContainerSpace()
