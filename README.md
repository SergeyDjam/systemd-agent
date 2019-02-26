# systemd-agent
Managing systemctl (STOP/START/RESTART) over TCP

Install:
1. ```git clone https://github.com/SergeyDjam/systemd-agent.git```

2. ```cd systemd-agent```

3. create user "systemd-agent"

```sudo useradd systemd-agent```

4. copy systemd-agent.sudoers to /etc/sudoers.d and rename in systemd-agent

```sudo cp systemd-agent.sudoers /etc/sudoers.d/systemd-agent```

5. copy systemd-agent.service to /lib/systemd/system

```sudo cp systemd-agent.service /lib/systemd/system```

6. copy systemd-agent.cfg.sample to /etc/ and rename in systemd-agent.cfg

```sudo cp systed-agent.cfg.sample /etc/systemd-agent.cfg```

```sudo vi /etc/systemd-agent.cfg```

Explore:

Start agent 
1. Sdandalone 

run ```./systemd-agent```

2. Service

```sudo systemctl start systemd-agent```

Example restart Tomcat 

```echo "restart" | nc 127.0.0.1 44044```

