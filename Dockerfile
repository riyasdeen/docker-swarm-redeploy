from docker
RUN apk add --update \
		python \
		py-pip \
		&& pip install -r requirements.txt
ADD requirements.txt .
ADD runserver.py .
CMD ["python", "runserver.py"]