#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import requests
import time
import json
import prometheus_client
from prometheus_client import start_http_server, Metric, REGISTRY


class JsonCollector(object):
    def __init__(self):
        pass

    def collect(self):
        #Get the Json from st2 api

        st2_host = os.environ.get('ST2_HOST', 'http://localhost/')


        st2_api_key = os.environ.get('ST2_API_KEY')


        st2_host_url = st2_host.rstrip("/")
        headers = {'St2-Api-Key': st2_api_key }


        status = 'running'
        url = st2_host + '/api/v1/executions?status=' + status + '&parent=null'
        r = requests.get(url, headers=headers, verify=False)
        metric = Metric('jobs_running', 'Current Jobs Running', 'gauge')
        metric.add_sample('jobs_running', value=float(len(r.json())), labels={})
        yield metric

        status = 'failed'
        url = st2_host + '/api/v1/executions?status=' + status + '&parent=null'
        r = requests.get(url, headers=headers, verify=False)
        metric = Metric('jobs_failed', 'Number of failed jobs', 'gauge')
        metric.add_sample('jobs_failed', value=float(len(r.json())), labels={})
        yield metric

        status = 'succeeded'
        url = st2_host + '/api/v1/executions?status=' + status + '&parent=null'
        r = requests.get(url, headers=headers, verify=False)
        metric = Metric('jobs_succeeded', 'Number of failed jobs', 'gauge')
        metric.add_sample('jobs_succeeded', value=float(len(r.json())), labels={})
        yield metric


if __name__ == "__main__":
    start_http_server(8000)
    REGISTRY.register(JsonCollector())
    while True: time.sleep(1)
