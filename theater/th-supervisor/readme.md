### TH-SITE ###

#### Config ####
Edit the .env file


Edit docker-compose.yml file:
    Change the suffics "user-name" of the external integration network to your user name"
  

#### Run ####
```bash
./start.bash
```

#### Stop ####
```bash
.stop.bash [down]
```

#### Connect to the docker container ####
```bash
http://127.0.0.1:8025
```

#### Test via Swagger ####
```bash
http://127.0.0.1:8025/docs
```

#### Connect inside the docker container ####
```bash
docker exec -it th-supervisor-$USER bash
```
