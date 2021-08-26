#取消github代理
git config --global --unset http.https://github.com.proxy
git config --global --unset https.https://github.com.proxy

#取消全局代理
git config --global --unset http.proxy
git config --global --unset https.proxy
