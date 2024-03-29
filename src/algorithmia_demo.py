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
import Algorithmia

# para incluir app en el path...
testdir = os.path.dirname(__file__)
srcdir = '../src'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

from Algorithmia import ADK
from module_bla.say_hi import hello

client = Algorithmia.client()


def apply(input):

    # creds = client.file('data://jserrano/test_data/data.json').getJson()

    print("in apply")
    return hello(input)


algorithm = ADK(apply)
algorithm.init("Algorithmia")
