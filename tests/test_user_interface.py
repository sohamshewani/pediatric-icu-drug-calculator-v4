import pytest
from src.user_interface import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert 'Welcome to Pediatric ICU Drug Calculator' in captured.out
