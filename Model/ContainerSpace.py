from Cargo import Cargo
from datetime import date
from typing import List, Union, Optional

class Cuboid:
    x : int
    y : int
    z : int
    widht : int
    height : int
    depth : int
    volume : int

    def __init__(
            self, 
            x : int,
            y : int,
            z : int,
            height : int,
            depth : int,
            widht : int
    ):
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.depth = depth
        self.widht = widht
        self.volume = self.height * self.widht * self.depth

class UnitVolume:
    """
        Unit Volume represents the basic unit of Space in the container
        Following the cartesian place, the units are unit cube with volume of 1 cm^3

        For a container with dimensions [ width, height, depth ] => There are (width * height * depth) number of UnitVolume

        Each volume can be occupied by exactly one cargo

        #     ^
        #     |
        #     |
        #     |
        #     |
        #     |
        #     |
        #     |___ ___ ___ ___ ___
        #     | 1 | 2 | 3 | 4 | 5 | 
        #     --------------------------
        #     (0, 0)
    """
    cargo : Cargo



class ContainerSpace:
    SpaceMatrix: List[List[List["Cargo" | None]]]
    itemsIncluded : List["Cargo"]
    width : int
    height : int
    depth : int
    spaceAvailable : int
    contiguousSpace : List[int]
    largestCuboidsAvailabe : List[Cuboid]

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.itemsIncluded = []
        self.spaceAvailable = self.height * self.width * self.depth
        self.contiguousSpace = self.spaceAvailable
        self.largestCuboidsAvailabe = tuple(Cuboid(
            x = 0,
            y = 0,
            z = 0,
            height = height,
            depth = depth,
            widht= width
        ))
        self.SpaceMatrix = [ [ [ None for x in range(self.depth) ] for y in range(self.height) ] for z in range(self.width) ] 

    def isSpaceFree(
            self, 
            cargo : Cargo,
    ):
        pass
