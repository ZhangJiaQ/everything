package JudgeWeb

import (
	"fmt"
	"net/http"
)

type HandlerFunc func(http.ResponseWriter, *http.Request)

type Engine struct {
	router map[string] HandlerFunc
}

func New() *Engine {
	return &Engine{
		router: make(map[string] HandlerFunc),
	}
}

func (engine *Engine) addRoute(method string, pattern string, handler HandlerFunc){
	key := method + "_" + pattern
	engine.router[key] = handler
}


func (engine *Engine) Get(pattern string, handler HandlerFunc){
	engine.addRoute("GET", pattern, handler)
}


func (engine *Engine) Post(pattern string, handler HandlerFunc){
	engine.addRoute("Post", pattern, handler)
}


func (engine *Engine) Put(pattern string, handler HandlerFunc){
	engine.addRoute("Put", pattern, handler)
}


func (engine *Engine) Delete(pattern string, handler HandlerFunc){
	engine.addRoute("Delete", pattern, handler)
}


func (engine *Engine) Run(addr string) error{
	return http.ListenAndServe(addr, engine)
}

func (engine *Engine) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	key := req.Method + "_" + req.URL.Path
	if handler, ok := engine.router[key]; ok {
		handler(w, req)
	} else {
		fmt.Fprintf(w, "404 NOT FOUND: %s\n", req.URL)
	}
}