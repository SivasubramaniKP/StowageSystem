
from datetime import date
from typing import List, Union, Optional

class Cargo:
    _id : int
    name : str
    width : int
    height : int
    depth : int 
    mass : float
    priority : int
    expiryDate : date
    usageLimit : int
    preferredZone : str 
    container : Union["Container", None] 

    def __init__(
        self,
        _id: int,
        name: str,
        width: int,
        height: int,
        depth: int,
        mass: float,
        priority: int,
        expiryDate: date,
        usageLimit: int,
        preferredZone: str,
        container: Optional["Container"] = None
    ):
        
        from .Container_ import Container
        self._id = _id
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.mass = mass
        self.priority = priority
        self.expiryDate = expiryDate
        self.usageLimit = usageLimit
        self.preferredZone = preferredZone
        self.container = container

    def place_item(
            self,
            container : "Container",
    ):
        pass
