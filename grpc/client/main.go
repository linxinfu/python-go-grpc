package main

import (
	"client/proto"
	"context"
	"fmt"
	"google.golang.org/grpc"
	"log"
)

func main() {
	conn, err := grpc.Dial("127.0.0.1:8098", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	t := hello.NewHelloWordClient(conn)

	resp, err := t.Hello(context.Background(), &hello.StringRequest{Param: "cxk"})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	fmt.Println("服务端返回: ", resp.Resp)
}
