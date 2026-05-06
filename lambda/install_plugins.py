import json
import urllib3

http = urllib3.PoolManager()

def handler(event, context):
    grafana_url = "https://your-grafana-url"
    api_key = "your-api-key"

    plugins = ["grafana-piechart-panel"]

    for plugin in plugins:
        url = f"{grafana_url}/api/plugins/{plugin}/install"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = http.request("POST", url, headers=headers)

    return {
        "statusCode": 200,
        "body": json.dumps("Plugins installed")
    }
