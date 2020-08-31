from IPython.core.magic import Magics, magics_class, line_cell_magic

@magics_class
class Nbbranch(Magics):

    def __init__(self, shell):
        super().__init__(shell)
        self.conditions = []

    def execute(self):
        conditions = [False if v is None else v for v in self.conditions]
        return all(conditions)

    @line_cell_magic
    def IF(self, line, cell=None):
        if line:
            self.conditions.append(self.shell.ev(line.rstrip(':')))
        if self.execute() and cell:
            self.shell.ex(cell)

    @line_cell_magic
    def ELSE(self, line, cell=None):
        assert self.conditions
        if self.conditions[-1] is None:
            # one of the previous branches was already taken
            self.conditions[-1] = False
        else:
            self.conditions[-1] = not self.conditions[-1]
        if self.execute() and cell:
            self.shell.ex(cell)

    @line_cell_magic
    def ELIF(self, line, cell=None):
        assert self.conditions
        if self.conditions[-1] is None:
            # one of the previous branches was already taken
            pass
        elif self.conditions[-1]:
            # previous branch was taken, all following ones must be ignored
            self.conditions[-1] = None
        else:
            self.conditions[-1] = self.shell.ev(line.rstrip(':'))
        if self.execute() and cell:
            self.shell.ex(cell)

    @line_cell_magic
    def ENDIF(self, line, cell=None):
        assert self.conditions
        self.conditions.pop()
        if cell:
            self.shell.ex(cell)
