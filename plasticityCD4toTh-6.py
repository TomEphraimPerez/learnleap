                        # PLASTICITY of CD4+T to "The Big-8"  Optimization -
                            # Big-8 ::= Tfh, Th9, Th2, iTreg, Tr1, Th22, Th17, Th1
                            # attributes to the BIG-8: AED + plasticity, current, expression.
                            
# This app'is a CQM solver problem on a simple mixed-integer linear-programming, (MILP) type of optimization.
# This quantum application is an adaptation from DWaveSys quantum code from:
 # https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-Thelp-reals ††


import dimod as dimod       # thx red lightbulb
from dwave.system import LeapHybridCQMSampler           #o
# from dimod.core import sampler
# from dwave.system import LeapHybridCQMSampler         #o
import re
 # solver has options. [See the solve-by sampling section toward the end ††]
  # For charges - $$$
    # Select a solver
    # sampler = LeapHybridSampler()
    # Submit for solution
    # answer = sampler.sample_qubo(Q)

# Python 3.9.2

print('This is DWaveSys quantum computing CQM solver prob on a simple mixed-integer linear-programming,')
print('MILP) type of optimization prob.')
print('\nThis is a flexible user i/p T-help optimization problem that can hopefully with some sound')
print('logic and accuracy initially, be a useful application since it\'s somewhat of a nascent application.')
print('Hopefully some GitHub forkers can contribute. The goal is to optimize CD4+ T-cell subsets as per')
print('Carbo et al, derived from the following attributes of each heterogeneous subset of the CD4+ T-cell:')

print('\n† attomaps, ACTivation, EXPansion, DIFFerentiation, Expression, and Plasticity.')
print('Not all these have to be included in the user input. \'Attoamps\', (10^-18 a) is a theory.')
print('Ie., I declare, with the aid of citations, a little experience, logic and heuristics, to be a valid')
print('and necessary attribute. The candidate subsets are:')

print('\nTfh, Th9, Th2, iTreg, Tr1, Tr22, Tr17 and Th1.')
print('All these T-helper cells (via heterogeneity) are what I\'ll refer to as \'The big-8\', since these 8')
print('were discussed by Carbo et al. This of course is cited, and is the primary source of inspiration')
print('for this thesis. Of course the thesis will explain in detail.')

print('\n\tOSTENSIBLY - this application MUST BE BACKED UP BY LABORATORY verification and validation through')
print('\tdocumented experimentation and results. This author is OPEN to suggestions amd comments.')
print('\n\n')

# Self notes:
# attribute = ['Attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation', 'Expression', 'Plasticity']
# Pts dict of Pts' Pts.
# Attoamps -> picoamp = 10^-12a, femtoamps =10^-15a, Attoamps = 10^-18a.


'''
                # INITIALIZE >>>   THIS WORKS !     USER I/P DOES  NOT WORK !!
                
Pts = {'Tfh': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Th9': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Th2': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'iTreg': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Tr1': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Th22': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Th17': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'},
        'Th1': {'Attoamps': 1, 'ACTivation': 1, 'EXPansion': 1, 'DIFFerentiation': 1,
                    'Expression': 1, 'Plasticity': 1, 'Units': 'continuous'}}
'''

'''
                                                        # INITIALIZE >>>
Pts = {'Tfh': {},
       'Th9': {},
       'Th2': {},
       'iTreg': {},
       'Tr1': {},
       'Th22': {},
       'Th17': {},
       'Th1': {}}
'''
strattoamps1 = 0.1
strACTivation1 = 0.1
strEXPansion1 = 0.1
strDIFFerentiation1 = 0.1
strExpression1 = 0.1
strPlasticity1 = 0.1
Units1 = 'continuous'

strattoamps2 = 0.1
strACTivation2 = 0.1
strEXPansion2 = 0.1
strDIFFerentiation2 = 0.1
strExpression2 = 0.1
strPlasticity2 = 0.1
Units2 = 'continuous'

strattoamps3 = 0.1
strACTivation3 = 0.1
strEXPansion3 = 0.1
strDIFFerentiation3 = 0.1
strExpression3 = 0.1
strPlasticity3 = 0.1
Units3 = 'continuous'

strattoamps4 = 0.1
strACTivation4 = 0.1
strEXPansion4 = 0.1
strDIFFerentiation4 = 0.1
strExpression4 = 0.1
strPlasticity4 = 0.1
Units4 = 'continuous'

strattoamps5 = 0.1
strACTivation5 = 0.1
strEXPansion5 = 0.1
strDIFFerentiation5 = 0.1
strExpression5 = 0.1
strPlasticity5 = 0.1
Units5 = 'continuous'

strattoamps6 = 0.1
strACTivation6 = 0.1
strEXPansion6 = 0.1
strDIFFerentiation6 = 0.1
strExpression6 = 0.1
strPlasticity6 = 0.1
Units6 = 'continuous'

strattoamps7 = 0.1
strACTivation7 = 0.1
strEXPansion7 = 0.1
strDIFFerentiation7 = 0.1
strExpression7 = 0.1
strPlasticity7 = 0.1
Units7 = 'continuous'

strattoamps8 = 0.1
strACTivation8 = 0.1
strEXPansion8 = 0.1
strDIFFerentiation8 = 0.1
strExpression8 = 0.1
strPlasticity8 = 0.1
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



#============================ USER INPUT =====================================|||
# SUBSET 1
print('\n--- Attributes for --- Tfh')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    #match_val = re.match("[-+]?\\d+([/.]\\d+)?$", strattoamps) #ints & floats not preceded w letters, colon
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps1 = strattoamps
print('You entered ', strattoamps1)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation1 = strACTivation
print('You entered' , strACTivation1)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion1 = strEXPansion
print('You entered' , strEXPansion1)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation1 = strDIFFerentiation
print('You entered', strDIFFerentiation1)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression1 = strExpression
print('You entered', strExpression1)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity1 = strPlasticity
print('You entered', strPlasticity1)                    #===========================|

Units1 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units1)                            #===========================|
#====================================================================|


# SUBSET 2
print('\n--- Attributes for --- Th9')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps2 = strattoamps
print('You entered ', strattoamps2)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation2 = strACTivation
print('You entered' , strACTivation2)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion2 = strEXPansion
print('You entered' , strEXPansion2)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation2 = strDIFFerentiation
print('You entered', strDIFFerentiation2)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression2 = strExpression
print('You entered', strExpression2)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity2 = strPlasticity
print('You entered', strPlasticity2)                    #===========================|

Units2 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units2)                            #===========================|
#====================================================================|


# SUBSET 3
print('\n--- Attributes for --- Th2')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps3 = strattoamps
print('You entered ', strattoamps3)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation3 = strACTivation
print('You entered' , strACTivation3)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion3 = strEXPansion
print('You entered' , strEXPansion3)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation3 = strDIFFerentiation
print('You entered', strDIFFerentiation3)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression3 = strExpression
print('You entered', strExpression3)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity3 = strPlasticity
print('You entered', strPlasticity3)                    #===========================|

Units3 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units3)                            #===========================|
#====================================================================|


# SUBSET 4
print('\n--- Attributes for --- iTreg')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps4 = strattoamps
print('You entered ', strattoamps4)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation4 = strACTivation
print('You entered' , strACTivation4)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion4 = strEXPansion
print('You entered' , strEXPansion4)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation4 = strDIFFerentiation
print('You entered', strDIFFerentiation4)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression4 = strExpression
print('You entered', strExpression4)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity4 = strPlasticity
print('You entered', strPlasticity4)                    #===========================|

Units4 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units4)                            #===========================|
#====================================================================|


# SUBSET 5
print('\n--- Attributes for --- Tr1')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps5 = strattoamps
print('You entered ', strattoamps5)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation5 = strACTivation
print('You entered' , strACTivation5)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion5 = strEXPansion
print('You entered' , strEXPansion5)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation5 = strDIFFerentiation
print('You entered', strDIFFerentiation5)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression5 = strExpression
print('You entered', strExpression5)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity5 = strPlasticity
print('You entered', strPlasticity5)                    #===========================|

Units5 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units5)                            #===========================|
#====================================================================|


# SUBSET 6
print('\n--- Attributes for --- Tr22')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps6 = strattoamps
print('You entered ', strattoamps6)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation6 = strACTivation
print('You entered' , strACTivation6)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion6 = strEXPansion
print('You entered' , strEXPansion6)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation6 = strDIFFerentiation
print('You entered', strDIFFerentiation6)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression6 = strExpression
print('You entered', strExpression6)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity6 = strPlasticity
print('You entered', strPlasticity6)                    #===========================|

Units6 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units6)                            #===========================|
#====================================================================|


# SUBSET 7
print('\n--- Attributes for --- Th17')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps7 = strattoamps
print('You entered ', strattoamps7)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation7 = strACTivation
print('You entered' , strACTivation7)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion7 = strEXPansion
print('You entered' , strEXPansion7)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation7 = strDIFFerentiation
print('You entered', strDIFFerentiation7)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression7 = strExpression
print('You entered', strExpression7)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity7 = strPlasticity
print('You entered', strPlasticity7)                    #===========================|

Units7 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units7)                            #===========================|
#====================================================================|


# SUBSET 8
print('\n--- Attributes for --- Th1')

flag = True                                             # O
while flag:
    strattoamps = input('Enter a float for Attoamps: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strattoamps) #ints & floats not preceded w letters, colon
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strattoamps8 = strattoamps
print('You entered ', strattoamps8)                     #===========================|

flag = True
while flag:
    strACTivation = input('Enter value for ACTivation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strACTivation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strACTivation8 = strACTivation
print('You entered' , strACTivation8)                   #===========================|

flag = True
while flag:
    strEXPansion = input('Enter value for EXPansion: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strEXPansion)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strEXPansion8 = strEXPansion
print('You entered' , strEXPansion8)                    #===========================|

flag = True
while flag:
    strDIFFerentiation = input('Enter value for DIFFerentiation: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strDIFFerentiation)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strDIFFerentiation8 = strDIFFerentiation
print('You entered', strDIFFerentiation8)               #===========================|

flag = True
while flag:
    strExpression = input('Enter value for Expression: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strExpression)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strExpression8 = strExpression
print('You entered', strExpression8)                    #===========================|

flag = True
while flag:
    strPlasticity = input('Enter value for Plasticity: ')
    match_val = re.match(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+", strPlasticity)
    if match_val is None:
        print("\n\t\tPlease enter a vAliD DecImal number.")
    else:
        flag = False
strPlasticity8 = strPlasticity
print('You entered', strPlasticity8)                    #===========================|

Units8 = input('Enter \'continuous\' or \'disrete\' ')
print('You entered', Units8)                            #===========================|
#============================= END USER INPUT ==============================|||




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
print(Pts)                                            # ok

print('\n')

min_attributes = {"Expression": 1.1, "ACTivation": 1.2, "EXPansion": 1.3, "DIFFerentiation": 1.4} # ARBITRARY ASMTs
max_attoamps = 100                                     # for setting up bounds. See 12 lines below.


# quantities list | dimod is a shared API for samplers and provides classes for eg., QM's
  # inc higher-order non-quadratic models.
# quantities = [dimod.Real(f"{Pt}") if Pts[Pt]["Units"] == "continuous"       # O an f-string. '{Pt}'..
quantities = [dimod.Real(f"{Pt}") if Pts[Pt]["Units"] == "continuous"
                                                        # ..will be replaced by a value.
    else dimod.Integer(f"{Pt}")
    for Pt in Pts.keys()]                     # key = eg amps : value = 2


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
    ub = max_attoamps/Pts[Pt]['Attoamps']       # O
    print('\t\t\tUB = ', ub)                    # --->>. 100 :)
    quantities[ind].set_upper_bound(Pt, ub)

qub = quantities[0].upper_bound("Tfh")	# quantity ub fro Tfh=X, Th1=X, Th22=X, Th17=X,
print('\nquantities[0].ub (upper bound) is: ', qub)                   # -> 20.0
print('\n\n')

# setup the OBJective Fn w a UTILity Fn             # OBJECTIVE Fn     <<<
cqm = dimod.ConstrainedQuadraticModel()			    # NOT arbitrarily set alpha=2 beta=1;

# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
  # such as ACTivation;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (Pts[Pt][category] for food in Pts.keys()) ) )
    # ZIP https://www.w3schools.com/python/ref_func_zip.asp -> ordered pairs (('',''),('','')) fr a=, b=

# Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize DIFFn, DIFFn
   # is multiplied by -1 and minimized.
cqm.set_objective(-total_mix(quantities, "DIFFerentiation") + 6 * total_mix(quantities, "Plasticity"))#NEED '-tot'

# TUNING/Constraints
# Constrain the Thelp’s MAXIMUM current i.
cqm.add_constraint(total_mix(quantities, "Attoamps") <= max_attoamps, label="Attoamps") # rtn 'Attoamps'


# Require that the nominal MINIMUM of each Th attribute is met or exceeded.
# THIS SHOULD BE USER DEFINED AS WELL.
for attribute, amount in min_attributes.items():        # Items() is a BI.  # Note: 'MIN-ATTRs'
    cqm.add_constraint(total_mix(quantities, attribute) >= amount, label=attribute)
    'Expression'
    'ACTivation'
    'EXPansion'
    'DIFFerentiation'

# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys()) #@overld. __def__ init(self). @ is polymorph.
# list(cqm.constraints.keys())              # ['Attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation']
print('\nConstraints Dict w/ labels as keys: ', constraintsDictLabelsAsKeys)
print('Attoamps(has max) constraints (as polystr):', cqm.constraints['Attoamps'].to_polystring())# hates Attoamps
    # 100*Tfh + 140*Th9 + 90*Th2 + 150*iTreg + 270*Tr1 + 300*Th22 <= 2000, what is gvn abv
print('Expression constraints (as polystr):', cqm.constraints['Expression'].to_polystring())
    # 3*Tfh + 17*Th9 + Th2 + 9*iTreg + 9*Tr1 + 4*Th22 >= 50  , what is gvn abv

'''
Solve the Problem by Sampling
Solve the Problem by Sampling
D-Wave’s quantum cloud service provides cloud-based hybrid solvers you can submit arbitrary QMs to.
These solvers, which implement state-of-the-art classical algorithms together with intelligent allocation
of the quantum processing unit (QPU) to parts of the problem where it benefits most, are designed to
accommodate even very large problems.
Ocean software’s dwave-system LeapHybridCQMSampler class enables you to easily incorporate Leap’s hybrid
CQM solvers into your application:
'''
# Make certain ur in (ocean) venv sampler = LeapHybridCQMSampler()
sampler = LeapHybridCQMSampler()

'''
Submit the CQM to the selected solver. For one particular execution, the CQM hybrid sampler returned 
49 samples, out of which 25 were solutions that met all the constraints.
CQM) solver on a simple mixed-integer linear-programming (MILP) type of optimization problem.
'''
sampleset = sampler.sample_cqm(cqm)                     # SUBMIT THE PROBLEM to solver.
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)# A num. 'Filter' is a dimod API/class.
    # 'filter' rtns a new sampleset with rows filtered by the given predicate. From dimod.
    # 'pred', a Fn th accepts a named tuple as returned by :meth:'.data', and rtns a :class:'bool'
    # lambda creates anonymous Fns -> function obj.

print("\nThere are {} feasible solutions OUT of {}.\n".format(len(feasible_sampleset), len(sampleset)))
def print_Thelpers(sample):
    Thelp = {Pt: round(quantity, 1) for Pt, quantity in sample.items()} # 'Pt:' has 1 dec place?
    print(f"Thelp----->: {Thelp}")
    DIFFerentiation_total = sum(Pts[Pt]["DIFFerentiation"] * amount for Pt, amount in sample.items())
    Plasticity_total =  sum(Pts[Pt]["Plasticity"] * amount for Pt, amount in sample.items())
    print(f"Total DIFFerentiation of {round(DIFFerentiation_total, 2)} at Plasticity {round(Plasticity_total, 2)}")
    for constraint in cqm.iter_constraint_data(sample):
        print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")
                                                        # rhs_energy is a dimod float attribute
# The best solution found in this current execution was a T-help of Tr1 and bananas, with
# Th22 completing the required DIFFerentiation and ACTivation portions
best = feasible_sampleset.first.sample
print('\nprint_T-HELPERS <- CD4T+ (differentiated or via plasticity) (BEST): ')
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
'''

'''
# TUNING THE SOLUTION
	# # TUNING THE SOLUTION !
# RECALL; Objective function must maximize DIFFerentiation of the Thelp’s Pts while minimizing purchase Plasticity.
	# So re min Plasticity, Plasticity_min  = min SUMMA_i (qty_i * Plasticity_i)
	#	            DIFFerentiation_max  = max SUMMA_i (qty_i * DIFFerentiation_i)
	
	# To optimize two different objectives, DIFFerentiation and Plasticity, requires weighing one AGAINST the other.
	 
 	# A simple way to do this, is to set priority weights; for example,
        #	OBJective = alpha(obj_1) + beta(obj_1). eg alpha can = 2, beta can = 1,
	    #	ie you double the priority of the first objective compared to the second.
'''

#Consider sampling each part of the combined objective ON ITS OWN (alpha=0, beta=1 and vv)
	# and comparing the best solutions.

	# Start with DIFFerentiation: -----------------------------------------------------------------------||
cqm.set_objective(-total_mix(quantities, "DIFFerentiation"))    # NOTE THE MINUS
sampleset_DIFFerentiation = sampler.sample_cqm(cqm)             # RHS SAME AS line that's 21 lines down.
feasible_sampleset_DIFFerentiation = sampleset_DIFFerentiation.filter(lambda row: row.is_feasible)
best_DIFFerentiation = feasible_sampleset_DIFFerentiation.first
print('best_DIFFerentiation.ENERGY: ', round(best_DIFFerentiation.energy))
# >>> a la -177

print('\nbest_DIFFerentiation.SAMPLE: ')
print_Thelpers(best_DIFFerentiation.sample)
# >>> a la;
'''
Thelp: {'Th22': 0.0, 'Th2': 17.0, 'Tr1': 0.0, 'iTreg': 0.0, 'Tfh': 0.0, 'Th9': 3.3}
Total DIFFerentiation of 6 at Plasticity 3.1 rounded off:
    ACTivation (nominal: 4): 2
    Attoamps (nominal: 2): 0.1
    ACTivation (nominal: 6): 3
    EXPansion (nominal: 3): 2
    DIFFerentiation (nominal: 5): 2
'''



    # NOW with Plasticity:  --------------------------------------------------------------------------||
cqm.set_objective(total_mix(quantities, "Plasticity"))
sampleset_Plasticity = sampler.sample_cqm(cqm)          # RHS SAME AS line that's 21 lines up.
feasible_sampleset_Plasticity = sampleset_Plasticity.filter(lambda row: row.is_feasible)
best_DIFFerentiation = feasible_sampleset_Plasticity.first
print(round(best_DIFFerentiation.energy))
	# >>> 3

print('\nbest_DIFFerentiation.SAMPLE: ')
print_Thelpers(best_DIFFerentiation.sample)


print('\n\n\t\t\t\t\t\tEND')
print('\n\n')
'''>>> a la
Thelp: {'Th22': 1.0, 'Th2': 0.0, 'Tr1': 5.3, 'iTreg': 0.0, 'Tfh': 0.0, 'Th9': 0.0}
Total DIFFerentiation of 7 at Plasticity 3.3
    ACTivation (nominal: 4): 3
    Attoamps (nominal: 2): 0.2
    ACTivation (nominal: 6): 4
    EXPansion (nominal: 3): 1
    DIFFerentiation (nominal: 5): 3
'''
'''
This Thelp is ranked as less tasty than the previous but much cheaper. 
It relies mainly on Tr1 and uses Th22 to add leaveACTivation and DIFFerentiation.
'''
'''
Because of the differences in energy scale between the two parts of the combined objective,
177 >> 3,  if you do not multiply the part representing Plasticity by some positive factor, optimal 
solutions will maximize DIFFerentiation and neglect Plasticity. That is, if in 
obj - alpha(obj1 + beta(obj2)), you set alpha=1=beta.
solutions will likely be 
  close or 
  identical 
to those found when optimizing for DIFFerentiation alone.
'''

''' SEE GRAPH with y-axis=Energy, x-axis=Multiplier, variables are DIFFerentiation, Plasticity and total. 
# This quantum application is an adaptation from DWaveSys quantum code from:
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-Thelp-reals
'''

'''
 ††† (Recall; Set the objective2. Because Ocean solvers minimize objectives, to maximize DIFFerentiation, 
    DIFFerentiation is multiplied by -1 and minimized.)
'''

