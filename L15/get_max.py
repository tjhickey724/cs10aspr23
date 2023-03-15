def get_max(vals):
    ''' returns the largest value in the list vals of numbers '''
    max_so_far = vals[0]
    for val in vals:
        if val > max_so_far:
            max_so_far = val
    return max_so_far

def get_max2(vals):
    vals.sort()
    return vals[-1]

