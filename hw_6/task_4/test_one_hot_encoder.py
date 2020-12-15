from one_hot_encoder import fit_transform
import pytest


def test_list_input():
    """
    List[str] input test
    """
    assert fit_transform(["Moscow", "New York", "Moscow", "London"]) == [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]


def test_strings_input():
    """
    Strings input test
    """
    assert fit_transform("Moscow", "New York", "Moscow", "London") == [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]


def test_true_case():
    """
    Test for using assertTrue case
    """
    assert (
        all(
            [
                isinstance(item, int)
                for row in fit_transform("Moscow", "New York", "Moscow", "London")
                for item in row[1]
            ]
        )
        == True
    )


def test_empty_input():
    """
    Empty input test
    """
    with pytest.raises(TypeError):
        fit_transform()


def test_not_in_case():
    """
    NoеIn case test
    """
    assert ("Moscow", [1, 1, 1]) not in fit_transform(
        ["Moscow", "New York", "Moscow", "London"]
    )
