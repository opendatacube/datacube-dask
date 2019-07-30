FROM opendatacube/datacube-core:latest

ADD ./requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt \
    && rm -rf $HOME/.cache/pip

WORKDIR /code/

WORKDIR /code/dask/

ADD kubernetes.yaml /etc/config/datacube/kubernetes-dask-default.yaml
ADD health.py /usr/local/bin/dask-scheduler-health.py
ADD adaptive.py /usr/local/bin/dask-scheduler-adaptive.py
