# SimpleDB

SimpleDB is a simple database similar to redis. The default underlying 
data structure is a hashtable ala python dictionary. 

There is an option to use a Red-black tree as the datastructure.

## Usage
Default usage with hash table:

    simpledb

Optional usage with red-black tree:

    simpledb use_rb_tree

Input `help` to see available commands and examples:

    > HELP

## Supported operations

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

## Implementation details

There are three main layers. The interface layer, the SimpleDB layer and the
data structure layer.

### 1. Interface layer: `simple_db/simple_db_interface.py`

This where the input from user is parsed, cleaned up and routed to the appropriate
function im SimpleDB.

### 2. SimpleDB layer: `simple_db/simple_db.py`

SimpleDB was created with the ability to easily swap different data structures to
be used. There is a `simple_db_protocol.py` file that potential data structures
should adhere to in order for SimpleDB to interface with them.

### 3. Data structure layer: `simple_db/data_structures`

Currently there is a hash table implementation and a red-black tree one.
These data structures are the backbone of operations for SimpleDB and offer at least
the basic functions of search, insert and delete.

## Some design details

### Hash table vs red-black tree

By default a hash table is used, but strictly speaking, search, insert and delete
in a hash table can be O(n) in the worst case. So I decided to optionally add
an implemention with a red-black tree because they are guaranteed to be O(log(n)) 
in the worst case for search, insert and delete.

### numequalto

I simply used a python dictionary here with default values set as 0. 
I mapped every value to an occurence count. Pretty straight forward implementation 
and maximizes for time.The same logic as above could apply here and a red-black tree 
would work as well, but to keep it simple I kept it as a dictionary. 

### Transactions

The transaction interactions were really interesting and engaging to build. At first I
thought about cloning the entire DB and keeping the state before every new transaction.
I realized that was way too space inefficient.

Next, I thought about storing commands as they were inputted and then a rollback would
do the opposite of the command if the command affected the state of the DB.
i.e. Opposite of SET is UNSET and vice versa. I used nested stacks for this implementation 
but soon hit a roadblock.

My final implementation is a culmination of the two ideas above. I want to only store the previous state
of changed variables instead of the entire DB. So I have a stack of dictionaries
and each dictionary represented the previous state of variables that were changed.
On rollback, the previous state would be restored. This implementation got past the 
roadblock and was quite space efficient as well as time efficient.