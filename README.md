# SimpleDB
===================

SimpleDB is a simple database similar to redis. The underlying data structure
is a python dictionary

## Supported operations:

### Data Commands

    - SET [name] [value]: Set the variable [name] to the value [value].

    - GET [name]: Print out the value of the variable [name]. 
                  NULL if that variable is not set.

    - UNSET [name]: Unset the variable [name],
                    making it just like that variable was never set.

    - NUMEQUALTO [value]: Print out the number of variables that are currently
                          set to [value]. 
                          If no variables equal that [value], prints 0.

    - END: Exit the program.

### Transaction Commands

    - BEGIN: Open a new transaction block. 
             Transaction blocks can be nested;
             a BEGIN can be issued inside of an existing block.

    - ROLLBACK: Undo all of the commands issued in the most 
                recent transaction block, and close the block. 

    - COMMIT: Close all open transaction blocks, 
              permanently applying the changes made in them. 
