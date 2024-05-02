# Interact Ubuntu with docker

**First we need to install ubuntu in docker:**
Follow these steps:
1.  Open docker desktop and for start
2.  Try to login in docker hub account
3.  Open terminal in your desired directory in my case
<img src="" alt="Ubuntu" width="500px">
4. Now Run this command

```bash
    docker run ubuntu
```
This command first check ubuntu is available in any container? if not that it will pull or download from docker hub.
<img src="" alt="Ubuntu" width="500px">

**Check Running Process or containers:**
```bash
    docker ps
```
<img src="" alt="Ubuntu" width="500px">
You were shecked beacuse we did not see any container is because currently no container is running in process

**Check Running Process or stop containers as well:**
```bash
    docker ps -a
```
<img src="" alt="Ubuntu" width="500px">
Now We can see stop containers as well, look we created ubuntu image with unique id 11 minutes ago.







