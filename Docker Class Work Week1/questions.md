1. What is difference between bash and terminal?

2. What is docker?
It is isolated environment from host machine

3. What is docker tag?

4. Some docker command
   docker run ubuntu (Downloading ubuntu) from here
   docker run -it ubuntu (Interactive mode), so now will be inside terminal of docker
   exit (if you want to come back to your system terminal)
   docker run -it --entrypoint=bash python:3.13.11-slim (--entrypoint=bash, will take us to system terminal else we will be at terminal of python)
   docker ps -a (list of what and in what state) , (a lot of garbage can be there)
   docker ps -aq (return list of containers)
   docker rm `docker ps -aq` (remove container)

   Whenever you exit from container, and restart it and check did installtion exists from your previous run. You find nothing (Challange)

   use following image
   docker run -it python:3.13.11-slim

   Now connect the container to machine folder, and open it in a particular folder of machine file

   docker run -it  --rm  -v $(pwd)/test:/app/test --entrypoint=bash python:3.9.16-slim (Format of command)

   -v volumn and -rm remove container from system
   How to provide some state to docker
   The answer is volume





5. Python question what is apt   
    apt update
    apt install python3


  Tip: "" can help you when you arguments contain space 