import pytest

from order import calculate_order_total


@pytest.mark.parametrize(
    "subtotal, discount, expected",
    [
        (100, 10, 90.0),
        (250, 20, 200.0),
        (499.99, 15, 424.99),
        (100, 0, 100.0),
    ],
)
def test_normal_inputs(subtotal, discount, expected):
    assert calculate_order_total(subtotal, discount) == expected


@pytest.mark.parametrize(
    "subtotal, discount, expected",
    [
        (0, 0, 0.0),
        (0, 50, 0.0),
        (100, 0, 100.0),
    ],
)
def test_zero_values(subtotal, discount, expected):
    assert calculate_order_total(subtotal, discount) == expected


@pytest.mark.parametrize(
    "subtotal, discount",
    [
        (-1, 10),
        (100, -5),
        (100, 101),
    ],
)
def test_invalid_values_raise_value_error(subtotal, discount):
    with pytest.raises(ValueError):
        calculate_order_total(subtotal, discount)


@pytest.mark.parametrize("subtotal", ["100", None, True])
def test_invalid_type_raises_type_error(subtotal):
    with pytest.raises(TypeError):
        calculate_order_total(subtotal, 10)


@pytest.mark.parametrize(
    "discount, expected",
    [
        (0, 200.0),
        (100, 0.0),
        (0.01, 199.98),
        (99.99, 0.02),
    ],
)
def test_discount_boundaries(discount, expected):
    assert calculate_order_total(200, discount) == expected
