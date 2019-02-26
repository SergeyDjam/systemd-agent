package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "os"
    "os/exec"
    "strings"
    "github.com/joho/godotenv"
)

type agentConfig struct {
        port    string
        unit	string
}


func main() {
    err := godotenv.Load("/etc/systemd-agent.cfg")
    if err != nil {
        log.Fatal("Error loading systemd-agent.cfg file")
    }

    cfg := agentConfig{ port: os.Getenv("PORT"), unit: os.Getenv("UNIT") }

    l, err := net.Listen("tcp", "127.0.0.1:"+cfg.port)

    if err != nil {
	log.Fatal(err)
    }

    defer l.Close()

    for {

	conn, err := l.Accept()

	if err != nil {
	    log.Fatal(err)
	}

	go func(c net.Conn) {

	    message, _ := bufio.NewReader(conn).ReadString('\n')

	    if strings.TrimRight(message, "\n") == "restart" {

	        fmt.Print("Command received: ", string(message))

		cmd := exec.Command("/usr/bin/sudo","/usr/bin/systemctl","restart",cfg.unit)

		err := cmd.Start()
                if err != nil {
                    log.Fatal(err)
                }


	    } else if strings.TrimRight(message, "\n") == "stop" {

		fmt.Print("Command received: ", string(message))

                cmd := exec.Command("/usr/bin/sudo","/usr/bin/systemctl","stop",cfg.unit)

                err := cmd.Start()
                if err != nil {
                    log.Fatal(err)
                }

	    } else if strings.TrimRight(message, "\n") == "start"{

		fmt.Print("Command received: ", string(message))

                cmd := exec.Command("/usr/bin/sudo","/usr/bin/systemctl","start",cfg.unit)

                err := cmd.Start()
                if err != nil {
                    log.Fatal(err)
                }
	    } else {

		fmt.Print("Command received: ", string(message))

	    }
	    c.Close()
	}(conn)
    }
}
