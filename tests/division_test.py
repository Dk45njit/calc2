"""Testing Division"""
import pytest
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    numbers = (4, 2)
    division = Division(numbers)
    #Act
    #Assert
    assert division.get_result() == 2

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    numbers = (1.0, 0.0)
    division = Division(numbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        #import pdb;pdb.set_trace()
        result = division.get_result()
        assert result is True
