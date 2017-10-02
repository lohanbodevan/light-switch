# Light Switch
The goal of this project is provide some automation for instances that have to be turned on and turned off regularly.

## Description
The application will look for instances id in `instances.json` file. With these instances id, the application will  
get each instance state and change to the oposite. If the instance state is `stoppend` the application will change to `running`.  
If the instance state is `running` the application will change to `stopped`.  

## Cloud Services Available
* AWS

## Dependencies
* Python 3

## Configurations
### Env vars
Configure credentials and region in `.env` file. See example in `.env.sample`

### Instances file
Configure yout instances id in `instances.json`. See example in `instances.json.default`

## Setup application
```
make setup
```

## Run
```
make run
```

## TODO
* Prepare for another cloud services
