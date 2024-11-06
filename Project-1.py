class Custom_list:

    def __init__(self):
        self.Pointer = 0
        self.size = 0
        self.Array = []
        

    def Insert(self, index, value):
        if index <0 or index > self.Pointer: # Check if index is valid
            print("Index out of range")
            return
        if self.Pointer >= self.size:  # Check if we need to resize the array  
            self.resize()
        for i in range(self.Pointer, index, -1):  
            self.Array[i] = self.Array[i - 1]  # Shift elements to the right 
        self.Array[index] = value # Insert the new element
        self.Pointer += 1 # Increase the pointer

    def Delete_By_Value(self, value):
        Bool = 0
        for x in range(self.Pointer):  
            if self.Array[x] == value:  
                for j in range(x, self.Pointer - 1):  
                    self.Array[j] = self.Array[j + 1]  # Shift elements to the left  
                self.Pointer -= 1  # Decrease pointer  
                # Clear the last element for cleanliness  
                self.Array[self.Pointer] = 0  
                Bool = 1   
        return Bool   

    def Delete_By_Index(self, input):
        if input <0 or input > self.Pointer: # Check if the input is a valid index
            print("Index out of range")
            return
        for i in range(input, self.Pointer - 1):
            self.Array[i] = self.Array[i + 1] # Shift elements to the left 
        self.Pointer -= 1 # Decrease pointer
        self.Array[self.Pointer] = 0 # Clear the last index for cleaner array
    
    def Display(self):
        #for x in range(self.Pointer):  
        #    print(self.Array[x]) #Print out the array
        index = 0
        print("[", end = " ")
        for item in self.Array:
            if index != self.Pointer - 1 :
                print(item, end = " , ")
            else:
                print(item, end = " ")
            index += 1
        print("]")

        
    def Append(self,value):
        if self.Pointer >= self.size:  # Check if we need to resize the array  
            self.resize()
        self.Array[self.Pointer] = value #Append the value to the end of the array
        self.Pointer += 1 #Expand the size of the array

    def Reverse(self):
        Reversed_Array = [0]* self.Pointer # Create a new array
        for i in range(self.Pointer):
            Reversed_Array[i]=self.Array[self.Pointer -1 -i] # Copy the old array in the new one in reversed order
        
        print("Reversed Array:", Reversed_Array) # Print the Reveresed array
        
        for i in range(self.Pointer):
            self.Array[i] = Reversed_Array[i] # Append the new array
                          
    def Search_By_Value(value):
        Index_Array = [0]* self.Pointer # Create a new array
        i = 0
        for index in range(self.Pointer): # Search thoroug the Array
            if self.Array[index] == value:
                Index_Array[i] = index
                i += 1
            return Index_Array
        print("There is no such value")
        return None # Return none if it doesn't exist

    def resize(self):  
        new_size = self.size * 2 + 1 if self.size > 0 else 1  # Ensure at least size of 1  
        new_array = [0] * new_size  # Create a new array with more size  
        for i in range(self.Pointer):  
            new_array[i] = self.Array[i]  # Copy old elements to new array  
        self.Array = new_array  # Update reference to new array  
        self.size = new_size  # Update the size 

obj = Custom_list() # Initialize the Class

# Main loop 
while True:
    I = input("What would you like to do?")
    if I == "Insert":
        Index = int(input("what index would you like to insert to?"))
        Value = int(input("What value would you like to insert?"))
        obj.Insert(Index, Value)
    elif I == "Delete by value":
        Value = int(input("What value would you like to delete? "))
        Check = obj.Delete_By_Value(Value)
        if Check == 0:
            print("There is no such value in the array")
    elif I == "Delete by index":
        Index = int(input("What index would you like to delete? "))  
        obj.Delete_By_Index(Index) 
    elif I == "Append":
        Value = int(input("What value would you like to Append?"))
        obj.Append(Value)
    elif I == "Reverse":
       obj.Reverse()
    elif I == "Search by value":
        Value = int(input("What value would you like to search for? "))  
        index = obj.Search_By_Value(Value)  
        if index is not None:  
            print(f"Value {Value} found at index: {Index_Array}") 
    elif I == "Display":
        obj.Display()
    elif I == "Exit":
        break # Exit the loop
    else:
        print("Invalid Operation")