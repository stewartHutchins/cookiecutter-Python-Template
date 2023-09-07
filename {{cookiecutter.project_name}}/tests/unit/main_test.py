from pytest import CaptureFixture

from {{cookiecutter.package_name}}.main import main


def test_main(capfd: CaptureFixture[str]) -> None:
    """The program should print "Hello World!"."""
    # act
    main()

    # assert
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
    assert err == ""
