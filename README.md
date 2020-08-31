# nbbranch: branching in the Jupyter Notebook

## What if you could branch over multiple cells?

You would argue, just merge the cells and use the built-in `if`/`elif`/`else` statements. Except that a cell can have an output (some text, an image, or a widget), and so by branching over multiple cells you can generate several outputs conditionally. In the context of [Voila](https://github.com/voila-dashboards/voila), this means you can e.g. have a dynamically generated dashboard.

## What does it look like?

`nbbranch` is implemented as IPython magic commands.

```python
%load_ext nbbranch

a = 1

#

%%IF a == 0:
print('foo')

# no output

%%ELIF a == 1:
print('bar1')

# prints "bar1"

%%IF True:
print('True')

# prints "True"

%ENDIF

#

%%IF
print('bar2')

# prints "bar2"

%%ELIF a == 2:
print('baz')

# no output

%%ELSE
print('ERROR')

# no output

%ENDIF
```

A few remarks:
- We use upper-case equivalents of built-in Python branching keywords (`IF`, `ELIF`, `ELSE`).
- These keywords must be prefixed with `%` if the reminder of the cell is empty, or `%%` otherwise (general magic syntax).
- Indentation is not required (this may change in the future).
- We need an `%ENDIF` to mark the end of a corresponding `%IF`.
- Between the outer-most `%IF`/`%ENDIF`, all cells must start with one of `%IF`, `%ELIF` or `%ELSE`. If the cell is just the continuation of the cell above, its first line must be an empty `%%IF`.
