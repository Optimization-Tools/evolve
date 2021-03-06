"""This module contains the midpoint crossover procreator class."""
from typing import List
from numpy import ndarray
from evolve.population import Chromosome
from .procreator import Procreator

# TODO: Small probability parameter?
class MidpointCrossoverProcreator(Procreator):
    """Midpoint Crossover on parents."""

    def procreate(self, parents: List[Chromosome]) -> List[Chromosome]:
        """
        Return a list of new children generated using midpoint crossover.

        Args:
            parents: the list of parents to select genes from

        Returns: a list of new children
        """
        super(MidpointCrossoverProcreator, self).procreate(parents)
        return [parents[0].copy(genes=(parents[0].genes + parents[1].genes) / 2)]


# explicitly specify exports
__all__ = [
    'MidpointCrossoverProcreator'
]
