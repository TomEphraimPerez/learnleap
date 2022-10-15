                        # DIET PLANNING  optimization -
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
# Python 3.9.2
print('\nHello quantum world.')
print('\nThis is the diet optimization prob w taste v cost goal, gvn several ')
print('constraints.')

# Pt dict of "food". MACROnutriens are cals, Pts, fat(s), carbs...
                    #   MICROnutirnet are vitamins and minerals, C, D, iron...
foods = {'rice': {'Calories': 100, 'Protein': 3, 'Fat': 1, 'Carbs': 22,
                    'Fiber': 2, 'Taste': 7, 'Cost': 2.5, 'Units': 'continuous'},
        'tofu': {'Calories': 140, 'Protein': 17, 'Fat': 9, 'Carbs': 3,
                    'Fiber': 2, 'Taste': 2, 'Cost': 4.0, 'Units': 'continuous'},
        'banana': {'Calories': 90, 'Protein': 1, 'Fat': 0, 'Carbs': 23, 'Fiber': 3,
                    'Taste': 10, 'Cost': 1.0, 'Units': 'discrete'},
        'lentils': {'Calories': 150, 'Protein': 9, 'Fat': 0, 'Carbs': 25, 'Fiber': 4,
                    'Taste': 3, 'Cost': 1.3, 'Units': 'continuous'},
        'bread': {'Calories': 270, 'Protein': 9, 'Fat': 3, 'Carbs': 50, 'Fiber': 3,
                    'Taste': 5, 'Cost': 0.25, 'Units': 'continuous'},
        'avocado': {'Calories': 300, 'Protein': 4, 'Fat': 30, 'Carbs': 20, 'Fiber': 14,
                    'Taste': 5, 'Cost': 2.0, 'Units': 'discrete'}}

min_nutrients = {"Protein": 50, "Fat": 30, "Carbs": 130, "Fiber": 30}
max_calories = 2000                                     # for setting up bounds. See 12 lines below.

# quantities list | dimod is a shared API for samplers and provides classes for eg., QM's
  # inc higher-order non-quadratic models.
quantities = [dimod.Real(f"{food}") if foods[food]["Units"] == "continuous" # an f-string. '{food}'
                                                        # will be replaced by a value.
    else dimod.Integer(f"{food}")
    for food in foods.keys()]                           # key = eg cals : value = 20

print("\nSimply showing ex of a lin bias. ")
print(quantities[0])                # simple linear bias
print("Now showing an ex of a dbl bias. ")
print(2*quantities[0])              # Now dbl lin bias
#print(quantities[0] * quantities[1]) #Now a quadratic bias. # ValueError: REAL variables
                                                        # (e.g. 'rice') cannot have interactions
for ind, food in enumerate(foods.keys()):
    ub = max_calories / foods[food]["Calories"]         # upper bnd is 20 portions, 2000/100 for rice below
    quantities[ind].set_upper_bound(food, ub)

qub = quantities[0].upper_bound("rice")			        # quantity ub fro rice
print('\nquantities[0].ub is: ', qub)                   # -> 20.0

# setup the OBJective Fn w a UTILity Fn                 # OBJECTIVE Fn     <<<
cqm = dimod.ConstrainedQuadraticModel()			        # NOT arbitrarily set alpha=2 beta=1;

# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
  # such as calories;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (foods[food][category] for food in foods.keys()) ) )
    # ZIP https://www.w3schools.com/python/ref_func_zip.asp -> ordered pairs (('',''),('','')) fr a=, b=

# Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize taste, Taste
   # is multiplied by -1 and minimized.
cqm.set_objective(-total_mix(quantities, "Taste") + 6 * total_mix(quantities, "Cost"))

# TUNING/Constraints
# Constrain the diet’s   MAXIMUM cal intake required daily.
cqm.add_constraint(total_mix(quantities, "Calories") <= max_calories, label="Calories") # rtn 'Calories'

# Require that the daily MINIMUM of each nutrient is met or exceeded.
for nutrient, amount in min_nutrients.items():          # Items is a BI
    cqm.add_constraint(total_mix(quantities, nutrient) >= amount, label=nutrient)
'Protein'
'Carbs'
'Fat'
'Fiber'

# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys()) #@overld. __def__ init(self). @ is polymorph.
# list(cqm.constraints.keys())        #o # ['Calories', 'Protein', 'Fat', 'Carbs', 'Fiber']
print('\nConstraints Dict w/ labels as keys: ', constraintsDictLabelsAsKeys)
print('Cal constraints (as polystr):', cqm.constraints['Calories'].to_polystring())
    # 100*rice + 140*tofu + 90*banana + 150*lentils + 270*bread + 300*avocado <= 2000, what is gvn abv
print('Pt constraints (as polystr):', cqm.constraints['Protein'].to_polystring())
    # 3*rice + 17*tofu + banana + 9*lentils + 9*bread + 4*avocado >= 50              , what is gvn abv

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
    diet = {food: round(quantity, 1) for food, quantity in sample.items()} # 'food:' has 1 dec place?
    print(f"Diet----->: {diet}")
    taste_total = sum(foods[food]["Taste"] * amount for food, amount in sample.items())
    cost_total =  sum(foods[food]["Cost"]  * amount for food, amount in sample.items())
    print(f"Total taste of {round(taste_total, 2)} at cost {round(cost_total, 2)}") # 2 dec places?
    for constraint in cqm.iter_constraint_data(sample):
        print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")
                                                        # rhs_energy is a dimod float attribute
# The best solution found in this current execution was a diet of bread and bananas, with
# avocado completing the required fiber and fat portions
best = feasible_sampleset.first.sample
print('\nprint_DIET(BEST): ')
print_diet(best)
''' >>>  a la:
Diet: {'avocado': 1.0, 'banana': 6.0, 'bread': 4.1, 'lentils': 0.3, 'rice': 0.0, 'tofu': 0.0}
Total taste of 86.56 at cost 9.46
Calories (nominal: 2000): 2000
Protein (nominal: 50): 50
Fat (nominal: 30): 42
Carbs (nominal: 130): 372
Fiber (nominal: 30): 46
>>>
The result is the same : )
'''

'''
# TUNING THE SOLUTION
	# TUNING THE SOLUTION !
# RECALL - The objective function must maximize taste of the diet’s Pt while minimizing purchase cost.
	# So re min cost, COST_min  = min SUMMA_i (qty_i * cost_i)
	#	             TASTE_max  = max SUMMA_i (qty_i * taste_i)

	# To optimize two different objectives, TASTE and COST, requires weighing ONE AGAINST the other.

 	# A simple way to do this, is to set priority weights; for example,
        #	OBJective = alpha(obj_1) + beta(obj_1). eg alpha can = 2, beta can = 1,
	    #	ie you double the priority of the first objective compared to the second.
'''



#Consider sampling each part of the combined objective ON ITS OWN (alpha=0, beta=1 and vv)
	# and comparing the best solutions. 
	# Start with TASTE: -----------------------------------------------------------------------||
cqm.set_objective(-total_mix(quantities, "Taste"))      # NOTE THE MINUS
sampleset_taste = sampler.sample_cqm(cqm)               # RHS SAME AS line that's 21 lines down.
feasible_sampleset_taste = sampleset_taste.filter(lambda row: row.is_feasible)
best_taste = feasible_sampleset_taste.first
print('best_taste.ENERGY: ', round(best_taste.energy))
# >>> a la -177

print('\nbest_taste.SAMPLE: ')
print_diet(best_taste.sample)
# >>> a la;
'''
 Diet: {'avocado': 0.0, 'banana': 17.0, 'bread': 0.0, 'lentils': 0.0, 'rice': 0.0, 'tofu': 3.3}
 Total taste of 176.93 at cost 30.41
 Calories (nominal: 2000): 2000
 Protein (nominal: 50): 74
 Fat (nominal: 30): 30
 Carbs (nominal: 130): 402
 Fiber (nominal: 30): 58
'''



    # NOW with COST:  --------------------------------------------------------------------------||
cqm.set_objective(total_mix(quantities, "Cost"))
sampleset_cost = sampler.sample_cqm(cqm)                    # RHS SAME AS line that's 21 lines up.
feasible_sampleset_cost = sampleset_cost.filter(lambda row: row.is_feasible)
best_cost = feasible_sampleset_cost.first
print(round(best_cost.energy))
	# >>> 3

print('\nbest_cost.SAMPLE: ')
print_diet(best_cost.sample)
'''>>> a la
  Diet: {'avocado': 1.0, 'banana': 0.0, 'bread': 5.3, 'lentils': 0.0, 'rice': 0.0, 'tofu': 0.0}
  Total taste of 31.67 at cost 3.33
  Calories (nominal: 2000): 1740
  Protein (nominal: 50): 52
  Fat (nominal: 30): 46
  Carbs (nominal: 130): 287
  Fiber (nominal: 30): 30
'''
'''
This diet is ranked as less tasty than the previous but much cheaper. 
It relies mainly on bread and uses avocado to add fat and fiber.
'''
'''
Because of the differences in energy scale between the two parts of the combined objective,
177 >> 3,  if you do not multiply the part representing cost by some positive factor, optimal 
solutions will maximize taste and neglect cost. That is, if in 
obj - alpha(obj1 + beta(obj2)), you set alpha=1=beta.
solutions will likely be 
  close or 
  identical 
to those found when optimizing for taste alone.
'''

''' SEE GRAPH with y-axis=Energy, x-axis=Multiplier, variables are taste, cost and total. 
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals
https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals
'''

'''
 ††† (Recall; Set the objective2. Because Ocean solvers minimize objectives, to maximize taste, Taste is 
          multiplied by -1 and minimized.)
'''

