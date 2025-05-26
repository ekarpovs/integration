#### Download postgres and pgAdmin docker images
```bash
docker pull postgres:latest  
docker pull dpage/pgadmin4  
```

#### Connect to the pgAdmin from a browser:
http://localhost:4001  

#### Login to the UI
pgadmin4@pgadmin.org  
admin  

#### Configure web pgAdmin (during the first run)  
server name:        pgsql-dev  

host name/address:  172.21.0.2  
port:               5432  
maintenance database: postgres  
username:           postgres  
password:           test1234

Note:  
Address "IPAddress":"172.21.0.2" from:  
docker inspect pgsql-dev-${USER} -f "{{json .NetworkSettings.Networks }}"  

#### Start/stop the Db and UI from the directory:
docker compose up -d  
docker compose stop  


#### Start single pgadmin:
docker run -p 5051:80 \
    --name "pgadmin"-${USER} \
    -e "PGADMIN_DEFAULT_EMAIL=user@domain.com" \
    -e "PGADMIN_DEFAULT_PASSWORD=SuperSecret" \
    -d dpage/pgadmin4


