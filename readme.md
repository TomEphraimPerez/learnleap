
LIst all the virtual environments created with venv
find ~ -d -name "site-packages" 2>/dev/null

python -m venv ocean				# **	# Create a venv
. ocean/bin/activate				# Activate it.


pip install dwave-ocean-sdk
pip install git+https://github.com/dwavesystems/dwave-ocean-sdk
dwave setup


Creating new configuration file: /home/jane/.config/dwave/dwave.conf
Profile [defaults]: ↵
Updating existing profile: defaults
Authentication token [skip]: ABC-1234567890abcdef1234567890abcdef ↵
Configuration saved.

API Token = $ dwave solvers  --list --all

$ dwave solvers --list --region eu-central-1 	#or
$ dwave solvers  --list --all   		# or to 
  using dwave-cloud-client to query for hybrid solvers.
	>>> from dwave.cloud import Client
	>>> with Client.from_config() as client:
	   print(client.get_solvers(hybrid=True))

By default, Ocean connects to North American (region na-west-1)

$ dwave config --help

s-API Token DEV-f9*

$ dwave config create         	#     s-API Token DEV-f9*

$ dwave ping --client qpu	# make sure ur in ocean env **
	# or
$ dwave sample --random-problem	# to produce a random prob to a remote solver

In the AM:
$  . ocean/bin/activate



/////////////////////////// NOTES ////// (Use/ pycharm) //////////////////////////////////////////
dimod 
is a shared API for samplers. It provides classes for QMs, quadratic models. (...even 
higher-ordered non-QMs). ((You can invoke functions with it))
eg., BQM => QUBO or Ising
It also provides abstract base classes for constructing samplers and composed samplers.
It also provides reference examples of samplers and composed samplers.\

eg., for the LIST, quantities;
quantities = [dimod.Real(f"{food}") if foods[food]["Units"] == "continuous"
...                                     else dimod.Integer(f"{food}")
...                                     for food in foods.keys()]
BTW
the VARIABLES (are QM OBJECTS!), are Real values and Integer values, respectively, "{food}" being continuous and "{food}"
being and integer, (eg., rice or tofu in continuous and bananas and avocados are discreet.) 
( https://docs.ocean.dwavesys.com/en/stable/docs_dimod/sdk_index.html )

Multiplying two such “variables” 
creates a quadratic bias, $ python
>>> quantities[0] * quantities[1]
  QuadraticModel({'rice': 0.0, 'tofu': 0.0}, {('tofu', 'rice'): 1.0}, 0.0,
   ... {'rice': 'REAL', 'tofu': 'REAL'}, dtype='float64')
((quantities[0] * quantities[1] * quantities[2] cannot generate a quadratic model and results in an error.))

Minorminer 
is a tool for finding graph minors, developed to embed Ising problems onto quantum annealers (QA). Where it can be used to find minors in arbitrary graphs, it is particularly geared towards the state of the art in QA: problem graphs of a few to a few hundred variables, and hardware graphs of a few thousand qubits.

gitpod.io/#https://github.com/gitpod-io/website      eg., add  gitpod.io/# like:
gitpod.io/#https://github.com/TomEphraimPerez/learnleap
/////////////// END //////// NOTES ////////////////////////////////////////////////////////






