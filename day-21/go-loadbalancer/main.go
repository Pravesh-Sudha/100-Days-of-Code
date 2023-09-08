package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
	"net/url"
	"os"
)

func main(){
	servers := []Server{
		newSimpleServer("https://www.facebook.com"),
		newSimpleServer("https://www.google.com"),
		newSimpleServer("https://www.yahoo.com"),
	}

	lb := newLoadBalancer("8000", servers)
	handleRedirect := func(rw http.ResponseWriter, req *http.Request){
		lb.serverProxy(rw, req)
	}
		http.HandleFunc("/", handleRedirect)
		fmt.Printf("Server is hosting at port %s\n" , lb.port)
		http.ListenAndServe(":" + lb.port, nil)

	}

type Server interface {
	Addresss() string
	IsAlive() bool
	Serve(rw http.ResponseWriter, r *http.Request) 	
}

type simpleServer struct {
	addr string
	proxy *httputil.ReverseProxy
}

type LoadBalancer struct {
	port 			  string
	roundRobinCount   int
	servers 		  []Server
}

func newSimpleServer (addr string) *simpleServer {
	serverUrl , err := url.Parse(addr)
	handleError(err)

	return &simpleServer{
		addr: addr,
		proxy: httputil.NewSingleHostReverseProxy(serverUrl),
	}
}

func (s *simpleServer) Addresss() string {return s.addr}

func (s *simpleServer) IsAlive() bool {return true}

func (s *simpleServer) Serve(rw http.ResponseWriter, req *http.Request){
	s.proxy.ServeHTTP(rw, req)
}

func (lb *LoadBalancer) getNextAvailableServer() Server{
	server := lb.servers[lb.roundRobinCount%len(lb.servers)]
	for !server.IsAlive(){
		lb.roundRobinCount++
		server = lb.servers[lb.roundRobinCount%len(lb.servers)]
	}
	lb.roundRobinCount++
	return server	
}

func (lb *LoadBalancer) serverProxy(rw http.ResponseWriter, r *http.Request){
	targetServer := lb.getNextAvailableServer()
	fmt.Printf("Forwarding request to the address: %q\n", targetServer.Addresss())
	targetServer.Serve(rw, r)
}



func newLoadBalancer(port string, servers []Server) *LoadBalancer{
	return &LoadBalancer{
		port: port,
		roundRobinCount: 0,
		servers: servers,
	}
}

func handleError(err error){
	if err != nil {
		fmt.Printf("error : %v", err)
		os.Exit(1)
	}
}
