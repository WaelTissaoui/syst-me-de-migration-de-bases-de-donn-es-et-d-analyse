# App fake data insertion 



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before using this code, you will need to have Docker installed on your machine. You can download Docker from the official website for your operating system:
link : (https://docs.docker.com/engine/install/ubuntu/)

Once you have Docker installed, you should be able to run the code using the instructions in the "Installation" and "Running the project" sections of this README

#### Installing

clone the project from the git repository

```

git clone : (https://gitlab.com/softbrain_digital/data-engineers/data-pipeline.git)

```

# Running the project
to build and run the containers :
get into the project folder and type :
```
sudo docker compose up --build

```

to access PGadmin web interface :
go to url http://localhost:5050 
MAIL=admin@admin.com  PASSWORD=root 
register a new server 
  at the ( General tap ) choose any name 
  at the connection tap :
      Host name/adresse : 172.20.0.3
      username : softbrain
      password : softbrain

```
 
## Built With

## Authors

👤 **Wael Tissaoui** 



