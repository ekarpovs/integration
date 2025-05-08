### TH-UI-PROXY ###
Provides the UI pack of templates for the th-client(s)

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
http://127.0.0.1:8022
```

#### Test via Swagger ####
```bash
http://127.0.0.1:8022/docs
```

#### Connect inside the docker container ####
```bash
docker exec -it th-client-evgeny bash
```

### **Diagram Breakdown**
1. **Owned by Different Organizations:**
   - **Sites (1-N):** Serve content to the viewers.
   - **Viewers (V 1-N):** Consume content from the broadcast server.
   - **Prompters (P 1-N):** Provide content chunks to the broadcast server.
   - **Admin:** Manages the site's content and process flow (upload, clean, start, stop).

2. **Shared Components:**
   - **UI-Proxy:** Stores viewer and prompter frontend files.
   - **Broadcast Server:** Distributes content chunks from the prompters to the viewers.

3. **Connections and Flow:**
   - **Viewers** consume content from the **Broadcast Server**.
   - **Prompters** push content chunks to the **Broadcast Server**.
   - **Admins** interact with the organization **Site**.
   - The **Broadcast Server** interacts with the **UI-Proxy** to store or retrieve frontend files.
