#Irene Font Peradejordi, if76
#Sachi Angle, sva22

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    # TODO: YOUR CODE HERE
    s = "-" + s
    t = "-" + t
    
    if i == 0 and j == 0:
        return DiffingCell(".", ".", 0)
    
    if i == 0:
        c = table.get(i,j-1).cost + cost("-",t[j])
        return DiffingCell("-",t[j], c)
    
    if j == 0:
        c = table.get(i-1,j).cost + cost(s[i],"-")
        return DiffingCell(s[i], "-", c)
        

    top = table.get(i-1,j).cost + cost(s[i], "-")
    left = table.get(i,j-1).cost + cost("-", t[j])
    diag = table.get(i-1,j-1).cost + cost(s[i], t[j])
    
    
    #a = ""
    #b = ""
    #c = 0
    
    if top <= left and top < diag:
        a = "-"
        b = s[i]
        c = top
    elif left <= top and left < diag:
        a = t[j]
        b = "-"
        c = left
    else:
        a = t[j]
        b = s[i]
        c = diag
        
    return DiffingCell(b, a, c)
    #return DiffingCell('a', 'a' , 0)

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    # TODO: YOUR CODE HERE
    order = []
    for i in range(n+1):
        for j in range(m+1):
            order.append((i,j))      

    return order

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE
    cost = table.get(len(s),len(t)).cost
    first= ""
    second = ""
    
    i = len(s) 
    j = len(t)
    while i > 0 or j > 0: 
        a_s, b_t = table.get(i,j).s_char, table.get(i,j).t_char
        first = first + a_s
        second = second + b_t
        if a_s == "-":
            j = j-1
        elif b_t == "-":
            i = i-1
        else:
            i = i-1
            j = j-1
        
    print(first, second)
    
    return (cost, first[::-1], second[::-1])

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    for i in D._table:
        print (i)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print (align_s)
    print (align_t)
    print ("cost was %d"%cost)
