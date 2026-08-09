# NGINX Request Exporter

Un exportador ligero y eficiente para Prometheus diseñado para monitorear archivos de log de NGINX, calcular la tasa de solicitudes y exponer métricas en tiempo real.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Características Principales

- **Monitoreo en tiempo real:** Analiza logs de NGINX para calcular solicitudes por intervalo.
- **Métrica estandarizada:** Expone la métrica `nginx_http_requests` compatible con Prometheus.
- **Resiliencia:** Detección automática de rotación y truncamiento de archivos de log.
- **Versátil:** Soporte para ejecución nativa en Python o mediante contenedor Docker.

## Estructura del Proyecto

```text
.
├── Dockerfile          # Definición de la imagen del contenedor
├── Pipfile             # Gestión de dependencias (Pipenv)
├── LICENSE             # Términos de la licencia
├── README.md           # Documentación del proyecto
├── requirements.txt    # Dependencias del proyecto
└── requestPerMinute.py # Lógica principal del exportador
```

## Guía de Inicio Rápido

### Docker (Recomendado)

Obtén la imagen desde GitHub Packages y ejecuta el contenedor montando el volumen de logs:

```bash
docker pull ghcr.io/alejandromolinamedina/count_request_nginx:latest

docker run -d \
  -v /var/log/nginx/access.log:/var/log/nginx/access.log:ro \
  -p 8000:8000 \
  ghcr.io/alejandromolinamedina/count_request_nginx:latest \
  --log /var/log/nginx/access.log --port 8000 --interval 60
```

### Ejecución Local

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicia el script:
   ```bash
   python requestPerMinute.py --log /ruta/a/tu/nginx/access.log --port 8000 --interval 60
   ```

### Argumentos de configuración

| Argumento | Descripción | Default |
| :--- | :--- | :--- |
| `--log` | Ruta absoluta al archivo access.log de NGINX | Requerido |
| `--port` | Puerto de escucha para métricas de Prometheus | 8000 |
| `--interval` | Intervalo de recolección en segundos | 60 |

## Soporte y Contribución

- **Reporte de errores:** Utiliza la sección de *Issues* en el repositorio para reportar bugs o solicitar nuevas funcionalidades.
- **Contribuciones:** Las propuestas de mejora son bienvenidas mediante *Pull Requests*. Asegúrate de seguir las convenciones de estilo del código.

## Licencia

Este proyecto se distribuye bajo los términos de la licencia especificada en el archivo [LICENSE](./LICENSE).