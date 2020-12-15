from morse import decode
import pytest


@pytest.mark.parametrize(
    "input,output",
    [
        ("... --- ...", "SOS"),
        (".--. .- ... .... .-", "PASHA"),
        (
            "... -.. ..-. --. .... .--- -.- .-.. . -.. .-. - -.-- ..- ..",
            "SDFGHJKLEDRTYUI",
        ),
    ],
)
def test_correct_strig_decoding(input, output):
    """
    Strings testing
    """
    assert decode(input) == output


def test_exception():
    """
    Exception testing
    """
    with pytest.raises(KeyError):
        decode("pasha")
