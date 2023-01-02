#

# PLASTICITY of CD4+T to "The Big-8"  Optimization - Using the D-WaveSys QPU.
# Thomas E. Perez       Chair: Professor K. Mkrtchyan

'''
                            This application is a mixed-integer linear-programming optimization application.
                            It's also a constrained quadratic model (CQM) solver problem.
                            The paper that accompanies this application explains all the informatopm in details,
                            as it is a thesis paper.

                            The optimization uses a linear objective and constraints.
                            The variables (actually, objects) are "real-valued" and "integer" values. Eg.,
                            this relates to the Big-8 proteins (Pts), ie., the subsets of the CD4 T-help
                            cell in which the "Units" will be;
                            "continuous", (0 < inf in this app). These are AKA:
                            "REAL-VALUED" variables.

                            "Discrete" units (eg., ACTivation, DIFFerentiation, and Expression, can be construed
                             to be an ON/OFF state, they are AKA:
                            "INTEGER-VALUED" variables.
'''
'''
                            The attributes, 6 of them are embedded into a Pts{{..}} dict, and processed by user input.
                            The paper accompanying this application explains the details of the application, 
                            including the quantum paradigm used, as well as the process in simple and detailed form.

                            I' name "Big-8" as (=::) {Tfh, Th9, Th2, iTreg, Tr1, Th22, Th17, Th1}. Like the paper
                            explains, these may or may not evolve from the CD4+ t-cell, (heterogeneity).
'''
'''
As the paper also explains, it's highly encouraged for for me tp have the user or contributor to clone my 
Github repo:
    https://github.com/TomEphraimPerez/learnleap
to acquire all components and dependencies in order to correct, comment, modify or critique my work. 

Both:
>>> min_attributes = {"Expression": 1, "ACTivation": 2, "EXPansion": 3, "DIFFerentiation": 4}
>>> max_attoamps = 80  
are hard-coded and may be changed at any time by the user or coder/author.
'''
'''
This is a command-line driven application. Necessary and helpful commands are:
$ python -m venv ocean
$ . ocean/bin/activate
$ dwave ping --client qpu
$ dwave solvers --list --all

 Last application verion >>>
 $ python plasticityCD4toTh-8.py
 For testing/debugging   >>>
 $ plasticityCD4toTh-TESTONLY.py   
'''

'''
The Goal:
Given nominal attribute values of;
  min_attributes † = {"Expression": 1, "ACTivation": 2, "EXPansion": 3, "DIFFerentiation": 4}  # ARBITRARY
for each protein, we want to optimize the ACTivation at the cost of Plasticity, while maintaining the 
† minimum attributes' requirements.    

"(Total ACTivation of x.xx at Plasticity y.yy)"
is the weight of ACTivation against opposing PLasticity.

>>> max_attoamps = 80 
is here to demonstrate that a contributor to the Github repo (above) can arbitrarily change the open-source
coding to reflect an attribute (and assign values to it as normal). In this code, 'attoamos' is my concept
of what I believe is a valid attribute, albeit not standardized as of this writing. Signal Strength is a 
topic in citation [3] in the accompanying paper for this application, however.
'''

import dimod as dimod
from dwave.system import LeapHybridCQMSampler  # o
# from dimod.core import sampler
# from dwave.system import LeapHybridCQMSampler         #o
import re

# Python 3.9.2
print('It\'s advised that reading the research paper that accompanies this application, is read.')
print('This is a DWaveSys quantum computing CQM solver CD4+ T-help cell problem  on a simple mixed-integer'
      ' linear-programming,')
print('\n')
print('Whether it\'s to test heterogeneity or optimize T-cell types, it\'s a mixed-integer linear-programming'
      'optimization application optimization (MILP) prob.')

print('\nThis uses flexible user i/p T-help optimizations that can hopefully, with some sound')
print('logic and accuracy, be a useful application since it\'s a nascent application.')

print('There is no such Related Work section in the research paper that accompanies this application.')

print('Hopefully some GitHub forkers can contribute. The goal is to optimize CD4+ T-cell subsets as per')
print('Carbo et al, derived from the following attributes of each heterogeneous subset of the CD4+ T-cell:')
print('\n† attomaps, ACTivation, EXPansion, DIFFerentiation, Expression, and Plasticity.')
print('Not all these have to be included in the user input. \'Attoamps\', (10^-18 a) is a theory.')

print('\nPlease see the end of the comments in the open-source code for \'attoamps.\'')

print('The candidate subsets are:')
print('\nTfh, Th9, Th2, iTreg, Tr1, Tr22, Tr17 and Th1.')
print('All these T-helper cells (via heterogeneity) are what I\'ll refer to as \'The big-8\', since these 8')
print('were discussed by Carbo et al. This of course is cited, and is the primary source of inspiration')
print('for this thesis. Of course the thesis will explain in detail, most everything necessary.')

print('\n\tOf course, this application MUST/SHOULD BE BACKED UP BY LABORATORY verification and validation through')
print('\tdocumented experimentation and peer-reviewed results. This author is very open to suggestions and comments.')

print('\n\tInstructions are easy-to-follow instructions upon launching the application via CLI.')
print('\n\n')

# Self notes >>>
# attribute = ['Attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation', 'Expression', 'Plasticity']
# Pts dict of Pts' Pts.
# Attoamps -> picoamp = 10^-12a, femtoamps =10^-15a, Attoamps = 10^-18a.


# Declare 8 CD4+ T-help subset attributes for Proteins (Pts) nested dict on next block. There are 8 CD4+ T-help subsets
strattoamps1 = 0
strACTivation1 = 0
strEXPansion1 = 0
strDIFFerentiation1 = 0
strExpression1 = 0
strPlasticity1 = 0
Units1 = 'continuous'

strattoamps2 = 0
strACTivation2 = 0
strEXPansion2 = 0
strDIFFerentiation2 = 0
strExpression2 = 0
strPlasticity2 = 0
Units2 = 'continuous'

strattoamps3 = 0
strACTivation3 = 0
strEXPansion3 = 0
strDIFFerentiation3 = 0
strExpression3 = 0
strPlasticity3 = 0
Units3 = 'continuous'

strattoamps4 = 0
strACTivation4 = 0
strEXPansion4 = 0
strDIFFerentiation4 = 0
strExpression4 = 0
strPlasticity4 = 0
Units4 = 'continuous'

strattoamps5 = 0
strACTivation5 = 0
strEXPansion5 = 0
strDIFFerentiation5 = 0
strExpression5 = 0
strPlasticity5 = 0
Units5 = 'continuous'

strattoamps6 = 0
strACTivation6 = 0
strEXPansion6 = 0
strDIFFerentiation6 = 0
strExpression6 = 0
strPlasticity6 = 0
Units6 = 'continuous'

strattoamps7 = 0
strACTivation7 = 0
strEXPansion7 = 0
strDIFFerentiation7 = 0
strExpression7 = 0
strPlasticity7 = 0
Units7 = 'continuous'

strattoamps8 = 0
strACTivation8 = 0
strEXPansion8 = 0
strDIFFerentiation8 = 0
strExpression8 = 0
strPlasticity8 = 0
Units8 = 'continuous'

Pts = {'Tfh': {'Attoamps': strattoamps1, 'ACTivation': strACTivation1, 'EXPansion': strEXPansion1,
               'DIFFerentiation': strDIFFerentiation1, 'Expression': strExpression1, 'Plasticity': strPlasticity1,
               'Units': Units1},
       'Th9': {'Attoamps': strattoamps2, 'ACTivation': strACTivation2, 'EXPansion': strEXPansion2,
               'DIFFerentiation': strDIFFerentiation2, 'Expression': strExpression2, 'Plasticity': strPlasticity2,
               'Units': Units2},
       'Th2': {'Attoamps': strattoamps3, 'ACTivation': strACTivation3, 'EXPansion': strEXPansion3,
               'DIFFerentiation': strDIFFerentiation3, 'Expression': strExpression3, 'Plasticity': strPlasticity3,
               'Units': Units3},
       'iTreg': {'Attoamps': strattoamps4, 'ACTivation': strACTivation4, 'EXPansion': strEXPansion4,
                 'DIFFerentiation': strDIFFerentiation4, 'Expression': strExpression4, 'Plasticity': strPlasticity4,
                 'Units': Units4},
       'Tr1': {'Attoamps': strattoamps5, 'ACTivation': strACTivation5, 'EXPansion': strEXPansion5,
               'DIFFerentiation': strDIFFerentiation5, 'Expression': strExpression5, 'Plasticity': strPlasticity5,
               'Units': Units5},
       'Th22': {'Attoamps': strattoamps6, 'ACTivation': strACTivation6, 'EXPansion': strEXPansion6,
                'DIFFerentiation': strDIFFerentiation6, 'Expression': strExpression6, 'Plasticity': strPlasticity6,
                'Units': Units6},
       'Th17': {'Attoamps': strattoamps7, 'ACTivation': strACTivation7, 'EXPansion': strEXPansion7,
                'DIFFerentiation': strDIFFerentiation7, 'Expression': strExpression7, 'Plasticity': strPlasticity7,
                'Units': Units7},
       'Th1': {'Attoamps': strattoamps8, 'ACTivation': strACTivation8, 'EXPansion': strEXPansion8,
               'DIFFerentiation': strDIFFerentiation8, 'Expression': strExpression8, 'Plasticity': strPlasticity8,
               'Units': Units8}}

# Red ball-flags means that those lines were indented LEFT from original code that included REs, regular expressions.
# ============================ USER INPUT =====================================|||
# SUBSET 1
print('\n--- Attributes for --- Tfh')

flag = True  # O
while flag:
    strattoamps = input('Enter an int > 0 for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)
    # match_val = re.match(r"[+,-]?[0-9]+", strattoamps)  # OK for letters and a la r4 but not 4r.
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps1 = int(strattoamps)
print('You entered ', strattoamps1)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int > 0 for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation1 = int(strACTivation)
print('You entered', strACTivation1)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int > 0 for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion1 = int(strEXPansion)
print('You entered', strEXPansion1)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int > 0 for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation1 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation1)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int > 0 for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression1 = int(strExpression)
print('You entered', strExpression1)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int > 0 for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity1 = int(strPlasticity)
print('You entered', strPlasticity1)  # ===========================|

Units1 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units1)  # ===========================|
# ====================================================================|


# SUBSET 2
print('\n--- Attributes for --- Th9')

flag = True  # O
while flag:
    strattoamps = input('Enter an int > 0 for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps2 = int(strattoamps)
print('You entered ', strattoamps2)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int > 0 for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation2 = int(strACTivation)
print('You entered', strACTivation2)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int > 0 for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion2 = int(strEXPansion)
print('You entered', strEXPansion2)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int > 0 for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation2 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation2)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int > 0 for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression2 = int(strExpression)
print('You entered', strExpression2)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int > 0 for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity2 = int(strPlasticity)
print('You entered', strPlasticity2)  # ===========================|

Units2 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units2)  # ===========================|
# ====================================================================|


# SUBSET 3
print('\n--- Attributes for --- Th2')

flag = True  # O
while flag:
    strattoamps = input('Enter an int > 0 for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps3 = int(strattoamps)
print('You entered ', strattoamps3)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int > 0 for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation3 = int(strACTivation)
print('You entered', strACTivation3)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int > 0 for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion3 = int(strEXPansion)
print('You entered', strEXPansion3)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int > 0 for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation3 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation3)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int > 0 for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression3 = int(strExpression)
print('You entered', strExpression3)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int > 0 for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity3 = int(strPlasticity)
print('You entered', strPlasticity3)  # ===========================|

Units3 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units3)  # ===========================|
# ====================================================================|


# SUBSET 4
print('\n--- Attributes for --- iTreg')

flag = True  # O
while flag:
    strattoamps = input('Enter an int for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps4 = int(strattoamps)
print('You entered ', strattoamps4)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation4 = int(strACTivation)
print('You entered', strACTivation4)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion4 = int(strEXPansion)
print('You entered', strEXPansion4)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation4 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation4)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression4 = int(strExpression)
print('You entered', strExpression4)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity4 = int(strPlasticity)
print('You entered', strPlasticity4)  # ===========================|

Units4 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units4)  # ===========================|
# ====================================================================|


# SUBSET 5
print('\n--- Attributes for --- Tr1')

flag = True  # O
while flag:
    strattoamps = input('Enter a an int for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps5 = int(strattoamps)
print('You entered ', strattoamps5)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation5 = int(strACTivation)
print('You entered', strACTivation5)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion5 = int(strEXPansion)
print('You entered', strEXPansion5)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation5 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation5)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression5 = int(strExpression)
print('You entered', strExpression5)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity5 = int(strPlasticity)
print('You entered', strPlasticity5)  # ===========================|

Units5 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units5)  # ===========================|
# ====================================================================|


# SUBSET 6
print('\n--- Attributes for --- Th22')

flag = True  # O
while flag:
    strattoamps = input('Enter an int for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps6 = int(strattoamps)
print('You entered ', strattoamps6)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation6 = int(strACTivation)
print('You entered', strACTivation6)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion6 = int(strEXPansion)
print('You entered', strEXPansion6)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation6 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation6)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression6 = int(strExpression)
print('You entered', strExpression6)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity6 = int(strPlasticity)
print('You entered', strPlasticity6)  # ===========================|

Units6 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units6)  # ===========================|
# ====================================================================|


# SUBSET 7
print('\n--- Attributes for --- Th17')

flag = True  # O
while flag:
    strattoamps = input('Enter an int for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps7 = int(strattoamps)
print('You entered ', strattoamps7)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation7 = int(strACTivation)
print('You entered', strACTivation7)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion7 = int(strEXPansion)
print('You entered', strEXPansion7)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation7 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation7)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression7 = int(strExpression)
print('You entered', strExpression7)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity7 = int(strPlasticity)
print('You entered', strPlasticity7)  # ===========================|

Units7 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units7)  # ===========================|
# ====================================================================|


# SUBSET 8
print('\n--- Attributes for --- Th1')

flag = True  # O
while flag:
    strattoamps = input('Enter an int for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)  # ints & floats not preceded w letters, colon
    if match_val is None or int(strattoamps) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strattoamps8 = int(strattoamps)
print('You entered ', strattoamps8)  # ===========================|

flag = True
while flag:
    strACTivation = input('Enter an int for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None or int(strACTivation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strACTivation8 = int(strACTivation)
print('You entered', strACTivation8)  # ===========================|

flag = True
while flag:
    strEXPansion = input('Enter an int for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None or int(strEXPansion) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strEXPansion8 = int(strEXPansion)
print('You entered', strEXPansion8)  # ===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter an int for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None or int(strDIFFerentiation) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strDIFFerentiation8 = int(strDIFFerentiation)
print('You entered', strDIFFerentiation8)  # ===========================|

flag = True
while flag:
    strExpression = input('Enter an int for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None or int(strExpression) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strExpression8 = int(strExpression)
print('You entered', strExpression8)  # ===========================|

flag = True
while flag:
    strPlasticity = input('Enter an int for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None or int(strPlasticity) < 0:
        print("\n\t\tPlease enter a vAliD number.")
    else:
        flag = False
strPlasticity8 = int(strPlasticity)
print('You entered', strPlasticity8)  # ===========================|

Units8 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units8)  # ===========================|
# ============================= END USER INPUT ==============================|||


Pts = {'Tfh': {'Attoamps': strattoamps1, 'ACTivation': strACTivation1, 'EXPansion': strEXPansion1,
               'DIFFerentiation': strDIFFerentiation1, 'Expression': strExpression1, 'Plasticity': strPlasticity1,
               'Units': Units1},
       'Th9': {'Attoamps': strattoamps2, 'ACTivation': strACTivation2, 'EXPansion': strEXPansion2,
               'DIFFerentiation': strDIFFerentiation2, 'Expression': strExpression2, 'Plasticity': strPlasticity2,
               'Units': Units2},
       'Th2': {'Attoamps': strattoamps3, 'ACTivation': strACTivation3, 'EXPansion': strEXPansion3,
               'DIFFerentiation': strDIFFerentiation3, 'Expression': strExpression3, 'Plasticity': strPlasticity3,
               'Units': Units3},
       'iTreg': {'Attoamps': strattoamps4, 'ACTivation': strACTivation4, 'EXPansion': strEXPansion4,
                 'DIFFerentiation': strDIFFerentiation4, 'Expression': strExpression4, 'Plasticity': strPlasticity4,
                 'Units': Units4},
       'Tr1': {'Attoamps': strattoamps5, 'ACTivation': strACTivation5, 'EXPansion': strEXPansion5,
               'DIFFerentiation': strDIFFerentiation5, 'Expression': strExpression5, 'Plasticity': strPlasticity5,
               'Units': Units5},
       'Th22': {'Attoamps': strattoamps6, 'ACTivation': strACTivation6, 'EXPansion': strEXPansion6,
                'DIFFerentiation': strDIFFerentiation6, 'Expression': strExpression6, 'Plasticity': strPlasticity6,
                'Units': Units6},
       'Th17': {'Attoamps': strattoamps7, 'ACTivation': strACTivation7, 'EXPansion': strEXPansion7,
                'DIFFerentiation': strDIFFerentiation7, 'Expression': strExpression7, 'Plasticity': strPlasticity7,
                'Units': Units7},
       'Th1': {'Attoamps': strattoamps8, 'ACTivation': strACTivation8, 'EXPansion': strEXPansion8,
               'DIFFerentiation': strDIFFerentiation8, 'Expression': strExpression8, 'Plasticity': strPlasticity8,
               'Units': Units8}}

for p_id, p_info in Pts.items():
    print("\nNEW VALUES: ", p_id)
    for key in p_info:
        print(key + ':', p_info[key])

print('\n')
print('Pts ------------------- > > > ')
print(Pts)  # ok

print('\n')
# The '4' in DIFFerentiation: 4 REPEATS <-> Bug -   XXXXXXXXXXXXXXXXXX see notebook XXXXXXXXXXXXXXXXXXX
min_attributes = {"Expression": 1, "ACTivation": 2, "EXPansion": 3, "DIFFerentiation": 4}  # ARBITRARY ASMTs
max_attoamps = 80  # for setting up bounds. See line ~859 below. See end of comments above.

# quantities list | dimod is a shared API for samplers and provides classes for eg., QM's
# inc higher-order non-quadratic models.
# quantities = [dimod.Real(f"{Pt}") if Pts[Pt]["Units"] == "continuous"       # O an f-string. '{Pt}'..
quantities = [dimod.Real(f"{Pt}") if Pts[Pt]["Units"] == "continuous"
              else dimod.Integer(f"{Pt}")
              for Pt in Pts.keys()]  # key = eg amps : value = 2

print('\n')
'''
# test
print("\n(Simply showing ex of a lin bias) ")
print(quantities[0])                                    # simple linear bias
print("(Now showing an ex of a dbl bias) ")
print(2*quantities[0])                                  # Now dbl lin bias
#print(quantities[0] * quantities[1])       #Now a quadratic bias. # ValueError: REAL variables
                                                        # (e.g. 'Tfh') cannot have interactions
'''

for ind, Pt in enumerate(Pts.keys()):
    ub = max_attoamps / Pts[Pt]['Attoamps']  # O
    quantities[ind].set_upper_bound(Pt, ub)

qub = quantities[0].upper_bound("Tfh")  # quantity ub from Tfh=X, Th1=X, Th22=X, Th17=X,
print('\nquantities[0].ub (upper bound TESTONLY.py) is: ', qub)
print('\n\n')

# setup the OBJective Fn w a UTILity Fn                 # OBJECTIVE Fn     <<<
cqm = dimod.ConstrainedQuadraticModel()  # NOT arbitrarily set alpha=2 beta=1;


# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
# such as ACTivation;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (Pts[Pt][category] for Pt in Pts.keys())))
    # ZIP https://www.w3schools.com/python/ref_func_zip.asp -> ordered pairs (('',''),('','')) fr a=, b=

    # Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize DIFFn, DIFFn
    # is multiplied by -1 and minimized!

#cqm.set_objective( - total_mix(quantities, "ACTivation") + 1 * total_mix(quantities, "Plasticity")) # Lambda=15
cqm.set_objective(- total_mix(quantities, "ACTivation") + 2 * total_mix(quantities, "Plasticity"))  # Lambda=15
#cqm.set_objective( - total_mix(quantities, "ACTivation") + 6 * total_mix(quantities, "Plasticity")) # Lambda=6
#cqm.set_objective( - total_mix(quantities, "ACTivation") + 8 * total_mix(quantities, "Plasticity")) # Lambda=8
#cqm.set_objective( - total_mix(quantities, "ACTivation") + 15 * total_mix(quantities, "Plasticity")) # Lambda=15
# cqm.set_objective( - total_mix(quantities, "ACTivation") + 30 * total_mix(quantities, "Plasticity")) # Lambda=15
# YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY K E Y YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY K E Y YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
# YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY K E Y YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

# TUNING/Constraints
# Constrain the T-help’s MAXIMUM current i.
cqm.add_constraint(total_mix(quantities, "Attoamps") <= max_attoamps, label="Attoamps")  # rtn 'Attoamps'

# Require that the nominal MINIMUM of each Th attribute is met or exceeded.
# THIS CAN BE USER DEFINED AS WELL.
for attribute, amount in min_attributes.items():  # Items() is a BI.  # Note: 'MIN-ATTRs'
    cqm.add_constraint(total_mix(quantities, attribute) >= amount, label=attribute)
    'Expression'
    #   'ACTivation' # Already used in cqm.set_objective(-..) above. # UNcommenting makes a small chg in E-table.
    'EXPansion'
    'DIFFerentiation'

# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys())  # @overld. __def__ init(self). @ is polymorph.
# list(cqm.constraints.keys())                      # ['Attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation']
print('\nConstraints Dict w/ labels as keys: ', constraintsDictLabelsAsKeys)
print('Attoamps(has max) constraints (as polystr):', cqm.constraints['Attoamps'].to_polystring())
# Eg., 100*Tfh + 140*Th9 + 90*Th2 + 150*iTreg + 270*Tr1 + 300*Th22 <= 2000, what is gvn abv.
print('cqm.constraints[Expression].to_polystring(): ', cqm.constraints['Expression'].to_polystring())
# Eg., 3*Tfh + 17*Th9 + Th2 + 9*iTreg + 9*Tr1 + 4*Th22 >= 50  , what is gvn abv.

'''
Solve the Problem by Sampling
Solve the Problem by Sampling
D-Wave’s quantum cloud service provides cloud-based hybrid solvers we can submit arbitrary QMs to.
These solvers, which implement state-of-the-art classical algorithms together with:

    intelligent allocation

of the quantum processing unit (QPU) to parts of the problem where it benefits most, are designed to
accommodate even very large problems.
Ocean software’s dwave-system LeapHybridCQMSampler class enables you to easily incorporate Leap’s hybrid
CQM solvers into your application:
'''
# Make certain ur in (ocean) venv sampler = LeapHybridCQMSampler()
sampler = LeapHybridCQMSampler()

'''
Submit the CQM to the selected solver. For one particular execution, the CQM hybrid sampler returned 
"49 samples out of which 25 were solutions" 

    ["FEASIBILITY"] 

that met all the constraints eg.
CQM) solver on a simple mixed-integer linear-programming (MILP) type of optimization problem.
'''
sampleset = sampler.sample_cqm(cqm)  # SUBMIT THE PROBLEM to solver.
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  # A num. 'Filter' is a dimod API/class.
# 'filter' rtns a new sampleset with rows filtered by the given predicate.
# 'pred', a Fn th accepts a named tuple as returned by :meth:'.data', and rtns a :class:'bool'
# returns: A new sampleset with only the data rows for which 'pred' returns.
# lambda creates anonymous Fns -> function objective.
#   The expression, (lambda args : expression), yields a function object (here, it's "row.is_feasible").

print("\nThere are {} feasible solutions OUT of {}.\n".format(len(feasible_sampleset), len(sampleset)))


def print_Thelpers(sample):
    Thelp = {Pt: round(quantity, 1) for Pt, quantity in sample.items()}
    print(f"Thelp----->: {Thelp}")
    ACTivation_total = sum(Pts[Pt]["ACTivation"] * amount for Pt, amount in sample.items())
    Plasticity_total = sum(Pts[Pt]["Plasticity"] * amount for Pt, amount in sample.items())
    print(f"Total ACTivation of {round(ACTivation_total, 2)} at Plasticity {round(Plasticity_total, 2)}")
    for constraint in cqm.iter_constraint_data(sample):
        print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")
        # rhs_energy is a dimod float attribute


# The best solution found in this current execution was a T-help of Tr1 and (_ _ _), with
# Th22 completing the required DIFFerentiation and ACTivation portions
# ASSUMING (ACTivation vs DIFFERENtiation),  as opposed to (ACTivation vs Plasticity).
best = feasible_sampleset.first.sample
print('\nprint_T-HELPERS <- CD4T+ (Total ACTivation of x.xx at Plasticity y.yy) (BEST): ')
print_Thelpers(best)
''' >>>  a la:
Thelp: {'Th22': 1.0, 'Th2': 6.0, 'Tr1': 4.1, 'iTreg': 0.3, 'Tfh': 0.0, 'Th9': 0.0}
Total DIFFerentiation of 86.56 at Plasticity 9.46
ACTivation (nominal: 2000): 5
Attoamps (nominal: 50): 50
ACTivation (nominal: 30): 42
EXPansion (nominal: 130): 372
DIFFerentiation (nominal: 30): 46
>>>
The result is the same : )

In statistics, nominal data (also known as nominal scale) is a type of data that is used to label variables
    without providing any quantitative value. It is the simplest form of a scale of measure.
'''

'''
# TUNING THE SOLUTION
    # # ASSUMING (ACTivation vs DIFFERENtiation),  as opposed to (ACTivation vs Plasticity).
	# TUNING THE SOLUTION !
# RECALL; Objective function must maximize DIFFerentiation of the Thelp’s Pts while minimizing Plasticity.
	# So re min Plasticity, Plasticity_min  = min SUMMA_i (qty_i * Plasticity_i)
	#	            DIFFerentiation_max  = max SUMMA_i (qty_i * DIFFerentiation_i)




	# To optimize two different objectives, ACTivation and Plasticity, requires weighing one AGAINST the other.

 	# A simple way to do this, is to set priority weights; for example,
        #	OBJective = alpha(obj_1) + beta(obj_1). eg alpha can = 2, beta can = 1,
	    #	ie you double the priority of the first objective compared to the second.
'''

# Consider sampling each part of the combined objective ON ITS OWN (alpha=0, beta=1 and vv)
# and comparing the best solutions.

# Start with ACTivation: -----------------------------------------------------------------------||
cqm.set_objective(- total_mix(quantities, "ACTivation"))  # NOTE THE MINUS for least energy; eigenspectrum.
# ~O >>>
'''
print('\n\n\t\t\tACTn Energy Table (may be commentedOut) | Lowest Energy eigenvalue wins')
for sample, energy in sampleset.data(['sample', 'energy']):     # Fr class  # OK for test.
    print(sample, energy)
'''
sampleset_ACTivation = sampler.sample_cqm(cqm)  # RHS SAME AS line that's 21 lines down.
feasible_sampleset_ACTivation = sampleset_ACTivation.filter(lambda row: row.is_feasible)
best_ACTivation = feasible_sampleset_ACTivation.first
print('\n\nbest_ACTivation.ENERGY: ', round(best_ACTivation.energy))
# >>> a la -177

print('\n\nbest_ACTivation.SAMPLE: ')
print_Thelpers(best_ACTivation.sample)
# >>> a la;
'''
Thelp: {'Th22': 0.0, 'Th2': 17.0, 'Tr1': 0.0, 'iTreg': 0.0, 'Tfh': 0.0, 'Th9': 3.3}
Total ACTivation of 6 at Plasticity 3.1 rounded off:
    ACTivation (nominal: 4): 2
    Attoamps (nominal: 2): 0.1
    EXPansion (nominal: 3): 2
    DIFFerentiation (nominal: 5): 2
'''

# NOW with Plasticity:  --------------------------------------------------------------------------||
cqm.set_objective(total_mix(quantities, "Plasticity"))  # + total mix !
# ~O >>>
print('\n\n\n\t\t\t\t-----------------------------------------------------')
'''
print('\n\n\t\t\tPlastic Energy Table (may be commentedOut) | Lowest Energy eigenvalue wins')
for sample, energy in sampleset.data(['sample', 'energy']):     # Fr class  # OK for test.
    print(sample, energy)
'''
sampleset_Plasticity = sampler.sample_cqm(cqm)  # RHS SAME AS line that's 21 lines up.
feasible_sampleset_Plasticity = sampleset_Plasticity.filter(lambda row: row.is_feasible)
best_Plasticity = feasible_sampleset_Plasticity.first
print('\n\nbest_Plasticity.ENERGY: ', round(best_Plasticity.energy))
# >>> a la xxx

print('\n\nbest_Plasticity.SAMPLE: ')
print_Thelpers(best_Plasticity.sample)

# ~O >>>
# USE/ fr line 933
# sampleset = sampler.sample_cqm(cqm)  # SUBMIT THE PROBLEM to solver.
'''  
for sample, energy in sampleset.data(['sample', 'energy']): # O
    print(sample, energy)
'''

print('\n\n\t\t\t\t\t\t\t\tEND')
print('\n\n\t\t\t\t\t\t\t\tCharge time >>>')
ssi = sampleset.info                        # fr Docs.
print(ssi)
print('\n\n')
'''>>> a la
Thelp: {'Th22': 1.0, 'Th2': 0.0, 'Tr1': 5.3, 'iTreg': 0.0, 'Tfh': 0.0, 'Th9': 0.0}
Total ACTivation of 7 at Plasticity 3.3
    Attoamps (nominal: 2): 0.2
    ACTivation (nominal: 6): 4
    EXPansion (nominal: 3): 1
    DIFFerentiation (nominal: 5): 3
'''
'''
This combination is ranked as less ACTivated than the previous but more Plastic. 
It relies mainly on Tr1 and uses Th22 to add ACTivation and DIFFerentiation.
'''
'''
Because of the differences in energy scale between the two parts of the combined objective,
177 >> 3,  if you do not multiply the part representing Plasticity by some positive factor, optimal 
solutions will maximize ACTivation and neglect Plasticity. That is, if in 

obj = alpha(obj1 + beta(obj2)), you set alpha=1=beta.

solutions will likely be 
  close or 
  identical 
to those found when optimizing for ACTivation alone.
'''

''' SEE GRAPH with y-axis=Energy, x-axis=Multiplier, variables are ACTivation, Plasticity and total. 
# This quantum application is an adaptation from DWaveSys quantum code from:
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-Thelp-reals
'''

'''
 ††† (Recall; Set the objective2. Because Ocean solvers minimize objectives, to maximize ACTivation, 
    ACTivation is multiplied by -1 and minimized.)
# This quantum application is an adaptation from DWaveSys quantum code from:
# https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-Thelp-reals ††
'''

'''
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4074550/
The fact that it is possible to reprogram cells by either perturbing their environment or changing their 
genomic output artificially, indicates that that the 
plasticity of the activated state may not be restricted 
to simple animals, and that programs for activation (or diff'n) may be more prevalent and much more 
broadly distributed among all animals (including humans) than most care to contemplate at the present time.
'''

