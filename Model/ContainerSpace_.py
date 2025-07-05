from datetime import date
from typing import List, Union, Optional

class Cuboid:
    """
        Let Cuboid represent the basic unit of Space in a Container
        A cuboid contains only one Cargo

        
        ( x y z ) : is the coordinate of bottom left vertex
    """
    x : int
    y : int
    z : int
    width : int
    height : int
    depth : int
    volume : int
    cargo : Union["Cargo",None] 

    def __init__(
            self, 
            x : int,
            y : int,
            z : int,
            height : int,
            depth : int,
            widht : int,
            cargo: "Cargo"
    ):

        from .Cargo_ import Cargo
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.depth = depth
        self.width = widht
        self.volume = self.height * self.width * self.depth
        self.cargo = cargo

    def _getXSpan(self):
        return ( self.x, self.x + self.width )

    def _getYSpan(self):
        return ( self.y, self.y + self.height )

    def _getZSpan(self):
        return ( self.z, self.z + self.depth )

    def _collision_detection(
        self, box : "Cuboid" 
    ) -> bool:
        """
            Detect if given box collides with the Cuboid
            My Naaive Principle:
                if SpanX SpanY and SpanZ of both box interesects
                then there is a collision
        """

class ContainerSpace:
    # SpaceMatrix: List[List[List["Cargo" | None]]]
    itemsIncluded : List["Cargo"]
    width : int
    height : int
    depth : int
    spaceAvailable : int
    contiguousSpace : List[int]
    largestCuboidAvailabe : List[Cuboid]
    placedCuboids : List[Cuboid]

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.itemsIncluded = []
        self.spaceAvailable = self.height * self.width * self.depth
        self.contiguousSpace = self.spaceAvailable
        self.largestCuboidsAvailabe = tuple()
        self.placedCuboids = []
        # self.SpaceMatrix = [ [ [ None for x in range(self.depth) ] for y in range(self.height) ] for z in range(self.width) ] 

    """
        What are the things Container Space needs to satisfy??
            -> Needs to place the item
            -> Check if there is a free space
            -> If it is in sight or not?
            -> Is there a cuboid below?
    """
