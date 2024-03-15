The functuon reads a .txt file to decode a hidden message by using sorting and creating a pyramid shape from tuples (index, word) 
and selects word appearing in the far end edge of the pyramid shape to select witch words to use for the decryption. e.g.:

if the .txt file contains:

        14 henry
        5 yes
        13 lisa
        6 name
        4 over
        10 is
        7 when
        11 fred
        2 what
        9 rocket
        1 hi
        15 bob
        8 no
        3 my
        12 ted

it will arrange the words like this:

                hi
              what my
            over yes name
          when no rocket is
        fred ted lisa henry bob 

and print the message "hi my name is bob" as a final result.
