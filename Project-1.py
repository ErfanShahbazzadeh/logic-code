class Editor:

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
        deleted_count = 0  # Count how many items were deleted  
        new_index = 0
        for i in range(self.Pointer):  
            if self.Array[i] == value:  
                deleted_count += 1  # Increment the count of deleted items  
            else:  
                self.Array[new_index] = self.Array[i]  # Keep non-matching items  
                new_index += 1
        self.Pointer = new_index

        if deleted_count > 0:  
            print(f"Deleted {deleted_count} occurrences of value: {value}")  
        else:  
            print("Value not found.") 

    def Delete_By_Index(self, input):
        
        if input <0 or input > self.Pointer: # Check if the input is a valid index
            print("Index out of range")
            return
        for i in range(input, self.Pointer - 1):
            self.Array[i] = self.Array[i + 1] # Shift elements to the left 
        self.Pointer -= 1 # Decrease pointer
        self.Array[self.Pointer] = 0 # Clear the last index for cleaner array
        
        #counter = 0 
        #for item in self.Array:
        #    if item != 0:
        #        print(item)
        #        self.Array[counter] = item
        #        counter += 1
    
    def Display(self):
        print("[", end="")
        for i in range(self.Pointer):
            if i == self.Pointer - 1:
                print(self.Array[i], end="")
            else:
                print(self.Array[i], end=",") 
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
                          
    def Search_By_Value(self, value):
        limit = self.size
        Index_Array = [0]*limit # Initializing a new array for founded index
        count = 0 # Count the number of found indexes
        Dis_count = 0 # Size of the displayer array
        for index in range(self.Pointer): # Search thoroug the Array
            if self.Array[index] == value:
                if count < limit:
                    Index_Array[count] = index
                    count += 1
        
        Dis_Array = [0]*count # Initializing the dispalyer array

        # Removing the '0' in the Index_Array
        for item in Index_Array:
            if item != 0: 
                Dis_Array[Dis_count] = item
                Dis_count += 1 

        # Result of the search
        if count > 0:
            print(f"Value {value} found at index: {Dis_Array}")
        else:
            print("There is no such value")
            return None # Return none if it doesn't exist

    def resize(self):  
        new_size = self.size * 1 + 1 if self.size > 0 else 1  # Ensure at least size of 1  
        new_array = [0] * new_size  # Create a new array with more size  
        for i in range(self.Pointer):  
            new_array[i] = self.Array[i]  # Copy old elements to new array  
        self.Array = new_array  # Update reference to new array  
        self.size = new_size  # Update the size 

    def Initialize(self, List):
        for item in List:
            self.Append(item)

obj = Editor() # Initialize the Class

# Test Case
'''
Test = [1, 2, 3, 4, 5, 0, 2, 3 ,1]
obj.Initialize(Test)
obj.Display()
obj.Reverse()
obj.Insert(5, 443)
obj.Display()
obj.Append(65)
obj.Delete_By_Index(3)
obj.Display()
obj.Delete_By_Value(2)
obj.Display()
obj.Search_By_Value(3)
'''