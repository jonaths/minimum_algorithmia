import os
import sys

# Para incluir src en el path
testdir = os.path.dirname(__file__)
srcdir = '../src'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

from src import algorithmia_demo


def test_algorithmia_demo():
    assert algorithmia_demo.apply("Jane") == "hello Jane"
