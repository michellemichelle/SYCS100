<SOUP>bsearch.py

'''Team S.O.U.P 
    Parnell Kelley
    Johnathan Curry 
    Jordan Marsaw
    Darius Carter
    Larry Sanders
    Marcus Killebrew'''
    
    
#Parnell Kelley
def bsearch (element, alist):               #Defines the function bsearch for a given list. Accepts the parameter 'element' to search for within the list.
        StartPoint = -1                           #Identifies a starting-point (one boundary) for the function to begin searching the list for the given element.
        EndPoint = len(alist)                     #Identifies an end-point (other boundary) for the function to end its search within the list or given boundaries for the given element.
        while StartPoint != EndPoint-1:           #Initiates a loop for which the condition is that each end/start point and end point/boundaries of the list being searched are not equal to one another. In other words...that the ordered list is not iterating over the same number. 
                MidPoint = (StartPoint + EndPoint) / 2  #Sets the varable 'Midpoint' equal to the average of the start and end points of the ordered list.
                if element > alist[MidPoint]:           #Conditional statement that if the element being searched for is greater than the midpoint of the list/ or if this condition returns the boolean value of True then move within the conditional for the next step. 
                        StartPoint = MidPoint                 #Sets the start point for the list at the midpoint if the given condition returns True.
                elif element < alist[MidPoint]:         #Conditional statement if the previos conditional is false. 
                        EndPoint = MidPoint                   #Sets the End Point equal to the midpoint of the original list if the second condition returns True
                elif element == alist[MidPoint]:        #Conditional statement to be executed if neither of the previos two conditions return True.
                        return MidPoint                       #Exits the function 'bsearch' and returns the value of midpoint after any number of iterations. 
        return -1                                 #if the condition of the loop is not satisfied that startpoint is not equal to endpoint -1 or if no condition within the loop is satisfied then -1 is returned and the function is exited. 


#Johnathan Curry
def bsearch(myList, item): #defines the function
  midpoint = len(myList) / 2 #gives midpoint the value of half the length of the list
  left = myList[0 : midpoint] #splits the list into two parts, the first from the begining to midpoint
  right = myList[midpoint: len(myList) - 1] #the second from the midpoint to the end
  while found is False: #the loop will continue until found is true
    midpoint = len(myList) / 2 #redefines midpoint
    if item < myList[midpoint]: #if item is less than the midpoint
      myList[midpoint] = len(left) / 2 #midpoint is equal to half the length of the left side
    elif item > myList[midpoint]: #if item is greater
      myList[midpoint] = len(right) / 2 #midpoint is equal to half the lenght of the right side
    elif item == myList[midpoint]: #when the midpoint is equal to the item
      found is True #found becomes true
      return myList[midpoint] #then exits the loop
    elif item not in myList: #if the item is not in the list
      return -1 #the loop exits and returns -1

#Jordan Marsaw 
''' The function takes a (L)ist and a (S)earch element and then makes takes the highest value as the last possible 
    index of the list (Remember that binary searches only work on lists that are sorted). The low value is at the 
    first position of the list and mid will be the high and low positions halved. While the list isn't empty, and 
    the mid and high values aren't the same, check to see if the (S)earch element is less than the element at the 
    middle of the list - if the (S)earch element is less than the element at mid then the middle point is the half 
    of the first part of the list, and the loop runs from the top again. Elif (S)earch element is greater than the 
    element at the position then the mid is changed to the middle of the upper half. If the values are the same 
    then just return the position in the list where the same values were found. When none of these conditions are 
    satisfied, return -1 '''
def BSearch(L, S):
	high = len(L) - 1
	low = 0
	mid = (high + low) / 2
	while mid < high and high >= 1 and high > low:
		if S < L[mid]:
     			mid = mid / 2
    		elif S > L[mid]:
      			mid = (mid + high) / 2
    		elif S == L[mid]:
      			return mid
    		else:
      			return -1
   
def bsearchRecursive(L, S, Min, Max):
  ''' The function takes a (L)ist, a (S)earch element, the minimum value of the list, and the maximum value of the list. 
      Mid is set at the halfway mark of the full list. If(S)earch element is less than the value at L[Mid] then the
      function calls itself again with the same (L)ist, the same (S)earch element, the Min value is set to the lowest
      value of the list (L[0]), and Max is set to the the value of the the halfway point and Mid is then changed to the 
      middle point based on the new Min and Max declared when the function is called. '''
      Mid = (Min + Max) / 2
      while len(L) != 0
      if S < L[Mid]:
      	return bsearchRecursive(L, S, Min = L[0], Max = L[Mid - 1])
      elif S > L[Mid]:
    	return bsearchRecursive(L, S, Min = L[Mid + 1], Max = L[-1])
      elif S == L[Mid]:
    	return Mid
      else:
    	return -1
  
#Xavier Ward
def Bsearch(SuperList, searchElement): #Fixed
	lowest = 0
    	highest = len(SuperList) - 1
    	mid = (lowest + highest) / 2
    	while highest >= lowest:  
        	if (searchElement >  SuperList[mid]):
        		mid = mid + highest / 2
        	elif searchElement < SuperList[mid]:
        		mid = mid / 2
      		elif searchElement == SuperList[mid]:
        		return mid
      		else:
        		return -1
        		
#Marcus Killebrew    
def binarySearch(BCL , Points): #Resubmission
	low = 0 
	high = len(BCL) - 1
	while low <= high:
		middle = (low+high)/2
        if BCL[middle] < Points:
        	low =middle + 1
        if BCL[middle]== Points:
                middle= middle/2
        elif Points <BCL[middle]:
            high = middle - 1
            return middle
            else:
            return -1

        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
