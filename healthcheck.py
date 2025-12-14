# healthcheck.py
import os, sys, urllib.request, urllib.error, socket, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", default=None, help="URL a chequear (ej: http://127.0.0.1:8000/health)")
parser.add_argument("--timeout", type=int, default=2, help="Timeout en segundos")
args = parser.parse_args()

# Si no se proporciona URL, usa la variable de entorno PORT
if args.url:
    url = args.url
else:
    port = os.environ.get("PORT", "8000")
    url = f"http://127.0.0.1:{port}/health"

socket.setdefaulttimeout(args.timeout)
try:
    with urllib.request.urlopen(url, timeout=args.timeout) as r:
        print(f"[OK] {url} -> {r.getcode()}")
        sys.exit(0 if r.getcode() == 200 else 1)
except Exception as e:
    print(f"[ERROR] {url} -> {e}")
    sys.exit(1)
