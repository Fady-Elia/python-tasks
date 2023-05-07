# We created a function and gave it the string and position and character
def function(string='abracadabra' ,position=5 ,character='k'):     
    mylist= list(string) 
    mylist[position]= character 
    string = ''.join(mylist) 
    print (string)   
function() 