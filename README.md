# Request Export NGINX

Este proyecto proporciona un exportador personalizado para Prometheus que monitorea archivos de log de NGINX, calcula el número de solicitudes recibidas por intervalo de tiempo y expone estas métricas para ser consumidas por Prometheus.

## Funcionalidades

- **Monitoreo de logs:** Cuenta el número de solicitudes en el archivo de log de NGINX en un intervalo definido.
- **Métrica Prometheus:** Expone la métrica `nginx_http_requests` (Gauge).
- **Soporte de Rotación de Logs:** Detecta cuando el archivo de log ha sido rotado o truncado y reinicia el contador automáticamente.

## Modo de Uso

### Docker

Puedes utilizar la imagen disponible en GitHub Packages:

```bash
docker pull ghcr.io/alejandromolinamedina/count_request_nginx:latest
```

Para ejecutar el contenedor, debes montar el archivo de log de NGINX de tu host dentro del contenedor:

```bash
docker run -d \
  -v /var/log/nginx/access.log:/var/log/nginx/access.log:ro \
  -p 8000:8000 \
  ghcr.io/alejandromolinamedina/count_request_nginx:latest \
  --log /var/log/nginx/access.log --port 8000 --interval 60
```

### Local (Python)

Si prefieres ejecutarlo localmente:

1. Asegúrate de tener instalado Python y las dependencias (puedes usar `pip install -r requirements.txt`).
2. Ejecuta el script directamente:

```bash
python requestPerMinute.py --log /ruta/a/tu/nginx/access.log --port 8000 --interval 60
```

### Argumentos

- `--log`: Ruta completa al archivo de log de NGINX (requerido).
- `--port`: Puerto para exponer las métricas de Prometheus (default: 8000).
- `--interval`: Intervalo de recolección en segundos (default: 60).

## Licencia

Este proyecto está bajo la Licencia LICENSE.
