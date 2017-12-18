import requests
import json
class YadageHTTPController():
    def __init__(self, server):
        self.server = server

    @property
    def adageobj(self):
        return None

    def applicable_rules(self):
        return requests.get(self.server + '/ctrl/read/applicable_rules').json()

    def submittable_nodes(self):
        return requests.get(self.server + '/ctrl/read/submittable_nodes').json()

    def apply_rules(self, ruleids):
        requests.post(
            self.server + '/ctrl/write/apply_rules',
            headers = {'Content-Type': 'application/json'},
            data = json.dumps({'ruleids': ruleids})
        )

    def submit_nodes(self, nodeids):
        requests.post(
            self.server + '/ctrl/write/submit_nodes',
            headers = {'Content-Type': 'application/json'},
            data = json.dumps({'nodeids': nodeids})
        )

    def finished(self):
        return requests.get(self.server + '/ctrl/read/finished').json()

    def validate(self):
        return requests.get(self.server + '/ctrl/read/validate').json()

    def successful(self):
        return requests.get(self.server + '/ctrl/read/successful').json()
