from numbers import Number
from typing import Sequence, Iterator, Generator

from .matrix_dimensions import MatrixDimensions


MatrixLikeSequence = Sequence[Sequence[Number]]

# structure:
# constructor + other magic/dunder methods
# operation methods
# classmethods
# properties
# "public" methods
# "private" methods
class Matrix:
    def __init__(self, matrix: MatrixLikeSequence):
        self._matrix = matrix
        self._dimensions = MatrixDimensions(
            len(self._matrix),
            0 if isinstance(self._matrix[0], Number) else len(self._matrix[0])
        )

        if not self._validate_matrix():
            raise ValueError('This matrix is invalid! Check if all of it\'s rows have the same number of elements.')

    def __add__(self, other: 'Matrix') -> 'Matrix':
        self._is_valid_for_operations(other)
        return self.__class__.from_generator(
            [svalue + ovalue for svalue, ovalue in zip(srow, orow)]
            for srow, orow in zip(self._matrix, other._matrix)
        )

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        self._is_valid_for_operations(other)
        return -self + other

    def __mul__(self, scalar: Number) -> 'Matrix':
        if not isinstance(scalar, Number):
            raise TypeError('As of now, you can only multiply a matrix by a number.')

        return self.__class__.from_generator(
            [value * scalar for value in row]
            for row in self._matrix
        )

    def __neg__(self) -> 'Matrix':
        return self * -1

    def __eq__(self, other: 'Matrix') -> bool:
        self._is_valid_for_operations(other)
        return all(
            n1 == n2
            for n1, n2 in zip(self, other)
        )

    def __ne__(self, other: 'Matrix') -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({str(self._matrix)})'

    def __str__(self, padding: int=2, padding_after_first_row: int=0) -> str:
        max_length = max(len(str(n)) for n in self)
        general_padding = max_length + padding

        def get_padding(i, j):
            p1 = general_padding if j > 0 else 0
            p2 = padding_after_first_row if i > 0 and j == 0 else 0
            return p1 + p2

        return '\n'.join(
            ''.join(
                f'{value:>{get_padding(row_index, column_index)}}'
                for column_index, value in enumerate(row)
            )
            for row_index, row in enumerate(self._matrix)
        )

    def __iter__(self) -> Iterator[Number]:
        return (
            value
            for row in self._matrix
            for value in row
        )

    def transpose(self) -> 'Matrix':
        t = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i, row in enumerate(self._matrix):
            for j, value in enumerate(row):
                t[j][i] = value

        return self.__class__(t)

    @classmethod
    def from_rows(cls, *rows: MatrixLikeSequence) -> 'Matrix':
        return cls(rows)

    @classmethod
    def from_columns(cls, *columns: MatrixLikeSequence) -> 'Matrix':
        return cls(columns).transpose()

    @classmethod
    def from_generator(cls, generator: Generator) -> 'Matrix':
        return cls(tuple(generator))

    @property
    def dimensions(self) -> MatrixDimensions:
        return self._dimensions

    @property
    def m(self) -> int:
        return self.dimensions.m

    @property
    def n(self) -> int:
        return self.dimensions.n

    @property
    def is_null(self) -> bool:
        return all(n == 0 for n in self)

    @property
    def is_square(self) -> bool:
        return self.m == self.n

    def get_column(self, column_index: int) -> 'Matrix': ## temp: returns matrix
        return self.__class__.from_generator(row[column_index] for row in self._matrix)

    def compare_dimensions(self, other: 'Matrix') -> bool:
        return self.dimensions == other.dimensions

    def _validate_matrix(self) -> bool:
        return all(len(row) == self.n for row in self._matrix)

    def _is_valid_for_operations(self, v: 'Matrix') -> bool:
        if not isinstance(v, self.__class__):
            type_name = v.__class__.__name__
            raise TypeError(f'This operation is only allowed between matrices! {type_name} isn\'t a matrix!')

        if not self.compare_dimensions(v):
            raise ValueError(f'This operation is only allowed between matrices of equal dimensions! {self.dimensions} != {v.dimensions}.')
