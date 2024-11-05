from hello_cli.model import HelloModel


def test_default_model():
    hello_model = HelloModel()
    assert hello_model.name == "Test me!!"
    assert hello_model.msg == "Hello 'Test me!!'"


def test_with_name_model():
    hello_model = HelloModel.with_name("Saurabh")
    assert hello_model.name == 'Saurabh'
    assert hello_model.msg == "Hello 'Saurabh'"
