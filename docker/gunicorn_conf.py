import os

from environs import Env


env_file = os.getenv('GUNICORN_ENV_FILE', '.env')

env = Env()
env.read_env(env_file)

web_concurrency = env.int('WEB_CONCURRENCY', None)
default_web_concurrency = 4
host = env('HOST', '0.0.0.0')
port = env('PORT', 80)
use_loglevel = env('LOG_LEVEL', 'info')
use_bind = f'{host}:{port}'
cores = os.cpu_count()

if web_concurrency:
    assert web_concurrency > 0
else:
    web_concurrency = default_web_concurrency

accesslog_var = env('ACCESS_LOG', '-')
use_accesslog = accesslog_var or None
errorlog_var = env('ERROR_LOG', '-')
use_errorlog = errorlog_var or None

# Gunicorn config variables
loglevel = use_loglevel
workers = web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = '/dev/shm'
accesslog = use_accesslog
graceful_timeout = env.int('GRACEFUL_TIMEOUT', 60)
worker_connections = env.int('WORKER_CONNECTIONS', 10000)
max_requests = env.int('MAX_WORKER_REQUESTS', 2500)
max_requests_jitter = env.int('MAX_WORKER_REQUESTS_JITTER', 500)
timeout = env.int('TIMEOUT', 60)
keepalive = env.int('KEEP_ALIVE', 5)
backlog = env.int('BACKLOG', 0)
