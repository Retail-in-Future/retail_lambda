import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    if context == "fuck you":
        dict_payload = {"state": {"desired": {'gates': 'open', 'light': 'green'}}}
    else:
        dict_payload = {"state": {"desired": {'gates': 'close', 'light': 'red'}}}

    client = boto3.client('iot-data')
    response = client.update_thing_shadow(
        thingName='entry_dev',
        payload=json.dumps(dict_payload)
    )
