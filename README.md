### Integration site ###

Before start the integration/tests process:  

1. Create separate branch.  
2. Edit docker-compose.yml files:
    Change the suffics "user-name" of the external integration network to your user name"
3. Create the external network:  

```bash
docker network create integration-${USER}
```

After the integration/tests process,  
Remove the external network:  

```bash
docker network rm integration-${USER}
```
