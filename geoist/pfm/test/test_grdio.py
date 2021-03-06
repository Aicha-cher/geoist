import numpy.testing as npt

from ... import pfm


def test_spacing():
    "gridder.spacing returns correct values given simple input"
    npt.assert_allclose(pfm.grdio.spacing((0, 10, 0, 20), (11, 11)), [1, 2])
    npt.assert_allclose(pfm.grdio.spacing((0, 10, 0, 20), (11, 21)), [1, 1])
    npt.assert_allclose(pfm.grdio.spacing((0, 10, 0, 20), (5, 21)), [2.5, 1])
    npt.assert_allclose(pfm.grdio.spacing((0, 10, 0, 20), (21, 21)), [0.5, 1])
