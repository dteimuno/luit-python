#This is my second version of the project which I am happy about
import random

def generate_random_ec2_names(num_names):
    department_names = input('What is your department name?')
    ec2_instance_number = range(1,num+1)
    
    random_names = []
    for _ in range(num_names):
        random_full_name = f"{(department_names)}{random.choice( ec2_instance_number)}"
        random_names.append(random_full_name)
    
    return random_names

# Input: number of names to generate
num = int(input('Number of ec2 Instances needed?'))
generated_names = generate_random_ec2_names(num)
print(f"Generated {num} random ec2 Instance names: {generated_names}")
