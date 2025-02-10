### Socket.Io client ###
Simple Socket.io client that receives messages from a Socket.io server   

#### Install ####


#### Config ####


#### Usage from cmd ####


#### Usage from Docker container ####
```bash
docker run --rm --network host --name sio-client-${USER} -d -it ekarpovs/sio-client-aarch64:1.0.0
```

### Build the docker file 
```bash
docker build . --tag ekarpovs/sio-client-aarch64:1.0.0
```

### Publish to the Docker registry
```bash
docker login -u <your-github-username>
docker push ekarpovs/sio-client-aarch64:1.0.0
``` 
