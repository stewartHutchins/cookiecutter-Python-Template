from {{cookiecutter.package_name}}.main import main

def test_main(capfd) -> None:
    """main should print "Hello World!" """
    # act
    main()

    # assert
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
    assert err == ""
