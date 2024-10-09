# download the officila version of pythotn
FROM python:3.9-slim

# we set the current directory as the working one 
WORKDIR /app

# install any required packages that were specified in requirements.txt
RUN pip install scapy

# copy all code from the project folder
COPY . .

# command to run the network sniffer script
CMD ["python","scapy_step1.py","scapy_step_2.py"]
