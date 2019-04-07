FROM python:3-alpine
LABEL Justin Cichra
ADD server.py /
EXPOSE 5555
CMD ["python","server.py"]
