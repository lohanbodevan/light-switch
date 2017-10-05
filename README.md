# Light Switch <a href="https://travis-ci.org/lohanbodevan/light-switch"><img alt="Travis Status" src="https://travis-ci.org/lohanbodevan/light-switch.svg?branch=master"></a>
Toggle your [EC2](https://aws.amazon.com/ec2/) instance to start or stop without have to configure and mantain cron jobs.  
The goal of this project is to provide some automation for instances that have to be turned on and turned off regularly.  
This project is a simple [serverless](https://en.wikipedia.org/wiki/Serverless_computing) application prepread to run with [AWS Lambda](https://aws.amazon.com//lambda)  

## How it Works
The application will look for instances ids in `instances.json` file. With these instances ids, the application will  
get each instance state and change to the oposite. For example, if the instance state is `running` the application will change to `stopped`  
based on a schedule previously configured.

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
Configure your instances ids in `instances.json`. See example in `instances.json.default`

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
make tests
```

## TODO
* Prepare for others cloud services
