from src.algorithmia import algorithmia_demo


def test_algorithmia_demo():
    assert algorithmia_demo.apply("Jane") == "hello Jane"
