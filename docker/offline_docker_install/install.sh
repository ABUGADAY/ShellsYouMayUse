#!/bin/sh
echo '解压tar包...'
tar -xvf $1

echo '将docker目录移到/usr/bin目录下...'
cp docker/* /usr/bin/

echo '将daemon.json 移到/etc/docker/目录下...'
cp daemon.json /etc/docker/


echo '将docker.service 移到/etc/systemd/system/ 目录...'
cp docker.service /etc/systemd/system/

echo '添加文件权限...'
chmod +x /etc/systemd/system/docker.service
chmod +x /etc/docker/daemon.json

echo '重新加载配置文件...'
systemctl daemon-reload

echo '启动docker...'
systemctl start docker

echo '设置开机自启...'
systemctl enable docker.service

echo '登陆私服...'
#docker login dockerhub url -p pwd -u usr


echo 'docker安装成功...'
docker -v
