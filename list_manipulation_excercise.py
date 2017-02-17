
# coding: utf-8

# ## LIST MANIPULATION IN PYTHON

# ## A. match_ends

# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
# 
# Note: python does not have a ++ operator, but += works.

# In[100]:

def match_ends(words):
    count=0
    for string in words:
        if len(string)>=2 and string[0]==string[-1]:
            count+=1
    return count


# ## B. front_x

# Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
# 
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# 
# Hint: this can be done by making 2 lists and sorting each of them before combining them.

# In[101]:

def front_x(words):
    x=[]
    y=[]
    for string in words:
        if string[0]=="x":
            x.append(string)
        else:
            y.append(string)
    x.sort()
    y.sort()
    z=x+y
    return z


# ## C. sort_last

# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# 
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# 
# Hint: use a custom key= function to extract the last element form each tuple.

# In[102]:

def customkey(key):
    return key[-1]


# In[103]:

def sort_last(tuples):
    tuples.sort(key=customkey)
    return tuples 


# Simple provided test() function used in main() to print what each function returns vs. what it's supposed to return.

# In[104]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# Calls the above functions with interesting inputs.

# In[105]:

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


# We call the main function.

# In[106]:

main()


# ## D. remove_adjacent

# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.

# In[96]:

def remove_adjacent(nums):
    n=len(nums)
    mlist=[]
    y=iter(xrange(0,n))
    for x in y:
        mlist.append(nums[x])
        if x<n-1 and nums[x]==nums[x+1]:
            while(x<n-1 and nums[x]==nums[x+1]):
                x+=1
        
    return mlist


# ## E. linear_merge

# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.

# In[97]:

def linear_merge(list1, list2):
    x=len(list1)
    y=len(list2)
    i=0
    j=0
    mlist=[]
    
    while(i<x and j<y):
            if list1[i]<=list2[j]:
                mlist.append(list1[i])
                i=i+1
            else: 
                    mlist.append(list2[j])
                    j=j+1
            
    if i==x and j<y:
        for k in range(j,y):
            mlist.append(list2[k])
    elif i<x and j==y:
        for k in range(i,x):
            mlist.append(list1[k])
    return mlist


# Calls the above functions with interesting inputs.

# In[98]:

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])


# We call the main function.

# In[99]:

main()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



