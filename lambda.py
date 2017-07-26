from json import JSONEncoder
from botocore.vendored import requests


def lambda_handler(event, context):
    # TODO implement

    uid = event.get("dev", None)
    token = event.get("token", None)

    print("r token:{} from dev:{}".format(uid, token))

    requests.post("http://54.255.182.198:5000/gates_status", json=JSONEncoder().encode(event))
