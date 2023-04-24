import redis
redis_host = 'localhost'
redis_port = 5000

connection = redis.Redis(host=redis_host)