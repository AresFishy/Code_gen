from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# modelus definus
# C: Contestant choice 
# H: Host choice
# P: Prize location
model = BayesianModel([('C', 'H'), ('P', 'H')])

cpd_c = TabularCPD('C', 3,[[0.33, 0.33, 0.33]])
cpd_p = TabularCPD('P', 3,[[0.33, 0.33, 0.33]])
cpd_h = TabularCPD('H', 3,[
    [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
    [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
    [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]],
    evidence=['C', 'P'], evidence_card=[3, 3]
)

model.add_cpds(cpd_c, cpd_p, cpd_h)
model.get_cpds()

