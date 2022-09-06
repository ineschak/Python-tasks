from sqlite3 import Row
def can_see_stage(seats):
    
   print (all(sorted(set(row)) == list(row) for row in zip(*seats)))
     



can_see_stage([[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]])
    