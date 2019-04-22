# portscanner_server
A python server that responds with open ports from the calling address

I was going to do this in C++ but I needed something quickly

Connect via a tcp connection, I'll send back JSON that tells you what ports you have open


## How to run a scan

```bash
telnet <server_ip> 5555
telnet>portscan
```
It will give you an interactive report scan

## Run in docker
```bash
docker run -d -p 5555:5555 --name=portscanner_server --hostname=portscanner_server jrcichra/portscanner_server:master
```
