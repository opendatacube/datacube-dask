#! /usr/bin/env python3
from dask.distributed import Client
import click
import sys

@click.option("--port", default=8786)
@click.option("--timeout", default="2s")
@click.command()
def health(port, timeout):
    returncode = 1
    try:
        client = Client(f'tcp://localhost:{port}', timeout=timeout)
        returncode = 0
    except Exception:
        pass
    sys.exit(returncode)


if __name__ == "__main__":
    health()
