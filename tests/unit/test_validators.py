"""
Tests the validator functions in utils dir
"""

# Command line: python -m pytest tests/test_validators.py

import pytest

from app.utils.validators import validate_integer

class TestIntegerValidator:
    def test_valid(self):
        validate_integer('arg', 10, 0, 20, 'custom min msg', 'custom max msg')

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer('arg', 1.5)

    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 100)
        assert 'arg' in str(ex.value)
        assert '100' in str(ex.value)

    def test_min_custom_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 100, custom_min_message='custom')
        assert str(ex.value) == 'custom'

    def test_max_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 1, 5)
        assert 'arg' in str(ex.value)
        assert '5' in str(ex.value)

    def test_max_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 1, 5, custom_max_message='custom')
        assert str(ex.value) == 'custom'

# You want your coverage to be as high as possible.
# 100% coverage does not mean you have tested everything, it just means that you have tested
# all the possible branches in your code. That does not mean you have actually done all the testing
# that you should have been testing. But a high percentage usually is a good sign that you have
# tested many things. Try to aim for a high %.