# Initialize two numbers
num1 = 10
num2 = 20
print(f'Initial:\nnum1 {num1} num2 {num2}')

# Step 1: Add both numbers and store in num1
num1 = num1 + num2
print(f'\nStep 1:\nnum1 {num1} num2 {num2}')

# Step 2: Subtract original num2 from new num1 to get original num1 and store in num2
num2 = num1 - num2
print(f'\nStep 2:\nnum1 {num1} num2 {num2}')

# Step 3: Subtract new num2 from new num1 to get original num2
num1 = num1 - num2
print(f'\nSwapped:\nnum1 {num1} num2 {num2}')