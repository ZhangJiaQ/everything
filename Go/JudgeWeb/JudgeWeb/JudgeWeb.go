package JudgeWeb

import (
	"net/http"
)

type HandlerFunc func(http.ResponseWriter, *http.Request)

type Engine struct {
	router *router
}

func New() *Engine {
	return &Engine{
		router: newRouter(),
	}
}

func (engine *Engine) addRoute(method string, pattern string, handler HandlerFunc){
	engine.router.addRoute(method, pattern, handler)
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
	c := newContext(w, req)
	engine.router.Handler(c)
}