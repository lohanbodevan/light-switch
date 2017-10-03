# Light Switch
The goal of this project is to provide some automation for instances that have to be turned on and turned off regularly.

## Description
The application will look for instances ids in `instances.json` file. With these instances ids, the application will  
get each instance state and change to the oposite. If the instance state is `stoppend` the application will change to `running`.  
If the instance state is `running` the application will change to `stopped`.  

## Cloud Services Available
* AWS

## Requirements
* Python 3.6
* [Serverless](https://serverless.com/)

## Configurations
### Env vars
Configure your env vars in `serverless.yml` file in `custom` section.  
The schedule configuration is also in `serverless.yml` file.

### Instances file
Configure yout instances ids in `instances.json`. See example in `instances.json.default`

## Using Serverless
### Install
```
npm install -g serverless
```

### Deploy to Cloud
```
sls deploy
```

Obs.: You must configure your [credentials](http://docs.aws.amazon.com/cli/latest/topic/config-vars.html) to work with `serverless`.

## Run tests
```
make run-tests
```

## TODO
* Prepare for another cloud services
