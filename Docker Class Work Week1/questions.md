Summery of story:
We make docker so every member in team can reproduce same environment, to avoid conflicts and to spend time efficiently. 
There are many challanges that we may have to come accorss:
1. Loss of memory from docker
2. Unused Docker occupying memory in system
3. Moving undockerized project to a dockerized system





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

  #There  will be three kind of environments:
  1. Your machine level
  2. Project level
  3. Docker level
  4. Sometimes you will start a project without docker (Task is how to move unconternized docker)

  With python these days we are using Uv command
  uv init
  uv add pandas 
  uv init 3.13
  uv run python -V


Making a folder for python project and then moving to it

uv init docker2
cd docker2

Now creating your virtual environment
uv python pin 3.13


then conforming virtual environment
uv run python -V

# BUILDING A CONTAINER FROM DOCKER file
docker build -t test:pandas .
