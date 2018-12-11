#! /usr/bin/env python3

import dask
from dask_kubernetes import KubeCluster
from time import sleep
import click
import logging
import sys
import signal

logger = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def adaptive():
    keep_running = True
    def sigterm_handler():
        keep_running = False

    signal.signal(signal.SIGTERM, sigterm_handler)
    min_pods = dask.config.get('kubernetes.count.min')
    if min_pods is None:
        min_pods = 0
    with KubeCluster() as cluster:
        cluster.adapt(minimum=min_pods)
        while keep_running:
            sleep(0)

if __name__ == "__main__":
    adaptive()