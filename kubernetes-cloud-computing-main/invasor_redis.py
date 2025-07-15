import redis

redis_ip = input("redis_ip: ")
redis_port = input("redis_port: ")

r = redis.Redis(host=redis_ip, port=int(redis_port))

list_name = input("list name: ")

values = r.lrange(list_name, 0, -1)

print("List items:")
for item in values:
    print(item.decode('utf-8'))