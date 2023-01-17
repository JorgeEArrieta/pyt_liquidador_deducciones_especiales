import psycopg2
import socket

class Usuario():

    def __init__(self):
        
        try:

            self.conexion = psycopg2.connect(
                host = 'ec2-52-70-186-184.compute-1.amazonaws.com',
                user = 'uhkhpyurbvrqdt',
                password = '1c4e30a0522816fc12826c162c59093b54b4d2dbffb4dbc27664893100085169',
                database = 'd3e6kcug0s3nur'
            )

        except Exception as error:
            print(error)

    def verifica_user(self, user: str, password: str) -> bool:
        
        try:
            
            cursor = self.conexion.cursor()

            cursor.execute('select usuario from users where usuario = %s and pass = %s', (user, password,))

            resultado = cursor.fetchone()

            if resultado != None:
                
                return True

            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def verifica_estado(self, user: str, password: str) -> bool:
    
        try:
            ip = str(socket.gethostbyname(socket.gethostname()))

            cursor_estado = self.conexion.cursor()
            cursor_estado.execute('select estado from users where usuario = %s and pass = %s', (user, password,))
            resultado_estado = cursor_estado.fetchone()

            cursor_ip = self.conexion.cursor()
            cursor_ip.execute('select ip from users where usuario = %s and pass = %s', (user, password,))
            resultado_ip = cursor_ip.fetchone()
            
            if resultado_estado[0] == 'desconectado' or ip == resultado_ip[0]:
                return True
            else:
                return False
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def actualiza_estado(self, user: str, estado: str) -> bool:

        try:
        
            cursor = self.conexion.cursor()
            cursor.execute('UPDATE users SET estado = %s where usuario = %s', (estado, user,))
            self.conexion.commit()
    
            return True
               
        except Exception as error:
            print(error)
            return False

    def actualiza_ip(self, user: str) -> bool:
        
        try:

            ip = str(socket.gethostbyname(socket.gethostname()))
    
            cursor = self.conexion.cursor()
            cursor.execute('UPDATE users SET ip = %s where usuario = %s', (ip, user,))
            self.conexion.commit()
    
            return True
           
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False

    def cerrar_conexion(self):
        try:
            self.conexion.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)