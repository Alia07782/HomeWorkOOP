from figure import Figure


class King(Figure):
    @property
    def char(self) -> str:
        return 'wKg' if self.color.is_white() else 'bKg'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        return (row_diff <= 1 and col_diff <= 1) and (row_diff != 0 or col_diff != 0)