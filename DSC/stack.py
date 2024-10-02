class ArrayStack:
    def __init__(self):
        
        self.stack = []

    def push(self, item):
        
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from stack.")
        return item

    def peek(self):
        
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.stack[-1]

    def is_empty(self):
        
        return len(self.stack) == 0

    def display(self):
        
        print("Current stack:", self.stack)



if __name__ == "__main__":
    array_stack = ArrayStack()

    array_stack.push(10)
    array_stack.push(20)
    array_stack.push(30)
    array_stack.display()  

    print("Top item:", array_stack.peek())  

    array_stack.pop()      
    array_stack.display()  
