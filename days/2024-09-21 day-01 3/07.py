def dec_to_base(dec, base=2):
    b = ''
    while dec > 0:
        mod = dec % base
        dec = dec // base
        b = str(mod) + b 
    return b
    

print( dec_to_base(20, 3) )
# A B C D E F 
