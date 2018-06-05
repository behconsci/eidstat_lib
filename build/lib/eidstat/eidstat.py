import grequests
import requests


class Stat(object):
    def __init__(self, token):
        self.url = 'http://eidstat.com/watch/event/%s/' % token

        # keep alive and connection pooling
        self.session = requests.session()

    def watch(self, event_name, extra=None):
        payload = {'name': event_name, 'extra': extra}
        req_ = [grequests.post(self.url, session=self.session, json=payload)]
        grequests.map(req_)
