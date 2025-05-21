from common import aws_resource_functions as aws

# Security group ingress permissions
ingress_permissions = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 3306, 'ToPort': 3306},
]

# Read security group name and sescription
sg_name = 'backend-sg'
sg_description = 'grupo de seguridad para el backend'

# Create security group
aws.create_security_group(sg_name, sg_description, ingress_permissions)

# List security groups
aws.list_security_groups()