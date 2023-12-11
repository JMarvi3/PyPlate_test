import pytest
import numpy as np
from pyplate.slicer import Slicer


@pytest.fixture
def array():
    return np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


def test_resolve_labels_zero():
    # Index must be in range 1..n
    with pytest.raises(ValueError):
        Slicer.resolve_labels(0, [])


def test_resolve_labels_high():
    # Index must be in range 1..n
    with pytest.raises(ValueError):
        Slicer.resolve_labels(100, ['1'])


def test_resolve_labels_high_slices():
    # Slice indexes must be in range 1..n
    with pytest.raises(ValueError):
        Slicer.resolve_labels(slice(100, None, None), ['1'])
    with pytest.raises(ValueError):
        Slicer.resolve_labels(slice(None, 100, None), ['1'])


def test_resolve_labels_not_in_labels():
    # Label must in list of labels
    with pytest.raises(ValueError):
        Slicer.resolve_labels('label', [])


def test_resolve_labels_invalid_step():
    # step must be None or int
    with pytest.raises(TypeError):
        Slicer.resolve_labels(slice(None, None, 'label'), [])


def test_resolve_labels_typerror():
    # item must be an int, str, or slice
    with pytest.raises(TypeError):
        Slicer.resolve_labels(1.0, [])


def test_Slicer_arraytype():
    # array_obj must be a numpy.ndarray
    with pytest.raises(TypeError, match="must be a numpy.ndarray"):
        Slicer(None, None, None, None)


def test_Slicer_row_labels(array):
    # row_labels must be a list or tuple
    with pytest.raises(TypeError, match="row_labels"):
        Slicer(array, None, None, None)
    # row_labels must not be empty
    with pytest.raises(TypeError, match="row_labels"):
        Slicer(array, (), None, None)


def test_Slicer_col_labels(array):
    # col_labels must be a list or tuple
    with pytest.raises(TypeError, match="col_labels"):
        Slicer(array, [], None, None)
    # col_labels must not be empty
    with pytest.raises(TypeError, match="col_labels"):
        Slicer(array, ['1'], (), None)
