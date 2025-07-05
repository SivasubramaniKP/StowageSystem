import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model import Cargo
from Model import Container
from Model import ContainerSpace, Cuboid

container = Container("Main", 1, 10,10, 10)
cargo = Cargo(1,"Oxygen Cylinder", 10,100,10, 100, 100, "10.10.2025", 10,"Main", container=container)
space = ContainerSpace(10, 10, 10)
cuboid = Cuboid(0, 0, 0, cargo.height, cargo.depth, cargo.width, None)

import pytest

@pytest.fixture
def sample_data():
    return {
        "cuboid": cuboid
    }
def test_getXSpan(sample_data):
    assert sample_data["cuboid"]._getXSpan() == (0, 10)