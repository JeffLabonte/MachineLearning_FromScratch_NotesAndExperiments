from tools import linear_algebra

import pytest


class TestLinearAlgebraTools:
    EXPECTED_RESULT_ADD = [5, 7, 9]

    def test_linear_algebra_add_same_length_vector(self):
        result = linear_algebra.add(v=[1, 2, 3], w=[4, 5, 6])
        assert result == self.EXPECTED_RESULT_ADD

    def test_linear_algebra_add_not_same_length(self):
        with pytest.raises(RuntimeError):
        	linear_algebra.add(v=[1, 2], w=[4, 5, 6])