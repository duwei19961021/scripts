//接收alertmanager的告警信息，进行处理后发送到钉钉机器人
package main

import (
        "fmt"
        "net"
        "strings"
)

func process(conn net.Conn)  {
        defer conn.Close()
        for {
                buf := make([]byte,102400)
                n,err := conn.Read(buf) //从conn读取
                if err != nil{
                        fmt.Println("server,read!",err)
                        return
                }
                //显示客户端发送的内容
                data := string(buf[:n])
                newdata := strings.Split(data,"POST")[0]
                fmt.Print(newdata)
        }
}

func main() {
        listen,err := net.Listen("tcp","0.0.0.0:5000")
        if err != nil{
                fmt.Println("listen err!",err)
                return
        }
        defer listen.Close()
        for {
                conn,err  := listen.Accept()
                if err != nil {
                        fmt.Println("accept error!",err)
                }
                go process(conn)
        }
        fmt.Println(listen)
}
