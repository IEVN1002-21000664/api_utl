# conexion, configuracion base de datos
class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost:8082'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='api_utl'
    # ssl_disabled=True

config={
    'development':DevelopmentConfig
}
