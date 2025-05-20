import os
import sys

# Allow import from demo-files directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'demo-files'))

from fcp_tsp import fcp_tsp


def test_fcp_tsp_returns_route():
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    route = fcp_tsp(points)
    assert route
    for p in points:
        assert p in route
