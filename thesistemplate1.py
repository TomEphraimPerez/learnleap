                        # ILs RECEPTORS AFFECT CURRNT FLOW TO THEIR RESPECTIVE IL-Cs  optimization -

# A CQM solver prob on a simple mixed-integer linear-programming, MILP, type of optimization problem.
 # https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals ††
# imports
import dimod as dimod       # thx red lightbulb
from dwave.system import LeapHybridCQMSampler         #o
 # solver is an option. [See the solve-by sampling section toward the end ††]
  # For charges - $$$
    # Select a solver
    # sampler = LeapHybridSampler()

    # Submit for solution
    # answer = sampler.sample_qubo(Q)

# Python 3.9.2

print('\nThis is the diet optimization prob w Expression v Plasticity goal, gvn several ')
print('constraints.')

# Pt dict of "Robustness".

# attoamps -> picoamp = 10^-12a, femtoamps =10^-15a, attoamps = 10^-18a.
Pt = {'IL-4C': {'Calories': 100, 'attoamps': 3, 'ACTivation': 1, 'EXPansion': 22,
                    'DIFFerentiation': 2, 'Expression': 7, 'Plasticity': 2.5, 'Units': 'continuous'},
        'IL-2C': {'Calories': 140, 'attoamps': 17, 'ACTivation': 9, 'EXPansion': 3,
                    'DIFFerentiation': 2, 'Expression': 2, 'Plasticity': 4.0, 'Units': 'continuous'},
        'IFNγC': {'Calories': 90, 'attoamps': 1, 'ACTivation': 0, 'EXPansion': 23, 'DIFFerentiation': 3,
                    'Expression': 10, 'Plasticity': 1.0, 'Units': 'discrete'},
        'TGFβC': {'Calories': 150, 'attoamps': 9, 'ACTivation': 0, 'EXPansion': 25, 'DIFFerentiation': 4,
                    'Expression': 3, 'Plasticity': 1.3, 'Units': 'continuous'},
        'TNF𝛼C': {'Calories': 270, 'attoamps': 9, 'ACTivation': 3, 'EXPansion': 50, 'DIFFerentiation': 3,
                    'Expression': 5, 'Plasticity': 0.25, 'Units': 'continuous'},
        'IL-6C': {'Calories': 300, 'attoamps': 4, 'ACTivation': 30, 'EXPansion': 20, 'DIFFerentiation': 14,
                    'Expression': 5, 'Plasticity': 2.0, 'Units': 'discrete'}}


min_nutrients = {"attoamps": 50, "ACTivation": 30, "EXPansion": 130, "DIFFerentiation": 30}
max_calories = 2000                                     # for setting up bounds. See 12 lines below.

# quantities list | dimod is a shared API for samplers and provides classes for eg., QM's
  # inc higher-order non-quadratic models.
quantities = [dimod.Real(f"{Robustness}") if Pt[Robustness]["Units"] == "continuous" # an f-string. '{Robustness}'
                                                        # will be replaced by a value.
    else dimod.Integer(f"{Robustness}")
              for Robustness in Pt.keys()]                    # key = eg cals : value = 20

print("\nSimply showing ex of a lin bias. ")
print(quantities[0])                                    # simple linear bias
print("Now showing an ex of a dbl bias. ")
print(2*quantities[0])                                  # Now dbl lin bias
#print(quantities[0] * quantities[1]) #Now a quadratic bias. # ValueError: REAL variables
                                                            # (e.g. 'IL-4C') cannot have interactions
for ind, Robustness in enumerate(Pt.keys()):
    ub = max_calories / Pt[Robustness]["Calories"] # upper bnd is 20 portions, 2000/100 for IL-4C below
    quantities[ind].set_upper_bound(Robustness, ub)

qub = quantities[0].upper_bound("IL-4C")			    # quantity ub fro IL-4C
print('\nquantities[0].ub is: ', qub)                   # -> 20.0

# setup the OBJective Fn w a UTILity Fn                 # OBJECTIVE Fn     <<<
cqm = dimod.ConstrainedQuadraticModel()			        # NOT arbitrarily set alpha=2 beta=1;

# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
  # such as calories;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (Pt[Robustness][category] for Robustness in Pt.keys())))
    # ZIP https://www.w3schools.com/python/ref_func_zip.asp -> ordered pairs (('',''),('','')) fr a=, b=

# Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize Expression, Expression
   # is multiplied by -1 and minimized.
cqm.set_objective(-total_mix(quantities, "Expression") + 6 * total_mix(quantities, "Plasticity"))

# TUNING/Constraints
# Constrain the diet’s   MAXIMUM cal intake required daily.
cqm.add_constraint(total_mix(quantities, "Calories") <= max_calories, label="Calories") # rtn 'Calories'

# Require that the daily MINIMUM of each nutrient is met or exceeded.
for nutrient, amount in min_nutrients.items():          # Items is a BI
    cqm.add_constraint(total_mix(quantities, nutrient) >= amount, label=nutrient)

# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys()) #@overld. __def__ init(self). @ is polymorph.
# list(cqm.constraints.keys())        #o # ['Calories', 'attoamps', 'ACTivation', 'EXPansion', 'DIFFerentiation']
print('\nConstraints Dict w/ labels as keys: ', constraintsDictLabelsAsKeys)
print('Cal constraints (as polystr):', cqm.constraints['Calories'].to_polystring())
    # 100*IL-4C + 140*IL-2C + 90*IFNγC + 150*TGFβC + 270*TNF𝛼C + 300*IL-6C <= 2000, what is gvn abv
print('Pt constraints (as polystr):', cqm.constraints['attoamps'].to_polystring())
    # 3*IL-4C + 17*IL-2C + IFNγC + 9*TGFβC + 9*TNF𝛼C + 4*IL-6C >= 50              , what is gvn abv


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
def print_diet(sample):
    diet = {Robustness: round(quantity, 1) for Robustness, quantity in sample.items()} # 'Robustness:' has 1 dec place?
    print(f"Diet----->: {diet}")
    taste_total = sum(Pt[Robustness]["Expression"] * amount for Robustness, amount in sample.items())
    cost_total =  sum(Pt[Robustness]["Plasticity"] * amount for Robustness, amount in sample.items())
    print(f"Total Expression of {round(taste_total, 2)} at Plasticity {round(cost_total, 2)}") # 2 dec places?
    for constraint in cqm.iter_constraint_data(sample):
        print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")
                                                        # rhs_energy is a dimod float attribute
# The best solution found in this current execution was a diet of TNF𝛼C and bananas, with
# IL-6C completing the required DIFFerentiation and ACTivation portions
best = feasible_sampleset.first.sample
print('\nprint_DIET(BEST): ')
print_diet(best)
''' >>>  a la:
Diet: {'IL-6C': 1.0, 'IFNγC': 6.0, 'TNF𝛼C': 4.1, 'TGFβC': 0.3, 'IL-4C': 0.0, 'IL-2C': 0.0}
Total Expression of 86.56 at Plasticity 9.46
Calories (nominal: 2000): 2000
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
# RECALL - The objective function must maximize Expression of the diet’s Pt while minimizing purchase Plasticity.
	# So re min Plasticity, COST_min  = min SUMMA_i (qty_i * cost_i)
	#	            TASTE_max  = max SUMMA_i (qty_i * taste_i)
	
	# To optimize two different objectives, Expression and Plasticity, requires weighing one AGAINST the other.
	 
 	# A simple way to do this, is to set priority weights; for example,
        #	OBJective = alpha(obj_1) + beta(obj_1). eg alpha can = 2, beta can = 1,
	    #	ie you double the priority of the first objective compared to the second.
'''



#Consider sampling each part of the combined objective ON ITS OWN (alpha=0, beta=1 and vv)
	# and comparing the best solutions.
	# Start with Expression: -----------------------------------------------------------------------||
cqm.set_objective(-total_mix(quantities, "Expression"))      # NOTE THE MINUS
sampleset_taste = sampler.sample_cqm(cqm)               # RHS SAME AS line that's 21 lines down.
feasible_sampleset_taste = sampleset_taste.filter(lambda row: row.is_feasible)
best_taste = feasible_sampleset_taste.first
print('best_taste.ENERGY: ', round(best_taste.energy))
# >>> a la -177

print('\nbest_taste.SAMPLE: ')
print_diet(best_taste.sample)
# >>> a la;
'''
 Diet: {'IL-6C': 0.0, 'IFNγC': 17.0, 'TNF𝛼C': 0.0, 'TGFβC': 0.0, 'IL-4C': 0.0, 'IL-2C': 3.3}
 Total Expression of 176.93 at Plasticity 30.41
 Calories (nominal: 2000): 2000
 attoamps (nominal: 50): 74
 ACTivation (nominal: 30): 30
 EXPansion (nominal: 130): 402
 DIFFerentiation (nominal: 30): 58
'''



    # NOW with Plasticity:  --------------------------------------------------------------------------||
cqm.set_objective(total_mix(quantities, "Plasticity"))
sampleset_cost = sampler.sample_cqm(cqm)                # RHS SAME AS line that's 21 lines up.
feasible_sampleset_cost = sampleset_cost.filter(lambda row: row.is_feasible)
best_cost = feasible_sampleset_cost.first
print(round(best_cost.energy))
	# >>> 3

print('\nbest_cost.SAMPLE: ')
print_diet(best_cost.sample)
'''>>> a la
  Diet: {'IL-6C': 1.0, 'IFNγC': 0.0, 'TNF𝛼C': 5.3, 'TGFβC': 0.0, 'IL-4C': 0.0, 'IL-2C': 0.0}
  Total Expression of 31.67 at Plasticity 3.33
  Calories (nominal: 2000): 1740
  attoamps (nominal: 50): 52
  ACTivation (nominal: 30): 46
  EXPansion (nominal: 130): 287
  DIFFerentiation (nominal: 30): 30
'''
'''
This diet is ranked as less tasty than the previous but much cheaper. 
It relies mainly on TNF𝛼C and uses IL-6C to add ACTivation and DIFFerentiation.
'''
'''
Because of the differences in energy scale between the two parts of the combined objective,
177 >> 3,  if you do not multiply the part representing Plasticity by some positive factor, optimal 
solutions will maximize Expression and neglect Plasticity. That is, if in 
obj - alpha(obj1 + beta(obj2)), you set alpha=1=beta.
solutions will likely be 
  close or 
  identical 
to those found when optimizing for Expression alone.
'''

''' SEE GRAPH with y-axis=Energy, x-axis=Multiplier, variables are Expression, Plasticity and total. 
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals
'''

'''
 ††† (Recall; Set the objective2. Because Ocean solvers minimize objectives, to maximize Expression, Expression is 
          multiplied by -1 and minimized.)
'''
