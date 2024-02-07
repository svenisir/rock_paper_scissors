import sys

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'formatter_1': {
            'format': '[{asctime}] #{levelname:8} {filename}:'
                      '{lineno} - {name}:{funcName} - {message}',
            'style': '{'
        },
        'formatter_2': {
            'format': '[{asctime}] #{levelname:8} {lineno}'
                      ' - {filename} - {name} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_2',
            'stream': sys.stdout
        },
        'warning_file': {
            'class': 'logging.FileHandler',
            'filename': 'warning.log',
            'mode': 'w',
            'formatter': 'formatter_1'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'mode': 'w',
            'formatter': 'formatter_1'
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': 'critical.log',
            'mode': 'w',
            'formatter': 'formatter_1'
        }
    },
    'loggers': {

    },
    'root': {
        'formatter': 'formatter_2',
        'handlers': ['stdout']
    }
}


