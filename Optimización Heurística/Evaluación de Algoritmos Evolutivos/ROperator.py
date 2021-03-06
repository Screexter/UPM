from Genome import Genome
from Population import Population
from ReplacementOperator import ReplacementOperator


class ROperator(ReplacementOperator):

    def __init__(self, population_list):
        self.population_list = population_list

    def apply(self, target_vector, trial_vector, population_list):
        if target_vector.get_score() >= trial_vector.get_score():
            population_list.replace_genome(target_vector, trial_vector)
        return population_list
