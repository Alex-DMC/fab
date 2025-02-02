
# 本地开发

## deploy mysql

```
linux
docker run --network host --restart always --name mysql -e MYSQL_ROOT_PASSWORD=admin -d mysql:5.7
mac
docker run -p 3306:3306 --restart always --name mysql -e MYSQL_ROOT_PASSWORD=admin -d mysql:5.7

```
进入数据库创建一个db
```
CREATE DATABASE IF NOT EXISTS myapp DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```
镜像构建


```
构建基础镜像（包含基础环境）
docker build -t myapp-base -f install/docker/Dockerfile-base .

使用基础镜像构建生产镜像
docker build -t tencentmusic/myapp:2020.10.01 -f install/docker/Dockerfile .
```

镜像拉取(如果你不参与开发可以直接使用线上镜像)
```
docker pull tencentmusic/myapp:2020.10.01
```

## deploy myapp (docker-compose)

本地开发使用

docker-compose.yaml文件在install/docker目录下，这里提供了mac和linux版本的docker-compose.yaml。
可自行修改
image：刚才构建的镜像
MYSQL_SERVICE：mysql的地址


1) init
```
cd install/docker
STAGE: 'init'
docker-compose -f docker-compose.yml  up
```
will create table and role/permission

2) debug backend
```
STAGE: 'dev'
docker-compose -f docker-compose.yml  up
```
3) Production
```
STAGE: 'prod'
docker-compose -f docker-compose.yml  up
```

部署以后，登录首页会自动调用认证，会自动创建用户，绑定角色（Gamma和rtx同名角色）。

可根据自己的需求为角色授权。

# 生产部署

参考install下方法
