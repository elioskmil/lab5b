### record_per_row()
```
def record_per_row(self):
    """
    Writes a CSV file with as many records as the size of any of the lists
    A record is a row in the file, with three columns, corresponding to
    a name, salary, and position.
    """
```
* Create 3-field records from the three attributes such that
    * a **record** has elements at the same position in the three lists.
* Format a record as a string with the three elements separated by comma
* Write each record to the **nba.txt** text file

We use the accumulation pattern with **accumulator** `nba_file`
* Iteration is over three sequences simultaneously, the class attributes
    * three loop variables `nme`, `slr`, `pos` get hold of elements in
    `self.names`, `self.salaries`, `self.positions` which have the same
    positions
    * we use `zip()` built-in function to allow for parallel processing
    * we assemble string representations of the elements including the commas
    and store in `nba_row` string local variable
    * we write `nba_row` to the file object **accumulator** `nba_file`

###names_by_pos()
```
def names_by_pos(self):
    """
    Returns a dictionary with the keys are set to the names of the positions
    and the values are set to lists of each name that is that position
    """
```
* Initializes a dictionary `sort_by_pos`, which will be returned at the end of
the method
* Uses an accumulation pattern with the **accumulator** `sort_by_pos`
* Iterates over two loop variables, `nme` and `pos` using the elements from
`self.names`, and `self.positions`, respectively
* uses an `if` statement to check if `pos` is a key in `sort_by_pos`
  * if it is, it will add `nme` to the list set as the value attached to `pos`
  * if it isn't, it will add `pos` as a key in `sort_by_pos`, and then a list
  containing `nme` as the attached values
* afterwards, the method will return `sort_by_pos`
