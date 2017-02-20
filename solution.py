import traceback
import logging

assignments = []


rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    i=0
    sudoku=dict()
    
    for value in grid:
        if value == ".":
            value = '123456789'
        sudoku[boxes[i]]=value
        #assign_value(sudoku, boxes[i], value)
        i=i+1
        
    return sudoku

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    for box,value in values.items():
        if ( len ( value ) == 1 ):
            for peer in peers[ box ]:
                new_peer_value=''
                for possible_peer_value in values[peer]:
                    if ( possible_peer_value != value ):
                        new_peer_value=new_peer_value+possible_peer_value
                #values[peer]=new_peer_value
                assign_value(values, peer, new_peer_value)
    
    return values   

def only_choice(values):
    for unit in unitlist:
        #print ("boxes : ",unit)
        #print ( "values of unit :",[values[box] for box in unit] )
        for i in range(1,10):
            #print ( "testing ",i)
            i=str(i)
            possible_positions=0
            for box in unit:
                if ( i in values[box] ):
                    #print (i,values[box])
                    possible_positions=possible_positions+1
                    matched_box=box
            #print (i,possible_positions)
            if ( possible_positions == 1 ):
                #print ("only possible position for ",i," is ",matched_box)
                #values[matched_box]=i
                assign_value(values, matched_box, i)
            
        
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values=eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values=only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values=reduce_puzzle(values)
    #print ("new values", values)
    if values is False:
        return False
        
    # Choose one of the unfilled squares with the fewest possibilities
    smallest_box_size=9
    smallest_box='solved!'
    for box,value in values.items():
        #print ("box value", box, value)
        if ( (len(value) <= smallest_box_size) and ( len(value) > 1 ) ):
            smallest_box=box
            smallest_box_size=len(value)
            
    if ( smallest_box == 'solved!' ):
        print('It  is solved!')
        #width = 1+max(len(values[s]) for s in boxes)
        #print ("width",width)
        #print (values)
        #display(values)
        #values
        return values
    
        # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for possible_value in values[smallest_box]:
        new_values=values.copy()
        #new_values[smallest_box]=possible_value
        assign_value(new_values, smallest_box, possible_value)
        attempt=search(new_values)
        #make it stop the for loop it is has found a solution
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except Exception as e:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
        logging.error(traceback.format_exc())
