# NGINX Request Exporter

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un exportador ligero y eficiente para Prometheus diseñado para monitorear archivos de log de NGINX, calcular la frecuencia de solicitudes en tiempo real y exponer métricas clave para su análisis y visualización.

## Características Principales

- **Monitoreo en Tiempo Real:** Analiza continuamente el flujo de logs de NGINX.
- **Métricas Prometheus:** Expone la métrica `nginx_http_requests` (Gauge) compatible con el ecosistema de monitoreo de Prometheus.
- **Resiliencia:** Detección inteligente de rotación o truncamiento de archivos de log, asegurando la continuidad de la medición sin intervención manual.
- **Configurable:** Ajusta fácilmente el intervalo de recolección y los puertos de exposición.

## Guía de Inicio Rápido

### Requisitos Previos
- Python 3.x instalado.
- Acceso de lectura al archivo de log de NGINX (`access.log`).

### Docker
La forma más rápida de ejecutar el exportador es mediante nuestra imagen oficial:

```bash
docker run -d \
  -v /var/log/nginx/access.log:/var/log/nginx/access.log:ro \
  -p 8000:8000 \
  ghcr.io/alejandromolinamedina/count_request_nginx:latest \
  --log /var/log/nginx/access.log --port 8000 --interval 60
```

### Local (Python)
1. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el script:
   ```bash
   python requestPerMinute.py --log /ruta/a/tu/nginx/access.log --port 8000 --interval 60
   ```

### Argumentos de Línea de Comandos
| Argumento | Descripción | Default |
| :--- | :--- | :--- |
| `--log` | Ruta absoluta al archivo access.log de NGINX | Requerido |
| `--port` | Puerto para exponer métricas de Prometheus | 8000 |
| `--interval` | Frecuencia de recolección en segundos | 60 |

## Estructura del Proyecto

```text
.
├── Dockerfile          # Configuración para contenedorización
├── Pipfile             # Gestión de dependencias de Python
├── LICENSE             # Términos de la licencia
├── README.md           # Documentación del proyecto
├── requirements.txt    # Lista de dependencias del sistema
└── requestPerMinute.py # Script principal de recolección de métricas
```

## Soporte y Contribución

- **Reportar Errores:** Por favor, utiliza la sección de Issues del repositorio.
- **Contribuciones:** Agradecemos las contribuciones para mejorar la estabilidad y nuevas funcionalidades. Consulta las políticas de contribución en el repositorio.

## Licencia

Este proyecto se distribuye bajo la licencia especificada en el archivo [LICENSE](./LICENSE).