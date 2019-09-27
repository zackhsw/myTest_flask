# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好