                        # PLASTICITY of CD4+T to "The Big-8"  Optimization -
                            # Big-8 ::= Tfh, Th9, Th2, iTreg, Tr1, Th22, Th17, Th1
                            # attributes to the BIG-8: AED + plasticity, current, expression.
                            
# This app'is a CQM solver problem on a simple mixed-integer linear-programming, (MILP) type of optimization.
# This quantum application is an adaptation from DWaveSys quantum code from:
 # https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-Thelp-reals ††


import dimod as dimod       # thx red lightbulb
from dwave.system import LeapHybridCQMSampler         #o
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


print('\n\tFor Tfh: ')
#attr1 = ('\tSelect attribute \'attr1\' for Tfh.')
flag = True
attr1 = None
while flag:
    attr1 = input("\tplease input a valid float for attribute for Tfh: " )
    match_val = re.match("[-+]?\\d+([/.]\\d+)?$", attr1)
    if match_val is None:
        print("\n\t\tPlease enter a valid decimal number.")
    else:
        flag = False
number = float(attr1)
print("\tThe input number is:", number)
print('\n\n\n')



# Pts dict of Pts' Pts.
# attoamps -> picoamp = 10^-12a, femtoamps =10^-15a, attoamps = 10^-18a.
Pts = {'Tfh': {'attoamps': 0.39, 'ACTivation': 1.1, 'EXPansion': 22.3, 'DIFFerentiation': 2.1,
                    'Expression': 7.7, 'Plasticity': 2.5, 'Units': 'continuous'},
        'Th9': {'attoamps': 0.17, 'ACTivation': 5.0, 'EXPansion': 3.1, 'DIFFerentiation': 2.2,
                    'Expression': 2, 'Plasticity': 4.0, 'Units': 'continuous'},
        'Th2': {'attoamps': 0.11, 'ACTivation': 2.3, 'EXPansion': 23.5, 'DIFFerentiation': 3.6,
                    'Expression': 10.1, 'Plasticity': 1.0, 'Units': 'continuous'},
        'iTreg': {'attoamps': 0.91, 'ACTivation': 4.1, 'EXPansion': 25.6, 'DIFFerentiation': 4.9,
                    'Expression': 3.5, 'Plasticity': 1.0, 'Units': 'continuous'},
        'Tr1': {'attoamps': 0.83, 'ACTivation': 3.8, 'EXPansion': 50.5, 'DIFFerentiation': 3.1,
                    'Expression': 5.4, 'Plasticity': 0.25, 'Units': 'continuous'},
        'Th22': {'attoamps': 0.44, 'ACTivation': 1.2, 'EXPansion': 20.7, 'DIFFerentiation': 14.5,
                    'Expression': 5.6, 'Plasticity': 2.0, 'Units': 'continuous'},
        'Th17': {'attoamps': 0.36, 'ACTivation': 4.3, 'EXPansion': 28.8, 'DIFFerentiation': 14.6,
                    'Expression': 5.7, 'Plasticity': 2.0, 'Units': 'continuous'},
        'Th1': {'attoamps': 0.52, 'ACTivation': 5.7, 'EXPansion': 12.2, 'DIFFerentiation': 15.9,
                    'Expression': 6.8, 'Plasticity': 3.7, 'Units': 'continuous'}}


min_attributes = {"attoamps": 0.1, "ACTivation": 1, "EXPansion": 1, "DIFFerentiation": 1}
max_attoamps = 0.99                                     # for setting up bounds. See 12 lines below.

# quantities list | dimod is a shared API for samplers and provides classes for eg., QM's
  # inc higher-order non-quadratic models.
quantities = [dimod.Real(f"{Pt}") if Pts[Pt]["Units"] == "continuous" # an f-string. '{Pt}'
                                                        # will be replaced by a value.
    else dimod.Integer(f"{Pt}")
              for Pt in Pts.keys()]                     # key = eg cals : value = 20

print("\n(Simply showing ex of a lin bias) ")
print(quantities[0])                                    # simple linear bias
print("(Now showing an ex of a dbl bias) ")
print(2*quantities[0])                                  # Now dbl lin bias
#print(quantities[0] * quantities[1]) #Now a quadratic bias. # ValueError: REAL variables
                                                        # (e.g. 'Tfh') cannot have interactions
for ind, Pt in enumerate(Pts.keys()):
    ub = max_attoamps / Pts[Pt]["ACTivation"] # upper bnd is 20 portions, 2000/100 for Tfh below
    quantities[ind].set_upper_bound(Pt, ub)

qub = quantities[0].upper_bound("Tfh")			    # quantity ub fro Tfh
print('\nquantities[0].ub (upper bound) is: ', qub)                   # -> 20.0

# setup the OBJective Fn w a UTILity Fn                 # OBJECTIVE Fn     <<<
cqm = dimod.ConstrainedQuadraticModel()			        # NOT arbitrarily set alpha=2 beta=1;

# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
  # such as ACTivation;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (Pts[Pt][category] for Pt in Pts.keys())))
    # ZIP https://www.w3schools.com/python/ref_func_zip.asp -> ordered pairs (('',''),('','')) fr a=, b=

# Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize DIFFn, DIFFn
   # is multiplied by -1 and minimized.
cqm.set_objective(-total_mix(quantities, "DIFFerentiation") + 6 * total_mix(quantities, "Plasticity"))

# TUNING/Constraints
# Constrain the Thelp’s MAXIMUM current i.
cqm.add_constraint(total_mix(quantities, "Plasticity") <= max_attoamps, label="Plasticity") # rtn 'Plastiticty'




# Require that the nominal MINIMUM of each Th attribute is met or exceeded.
# THIS SHOULD BE USER DEFINED AS WELL.
for attribute, amount in min_attributes.items(): # Items is a BI
    cqm.add_constraint(total_mix(quantities, attribute) >= amount, label=attribute)
    'attoamps'
    'ACTivation'
    'EXPansion'
    'Expression'



# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys()) #@overld. __def__ init(self). @ is polymorph.
# list(cqm.constraints.keys())                  # ['attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation']
print('\nConstraints Dict w/ labels as keys: ', constraintsDictLabelsAsKeys)
print('ACTivation constraints (as polystr):', cqm.constraints['ACTivation'].to_polystring())
    # 100*Tfh + 140*Th9 + 90*Th2 + 150*iTreg + 270*Tr1 + 300*Th22 <= 2000, what is gvn abv
print('Attomaps constraints (as polystr):', cqm.constraints['attoamps'].to_polystring())
    # 3*Tfh + 17*Th9 + Th2 + 9*iTreg + 9*Tr1 + 4*Th22 >= 50              , what is gvn abv


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
# Make certain ur in (ocean) venv
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
    print(f"Total DIFFerentiation of {round(DIFFerentiation_total, 2)} at Plasticity {round(Plasticity_total, 2)}") # 2 dec places
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
attoamps (nominal: 50): 50
ACTivation (nominal: 30): 42
EXPansion (nominal: 130): 372
DIFFerentiation (nominal: 30): 46
>>>
The result is the same : )
'''

'''
# TUNING THE SOLUTION
	# # TUNING THE SOLUTION !
# RECALL - The objective function must maximize DIFFerentiation of the Thelp’s Pts while minimizing purchase Plasticity.
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
cqm.set_objective(-total_mix(quantities, "DIFFerentiation"))      # NOTE THE MINUS
sampleset_DIFFerentiation = sampler.sample_cqm(cqm)               # RHS SAME AS line that's 21 lines down.
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
    attoamps (nominal: 2): 0.1
    ACTivation (nominal: 6): 3
    EXPansion (nominal: 3): 2
    DIFFerentiation (nominal: 5): 2
'''



    # NOW with Plasticity:  --------------------------------------------------------------------------||
cqm.set_objective(total_mix(quantities, "Plasticity"))
sampleset_Plasticity = sampler.sample_cqm(cqm)                # RHS SAME AS line that's 21 lines up.
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
    attoamps (nominal: 2): 0.2
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

