# Light Switch <a href="https://travis-ci.org/lohanbodevan/light-switch"><img alt="Travis Status" src="https://travis-ci.org/lohanbodevan/light-switch.svg?branch=master"></a> [![Coverage Status](https://coveralls.io/repos/github/lohanbodevan/light-switch/badge.svg)](https://coveralls.io/github/lohanbodevan/light-switch)
Toggle your [EC2](https://aws.amazon.com/ec2/) and [RDS](https://aws.amazon.com/rds/) instances to start or stop without having to configure and mantain cron jobs.  
The goal of this project is to provide some automation for instances that have to be turned on and off regularly (eg. development or staging envinronments).  
This project is a simple [serverless](https://en.wikipedia.org/wiki/Serverless_computing) application prepread to run with [AWS Lambda](https://aws.amazon.com//lambda)  

## How it Works
This application will look for EC2 instances ids in `instances.json` and RDS instaces ids in `rds_instances.json` file. With these ids, the application will  
get each instance state and change to the oposite.  
For example, if the instance state is `running` the application will change to `stopped` based on a schedule previously configured.

## Cloud Services Available
* AWS

## Requirements
* Python 3.6
* [Serverless](https://serverless.com/)

## Configurations
### Env vars
Configure your env vars in `serverless.yml` file in `custom` section.  
The schedule configuration is also in `serverless.yml` file.

### EC2 Instances file
Configure your EC2 instances ids in `instances.json`. See example in `instances.json.default`

### RDS Instances file
Configure your RDS instances ids in `rds_instances.json`. See example in `rds_instances.json.default`

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
