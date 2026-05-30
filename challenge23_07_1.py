payments = [400, 600, 800, 200] 

total = sum(payments) # adding the values in the list 
share = total / 4  # dividing equally 
#print(share)

names= {
  "Preethi":400,
  "Khushi":600,
  "Nivya":800,
  "Neha":200
}
# above the main guard you will have the variable , classes , functions and imports 
# below the main guard you will have the actual work that you are doing like excuting statements or loops, calling 
# functions creating objects from classes and using print statements 
if __name__ == '__main__':
    for name,p in names.items():
        balance = p - share 
    
        if balance > 0:
            print(f"{name} should receive ₹{balance}") 
        
        elif balance < 0:
            print(f"{name} should receive ₹{balance}")
        
        else:
            print(f"{name} paid fully")

        
    print(names)
    
    
    


