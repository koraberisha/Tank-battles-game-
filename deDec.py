# This function removes all index's of a string after a decimal point/full stop.

def de(strin):
    try:
        tStrin = strin.split(".")
        strin = tStrin[0]
    except:
        None
        
    return strin
            
            
