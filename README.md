# NGINX Request Exporter

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Un exportador de métricas ligero y eficiente para Prometheus diseñado para monitorear archivos de log de NGINX, permitiendo la visibilidad en tiempo real del tráfico HTTP.

## Características Principales

*   **Monitoreo en tiempo real:** Calcula el número de solicitudes recibidas por intervalo de tiempo.
*   **Integración con Prometheus:** Expone la métrica `nginx_http_requests` mediante un endpoint HTTP.
*   **Gestión inteligente de logs:** Detecta automáticamente la rotación o el truncamiento del archivo de log para evitar pérdida de datos o reinicios manuales.
*   **Ligero y portable:** Desarrollado en Python, optimizado para ejecutarse como contenedor Docker o script standalone.

## Guía de Inicio Rápido

### Requisitos Previos
*   Python 3.x instalado.
*   Acceso de lectura al archivo `access.log` de tu instancia de NGINX.
*   Docker (opcional, para despliegue en contenedores).

### Despliegue con Docker
Puedes utilizar la imagen precompilada disponible en GitHub Packages:

```bash
docker pull ghcr.io/alejandromolinamedina/count_request_nginx:latest

docker run -d \
  -v /var/log/nginx/access.log:/var/log/nginx/access.log:ro \
  -p 8000:8000 \
  ghcr.io/alejandromolinamedina/count_request_nginx:latest \
  --log /var/log/nginx/access.log --port 8000 --interval 60
```

### Ejecución Local
1. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el exportador:
   ```bash
   python requestPerMinute.py --log /var/log/nginx/access.log --port 8000 --interval 60
   ```

### Argumentos de Configuración
*   `--log`: Ruta absoluta al archivo de log de NGINX (requerido).
*   `--port`: Puerto de escucha para el servidor de métricas (default: `8000`).
*   `--interval`: Intervalo de recolección en segundos (default: `60`).

## Estructura del Proyecto

```text
.
├── Dockerfile          # Configuración para despliegue en contenedores
├── LICENSE             # Términos de licencia del proyecto
├── Pipfile             # Dependencias del entorno de Python
├── README.md           # Documentación del proyecto
├── requirements.txt    # Librerías necesarias para la ejecución
└── requestPerMinute.py # Código fuente principal del exportador
```

## Soporte y Documentación
Si encuentras algún error o deseas solicitar una nueva funcionalidad, por favor utiliza la sección de [Issues](https://github.com/alejandromolinamedina/count_request_nginx/issues) en el repositorio. Asegúrate de incluir los logs relevantes y la versión de NGINX utilizada.

## Mantenimiento y Contribución

Este proyecto es de código abierto. Si deseas contribuir:

1. Realiza un *fork* del repositorio.
2. Crea una rama para tu mejora (`git checkout -b feature/nueva-funcionalidad`).
3. Envía un *Pull Request* con una descripción clara de tus cambios.

Para más información sobre el uso del proyecto, consulta los archivos de configuración incluidos en el repositorio.

---
*Este proyecto se distribuye bajo los términos de la Licencia LICENSE.*