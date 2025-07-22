from prometheus_client import start_http_server, Gauge
import threading
import argparse
import time
import os

# Define la métrica
my_metric = Gauge('nginx_traffic_requests', 'Solicitudes recibidas por minuto')

def count_lines(path_file):
    try:
        with open(path_file, 'r') as file_log:
            return sum(1 for _ in file_log)
    except FileNotFoundError:
        print(f"El archivo '{path_file}' no existe.")
        return 0
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return 0

def traffic_collector(log_path, interval):
    print(f"Iniciando la recolección de tráfico cada {interval} segundos...")
    previous_lines = count_lines(log_path)

    while True:
        time.sleep(interval)
        current_lines = count_lines(log_path)

        # Detecta si el log fue truncado o reiniciado
        if current_lines < previous_lines:
            print("El log parece haber sido reiniciado. Reseteando contador.")
            delta = current_lines
        else:
            delta = current_lines - previous_lines

        my_metric.set(delta)
        print(f"Solicitudes en los últimos {interval} segundos: {delta}")

        previous_lines = current_lines

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Exporter personalizado para Prometheus.")
    parser.add_argument("--log", type=str, required=True, help="Ruta al archivo de log")
    parser.add_argument("--port", type=int, default=8000, help="Puerto donde exponer métricas (default: 8000)")
    parser.add_argument("--interval", type=int, default=60, help="Intervalo de recolección en segundos (default: 60)")

    args = parser.parse_args()

    # Arranca el servidor en el puerto especificado
    start_http_server(args.port)
    print(f"Servidor Prometheus escuchando en el puerto {args.port}.")

    # Lanza la función en un hilo
    collector_thread = threading.Thread(target=traffic_collector, args=(args.log, args.interval), daemon=True)
    collector_thread.start()

    # Mantiene el proceso vivo
    while True:
        time.sleep(3600)
