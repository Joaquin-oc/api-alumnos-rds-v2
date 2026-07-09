import json
import boto3

_sm_client = boto3.client('secretsmanager')
_cache = {}


def get_secret(secret_name):
    if secret_name in _cache:
        return _cache[secret_name]

    response = _sm_client.get_secret_value(SecretId=secret_name)
    secreto = json.loads(response['SecretString'])
    _cache[secret_name] = secreto
    return secreto


def invalidar_cache(secret_name=None):
    if secret_name:
        _cache.pop(secret_name, None)
    else:
        _cache.clear()