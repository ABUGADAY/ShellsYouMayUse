#按需选用
#设置全局代理
#http
git config --global http.proxy 'http://127.0.0.1:1080'
#https
git config --global https.proxy 'https://127.0.0.1:1080'
#使用socks5代理
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'

#只对github.com使用代理，其他仓库不走代理
git config --global http.https://github.com.proxy 'socks5://127.0.0.1:1080'
git config --global https.https://github.com.proxy 'socks5://127.0.0.1:1080'
