package JudgeWeb

import (
	"log"
	"net/http"
)

type router struct {
	handlers map[string] HandlerFunc
}

func newRouter() *router {
	return &router{handlers: make(map[string]HandlerFunc) }
}

func (r *router) addRoute(method string, pattern string, handler HandlerFunc) {
	log.Printf("Route %s -- %s",method, pattern)
	key := method + pattern
	r.handlers[key] = handler
}

func (r *router) Handler(c *Context){
	key := c.Method + c.Path
	if handler, ok := r.handlers[key]; ok {
		handler(c.Writer, c.Req)
	} else {
		c.String(http.StatusNotFound, "404 NOT FOUND %s\n",  c.Path)
	}
}