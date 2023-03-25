from graniteclient.example import Example


def test_number_property():
    num = 5
    example = Example(num)
    assert example.number == num
