from figure import Figure


class Queen(Figure):
    @property
    def char(self) -> str:
        return 'wQ' if self.color.is_white() else 'bQ'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        if from_row == to_row and from_col == to_col:
            return False  # Попытка остаться на месте

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Проверка: ход по прямой (горизонталь/вертикаль) или диагонали
        straight = row_diff == 0 or col_diff == 0
        diagonal = row_diff == col_diff
        if not (straight or diagonal):
            return False

        # Определение направления движения
        row_step = 0
        if to_row > from_row:
            row_step = 1
        elif to_row < from_row:
            row_step = -1

        col_step = 0
        if to_col > from_col:
            col_step = 1
        elif to_col < from_col:
            col_step = -1

        # Проверка промежуточных клеток
        row, col = from_row + row_step, from_col + col_step
        while (row, col) != (to_row, to_col):
            if board.get_item(row, col) is not None:
                return False  # Препятствие на пути
            row += row_step
            col += col_step

        return True