
# Test Lite Tihinking

La idea del proyecto es implemtar un backend en Django Rest Framework (DRF) para consumir desde un frontend.

El Backend se ejecutara con una instancia de docker al igual que la base de datos en postgresql.

El backend tendrá los endpoints correspondientes para Agregar, Consultar, Editar o Eliminar un registro, dependiendo de la ruta usada del API.


## Despliegue

Para desplegar el proyecto se pensó de la siguiente manera, ejecutar los dos contenedores que tienen tanto el backend como la base de datos. Conectar los contenedores a traves del comando `docker network conect <contenedor_backend> <contenedor_base de datos>`


```bash
# Clonar el repositorio
# Ubicar la carpeta del backend
cd test_litethinking_back

# Crear el contenedor a traves de la imagen
docker compose build

# Ejecutar el contenedor creado
docker compose up -d

# Crear el contenedor de la base de datos
cd BD_TEST
docker compose build
docker compose up -d

# Crear la conexión entre los dos contenedores
docker network connect test_litethinking_back_default BD_LITE


```

De está manera ya está corriendo el contenedor y la conexión a la base de datos
## API Reference

#### Generar token de acceso

```http
  POST /api/token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Usuario de la aplicación |
| `password` | `string` | **Required**. Contraseña de usuario |

#### Crear un registro de empresas

```http
  POST /api/empresas
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authentication Bearer` | `string` | **header**. Token generado con el método login |
| `id_nit` | `string` | **JSON**. Nit de la empresa |
| `nombre` | `string` | **JSON**. Token generado con el método login |
| `direccion` | `string` | **JSON**. Token generado con el método login |
| `telefono` | `string` | **JSON**. Token generado con el método login |

#### Consultar todas las empresas

```http
  GET /api/empresas
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **header**. Token generado con el método login |

#### Consultar una sola empresa por id

```http
  GET /api/empresas/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Bearer Token` | `string` | **header**. Token generado con el método login |


#### add(num1, num2)
Takes two numbers and returns the sum.


## Authors

- [@SoulHarry](https://www.github.com/SoulHarry)

