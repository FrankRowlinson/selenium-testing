# task from 3_lesson5_step7 to implement strict xfail.

import pytest


# this will fail because xfail is strict
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


# this will xfail because it supposed to fail
@pytest.mark.xfail
def test_not_succeed():
    assert False


# this test will be skipped
@pytest.mark.skip
def test_skipped():
    assert False