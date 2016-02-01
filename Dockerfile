FROM python:2.7.9
ADD . /Jigglypuff

RUN pip install falcon gunicorn
RUN git clone https://$USERNAME:$PASSWORD@github.com/calpeyser/Sebastian.git
RUN cd /Sebastian && python setup.py install

EXPOSE 8080
CMD cd /Jigglypuff && gunicorn --bind 0.0.0.0:8080 server