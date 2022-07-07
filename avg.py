# This function returns an average given a list of numbers.

def averageList(listo):
    enum = 0
    
    for i in listo:
        enum += i
    avg = enum/len(listo)
    return avg
        
