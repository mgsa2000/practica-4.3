from common.aws_resource_class import AWS

#definimos los parametros
sg_name_frontend = 'frontend-sg'
sg_name_backend = 'backend-sg'
sg_name_nfs = 'nfs-sg'
sg_name_lb = 'lb-sg'

sg_description_front = "grupo para el Frontend"
sg_description_back = "grupo para el Backend"
sg_description_lb = "grupo para el Balanceador"
sg_description_nfs = "grupo para el Servidor Nfs"

ami = 'ami-04b4f1a9cf54c11d0'
instance_type = 't2.small'
key_name = 'vockey'

instance_name_frontend_1 = "frontend-1"
instance_name_frontend_2 = "frontend-2"
instance_name_backend = "backend"
instance_name_nfs = "nfs"
instance_name_loadbalancer = "loadbalancer"

ingress_permissions_frontend = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80},
]

ingress_permissions_backend = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 3306, 'ToPort': 3306},
]

ingress_permissions_nfs = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 2049, 'ToPort': 2049},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22}
]

ingress_permissions_loadbalancer = [
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22},
    {'CidrIp': '0.0.0.0/0', 'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80},
]

def main():
    aws = AWS()
    print("Iniciando despliegue")

    # Crear el sg frontend
    if not aws.security_group_exists(sg_name_frontend):
        print(f"Creando grupo de seguridad: {sg_name_frontend}...")
        aws.create_security_group(sg_name_frontend, sg_description_front, ingress_permissions_frontend)

    # Crear el sg backend
    if not aws.security_group_exists(sg_name_backend):
        print(f"Creando grupo de seguridad: {sg_name_backend}...")
        aws.create_security_group(sg_name_backend, sg_description_back, ingress_permissions_backend)

    # Crear el sg NFS
    if not aws.security_group_exists(sg_name_nfs):
        print(f"Creando grupo de seguridad: {sg_name_nfs}...")
        aws.create_security_group(sg_name_nfs, sg_description_nfs , ingress_permissions_nfs)

    # Crear el sg lb
    if not aws.security_group_exists(sg_name_lb):
        print(f"Creando grupo de seguridad: {sg_name_lb}...")
        aws.create_security_group(sg_name_lb, sg_description_lb, ingress_permissions_loadbalancer)
        
        
    # Crear instancias EC2
    print("Creando instancias EC2...")

        

# Crear instancias EC2
    print("Creando instancias EC2...")
    # Crear instancias frontend 1 y 2
    instance_id_frontend_1 = aws.create_instance(ami, 1, instance_type, key_name, instance_name_frontend_1, sg_name_frontend)
    instance_id_frontend_2 = aws.create_instance(ami, 1, instance_type, key_name, instance_name_frontend_2, sg_name_frontend)
    # Crear instancia backend 
    instance_id_backend = aws.create_instance(ami, 1, instance_type, key_name, instance_name_backend, sg_name_backend)
    # Crear servidor NFS
    instance_id_nfs = aws.create_instance(ami, 1, instance_type, key_name, instance_name_nfs, sg_name_nfs)
    # Crear balanceador 
    instance_id_loadbalancer = aws.create_instance(ami, 1, instance_type, key_name, instance_name_loadbalancer, sg_name_lb)

    # 3️ Listar instancias activas
    print("Listando instancias...")
    aws.list_instances()

    print("Despliegue completado con éxito.")

if __name__ == "__main__":
    main()