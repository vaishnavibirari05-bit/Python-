#quetions:-
'''
print(not (True) and 31 > 34 or not (32 > 21 and (True)) and not(True or 561-0))
print(not(0-0) and 34 > 34 or not (32 > 21 and not (False)) and not (False or 010))
print(("Ram" "ram") and (8> 0) and 341 34 or not (32 > 21 and not(True)) and not (True or 56 10))
print(not (False) and 341 34 or not(int("32") >= 21 and not (True)) and not (True or 8.1 10))
print(not(False) and 34 <e or not (32 >= 21 and not( Sahil Sahil)) and not (True or 56 1-8))
'''


# Line 1 (already valid)
print(not True and 31 > 34 or not (32 > 21 and True) and not (True or 561-0))

# Line 2 (fixed 010 → 10)
print(not(0) and 34 > 34 or not (32 > 21 and not False) and not (False or 10))

# Line 3 (added missing operators)
print(("Ram" "ram") and (8 > 0) and (341 > 34) or not (32 > 21 and not True) and not (True or 56 - 10))

# Line 4 (added missing operators)
print(not False and (341 > 34) or not (int("32") >= 21 and not True) and not (True or 8.1 < 10))

# Line 5 (fixed invalid identifiers and operators)
print(not False and (34 < 50) or not (32 >= 21 and not ("Sahil" == "Sahil")) and not (True or 56 + (1-8)))
