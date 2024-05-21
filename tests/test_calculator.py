from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.add(a, b)

        # Assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.subtract(a, b)

        # Assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # Arrange
        a = 123
        b = 456
        cal = Calculator()

        # Act
        result = cal.multiply(a, b)

        # Assert
        expected = 56088
        assert result == expected

    def test_divide(self):
        # Arrange
        a = 100
        b = 10
        cal = Calculator()

        # Act
        result = cal.divide(a, b)

        # Assert
        expected = 10
        assert result == expected
