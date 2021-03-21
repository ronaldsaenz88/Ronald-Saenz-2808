# Ronald-Saenz-2808

Test Ronald Saenz

## Usage

You must clone the project in the web server

HTTPS o SSH:
```bash
git clone https://github.com/ronaldsaenz88/Ronald-Saenz-2808.git
git clone git@github.com:ronaldsaenz88/Ronald-Saenz-2808.git
```

You must create the MONGODB database in the Cloud: https://cloud.mongodb.com/

Next, you should configure the settings.py file based on the settings_sample.py file. 
You should replace the values on [variables]
```bash
DATABASES = {
    'default' : {
        'ENGINE': 'djongo',
        'NAME': '[BD]',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://[USER]:[PASSWORD]@[HOST]/[BD]?retryWrites=true&w=majority',
            'port': 27017,
            'username': '[USER]',
            'password': '[PASSWORD]',
            'authSource': '[BD]',
            'authMechanism': 'SCRAM-SHA-1'
        },
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,                        
                }
            },
        },
    }
}
```

## TESTING

To run the test on the project you need to execute:

```bash
coverage run manage.py test
coverage report  
```

## RUN

To run this example you need to execute:

```bash
pip3 install --upgrade pip
pip3 install -r ./requirements.txt
python3 ./manage.py runserver
```

## API DOCUMENTATION

To read the API Documentation, you can find on the "openapi" folder.
This folder containg the specifications to show the preview on Swagger.


## Requirements

| Name | Version |
|------|---------|
| python | >= 3.6 |

## Authors

Module managed by [Ronald Saenz](https://github.com/ronaldsaenz88).

## License

GNU General Public Licensed. See LICENSE for full details.