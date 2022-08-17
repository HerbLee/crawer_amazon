import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def get_key(k):
    return r.get(k)


def set_key(k, v):
    r.set(k, v)


def add_root_url(**v):
    r.lpush("root_host", str(v))


def pop_root_url():
    return r.rpop("root_host")



def add_second_url(**v):
    r.lpush("second_host", str(v))


def pop_second_url():
    res = r.rpop("second_host")
    return res


def add_item_list(**v):
    r.lpush("item_list", str(v))


def pop_item_list():
    res = r.rpop("item_list")
    return res


if __name__ == '__main__':
    r.set("a", "b")
    print(get_key("a"))
