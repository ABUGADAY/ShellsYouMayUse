# Docker 离线安装使用说明

## 使用方式

### 安装

执行命令
我这里放置的是 20.10.3 离线包，也可以自行下载放到目录中
[下载地址](https://download.docker.com/linux/static/stable/)
daemon.json 里配置私服地址(都离线了总归要有内网私服吧)

```bash
# sh install.sh docker-version.tgz
sh install.sh docker-20.10.3.tgz
```

运行结果

```bash
[root@localhost offline_docker_install]# sh install.sh docker-20.10.3.tgz
解压tar包...
docker/
docker/docker
docker/runc
docker/ctr
docker/dockerd
docker/docker-init
docker/docker-proxy
docker/containerd-shim-runc-v2
docker/containerd-shim
docker/containerd
将docker目录移到/usr/bin目录下...
将docker.service 移到/etc/systemd/system/ 目录...
添加文件权限...
重新加载配置文件...
启动docker...
设置开机自启...
docker安装成功...
Docker version 20.10.3, build 48d30b5
```

### 卸载

执行命令

```bash
sh uninstall.sh
```

运行结果

```bash
[root@localhost offline_docker_install]# sh uninstall.sh 
删除docker.service...
删除docker文件...
重新加载配置文件
卸载成功...
```
