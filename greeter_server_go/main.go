/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

// Package main implements a server for Greeter service.
package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"time"

	pb "bomei/comtrade-gopy/helloworld"

	"google.golang.org/grpc"
)



const (
	port = ":50051"
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedGreeterServer
}

// SayHello implements helloworld.GreeterServer
func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	log.Printf("Received: %v", in.GetName())
	return &pb.HelloReply{Message: "Hello " + in.GetName()}, nil
}

func (s *server) TestFastLoad(ctx context.Context, in *pb.HelloRequest) (*pb.Analog, error) {
	log.Printf("Received: %v", in.GetName())
	fmt.Println("hello, world.")
	fmt.Println(time.Now())
	analog,_,_:=Test()
	fmt.Println(time.Now())
	ac := pb.Analog{}
	for i :=range analog{
		ch :=pb.AnalogChannel{Value: analog[i]}
		ac.Channel = append(ac.Channel, &ch)
	}
	return &ac,nil
}

func (s *server) FastLoad(ctx context.Context,in *pb.DatParseParam) (*pb.WaveDataReply, error){
	log.Printf("Received: %v",in.GetDatFile())
	wave := pb.WaveDataReply{}
	datFile := in.GetDatFile()
	timeMult := in.GetTimeMult()
	timeBase := in.GetTimeBase()
	aChannels:=in.GetAchannels()
	sChannels := in.GetSchannels()

	a:=in.GetA()
	b:=in.GetB()
	groupsOf16bits := in.GetGroupsOf16Bits()
	totalSamples := in.GetTotalSample()

	timestampCritical := in.GetTimestampCritical()
	sampleRate := in.GetSampleRate()
	cfgSampleRate := [][]int32{}
	for i := range sampleRate{
		rate := sampleRate[i].GetSampleRateRow()
		cfgSampleRate = append(cfgSampleRate, rate)
	}

	log.Printf(datFile,timeMult,timeBase,aChannels,sChannels,a,b,groupsOf16bits,totalSamples,timestampCritical,cfgSampleRate)

	// analog, status, t := Parse(datFile,timeMult,timeBase,aChannels,sChannels,a,b,groupsOf16bits,
	// 	totalSamples,timestampCritical,cfgSampleRate)	
	// ac := pb.Analog{}
	// sc := pb.Status{}
	// tc := pb.Time{Value:t}
	// for i :=range analog{
	// 	ch :=pb.AnalogChannel{Value: analog[i]}
	// 	ac.Channel = append(ac.Channel, &ch)

	// 	sch := pb.StatusChannel{Value: status[i]}
	// 	sc.Channel = append(sc.Channel, &sch)
	// }

	// wave = pb.WaveDataReply{Analog: &ac,Status: &sc,T:&tc}

	

	return &wave,nil
}

func main() {

	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
