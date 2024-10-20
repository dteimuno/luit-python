import random

def generate_random_ec2_names(num_names):
    department_names = ['Marketing', 'Accounting', 'FinOps', 'IT', 'Research']
    ec2_instance_number = ['1', '2', '3', '4', '5']
    
    random_names = []
    for _ in range(num_names):
        random_full_name = f"{random.choice(department_names)}{random.choice( ec2_instance_number)}"
        random_names.append(random_full_name)
    
    return random_names

# Input: number of names to generate
num = int(input('Number of ec2 Instances needed?'))
generated_names = generate_random_ec2_names(num)
print(f"Generated {num} random ec2 Instance names: {generated_names}")
