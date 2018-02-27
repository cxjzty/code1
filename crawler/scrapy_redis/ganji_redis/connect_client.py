import redis
conn=redis.Redis(host="127.0.0.1",password="",port=6379)
conn.lpush("mycrawler:start_urls","http://sz.ganji.com/shouji/o1/")