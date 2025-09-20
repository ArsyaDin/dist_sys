import requests
import json

# Fungsi untuk memanggil RPC
def call_rpc(method, params):
    # Use docker compose service name for internal networking
    url = "http://rpc-server:4000"
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response

result_add = call_rpc("add", [10, 2])
print(f"Result of add: {result_add['result']}")

result_multiply = call_rpc("multiply", [10, 10])
print(f"Result of multiply: {result_multiply['result']}")

result_sub = call_rpc("subtract", [10, 7])
print(f"Result of subtract: {result_sub['result']}")

result_divide = call_rpc("divide", [100, 5])
print(f"Result of divide: {result_divide['result']}")
