class Basket:

    # __init__ is a special constructor method
    # if no parameter given, contents set to None
    def __init__(self, contents=None):
        # short circuit logic, all elements ewuate to a boolean
        # eg. empty string is false, all other strings are true
        # For 'or' if contents is false return [], else return contents
        # For 'and' if contents is false return contents,else return []
        # For 'or' [not contents] if contents is false, true, else false
        self.contents = contents or []

 
        
    def add(self,element):
         self.contents.append(element)

    def print_me(self):
        result = ""
        for element in self.contents:
            result = result + " " + str(element)
            
        # + works here because strings are basically lists of characters
        # indexing, slicing and len will also work on them
        print ("Contains:" + result)

    # Special method for print
    def __str__(self):
        result = ""
        for element in self.contents:
            result = result + " " + str(element)
            return "Contains:"+result
        

'''    
 Constructor below would not work
 If one basket was not empty, subsequent baskets would not be either
 They would all use the same 'unempty' contents in their constructor
 Read identity vs equality for None

  def __init__(self, contents=[]):
    self.contents = contents

 This would get over identity issue above. This would create a new list
 every time rather than copy the same list
 
  def __init__(self, contents=[]):
      self.contents = contents[:]   
'''

b = Basket(["fruit", 3, 4])
b.add("test")
b.print_me()
print (b)



  
