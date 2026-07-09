import os
import json
import pymysql
from secrets_helper import get_secret


def lambda_handler(event, context):
    secret_name = os.environ['SECRET_NAME']
    creds = get_secret(secret_name)

    connection = None
    try:
        connection = pymysql.connect(
            host=creds['host'],
            user=creds['user'],
            password=creds['password'],
            db=creds['database'],
            connect_timeout=5
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM alumnos;")
            results = cursor.fetchall()

        return {
            "statusCode": 200,
            "body": json.dumps(results, default=str)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
    finally:
        if connection:
            connection.close()