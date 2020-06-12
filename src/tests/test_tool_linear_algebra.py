from tools import linear_algebra


class TestLinearAlgebraTools:
    EXPECTED_RESULT_ADD = [5, 7, 9]

    def test_linear_algebra_add(self):
        result = linear_algebra.add(v=[1, 2, 3], w=[4, 5, 6])
        assert result == self.EXPECTED_RESULT_ADD
