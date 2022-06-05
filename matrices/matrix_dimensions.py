from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from matrix import Matrix


class MatrixDimensions:
    def __init__(self, m: int, n: int):
        self._m = m
        self._n = n

    @property
    def m(self) -> int:
        return self._m

    @property
    def n(self) -> int:
        return self._n

    @property
    def as_tuple(self) -> tuple[int]:
        return self.m, self.n

    @classmethod
    def from_tuple(cls, dimensions) -> 'MatrixDimensions':
        return cls(*dimensions)

    def __repr__(self) -> str:
        return f'MatrixDimensions({self.m}, {self.n})'

    def __str__(self) -> str:
        return f'{self.m}x{self.n}'
    
    def __eq__(self, other: 'Matrix') -> bool:
        if not isinstance(other, self.__class__):
            cls_name = self.__class__.__name__
            raise TypeError(f'{cls_name} can only be compared to other {cls_name}!')
        
        return self.m == other.m and self.n == other.n

    def __ne__(self, other: 'Matrix') -> bool:
        return not self.__eq__(other)
