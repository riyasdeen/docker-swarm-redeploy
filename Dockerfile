FROM docker
ADD requirements.txt .
RUN apk add --update \
		python \
		py-pip \
		&& pip install -r requirements.txt
ADD runserver.py .
CMD ["python", "runserver.py"]