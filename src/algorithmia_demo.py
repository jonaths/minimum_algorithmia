"""Algorithm Development Kit (ADK) algorithm-creation template.

* This template uses Algorithmia's ADK module to provide structure for algorithm development. For details see:
      https://algorithmia.com/developers/algorithm-development/languages/python#what-is-an-algorithm-development-kit-adk
      https://github.com/algorithmiaio/algorithmia-adk-python

* API calls begin at the `apply` function, with the JSON request body deserialized and passed as `input`.

* The instantiation of an `ADK` object is what turns your library code into an algorithm that can run on Algorithmia.

* The `ADK.init` method is what actually starts the algorithm. To explore further, see the source code linked above.

* If your algorithm relies on in-memory data (e.g., large model files) that are the same every time the algorithm
  is executed, you can load those data into a `globals` object in a `load` function and pass that to `apply`, i.e.:

      ...
      def apply(input, globals):
          return "hello {} {}".format(str(input), str(globals["payload"]))

      def load():
          globals = {}
          globals["payload"] = "Loading has been completed."
          return globals

      algorithm = ADK(apply, load)
      ...
"""

import os
import sys

# Para incluir src en el path y no tener que usar imports relativos
testdir = os.path.dirname(__file__)
srcdir = '../src'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

from Algorithmia import ADK
from module_bla.say_hi import hello


def load():
    globals = {"payload": "Nice to meet you. "}
    return globals


def apply(input, globals):
    """
    LLama a una función importada localmente y la concatena con un valor recuperado localmente.
    Podría ser un modelo.
    """
    return f'{hello(input)} {globals["payload"]}'


algorithm = ADK(apply, load)
algorithm.init("Algorithmia")
