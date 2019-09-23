## 编译proto

```
protoc -I . --go_out=plugins=grpc:. proto/hello.proto

```