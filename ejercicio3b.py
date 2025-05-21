import time
from common.aws_resource_class import AWS

# Definir nombres de grupos de seguridad e instancias
sg_names = ["frontend-sg", "backend-sg", "nfs-sg", "lb-sg"]
instance_names = ["frontend-1", "frontend-2", "backend", "nfs", "loadbalancer"]

def main():
    aws = AWS()
    print("Eliminación de infraestructura en proceso...")

    # Terminar instancias
    for instance_name in instance_names:
        aws.terminate_instance(instance_name)

    # Esperar un tiempo fijo para que las instancias se terminen
    print(" Esperando 120 segundos para la terminación de instancias...")
    time.sleep(120)  # Espera 2 minutos antes de continuar

    # Eliminar grupos de seguridad
    for sg_name in sg_names:
        aws.delete_security_group(sg_name)

    print("Eliminación completada con éxito.")

if __name__ == "__main__":
    main()
