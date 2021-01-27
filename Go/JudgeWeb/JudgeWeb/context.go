package JudgeWeb

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type H map[string]interface{}

type Context struct {
	Writer http.ResponseWriter
	Req *http.Request
	Path string
	Method string
	StatusCode int
}


func newContext(w http.ResponseWriter, req *http.Request) *Context{
	return &Context{
		Writer: w,
		Req: req,
		Path: req.URL.Path,
		Method: req.Method,
	}
}


func (c *Context) PostForm (key string) string {
	return c.Req.FormValue(key)
}

func (c *Context) Query (key string) string {
	return c.Req.URL.Query().Get(key)
}

func (c *Context) Status(code int) {
	c.StatusCode = code
	c.Writer.WriteHeader(code)
}

func (c *Context) SetHeader(key, value string) {
	c.Writer.Header().Set(key, value)
}

func (c *Context) String(code int, format string, value ...interface{}) {
	c.SetHeader("Content-type", "text/plain")
	c.Status(code)
	if _, err := c.Writer.Write([]byte(fmt.Sprintf(format, value...))); err != nil {
		http.Error(c.Writer, err.Error(), 500)
	}
}


func (c *Context) Json(code int, obj interface{}) {
	c.SetHeader("Content-type", "application/json")
	c.Status(code)
	encoder := json.NewEncoder(c.Writer)
	if err := encoder.Encode(obj); err != nil {
		http.Error(c.Writer, err.Error(), 500)
	}
}

func (c *Context) Data(code int, data []byte) {
	c.Status(code)
	if _, err := c.Writer.Write(data); err != nil {
		http.Error(c.Writer, err.Error(), 500)
	}
}

func (c *Context) Html(code int, html string){
	c.Status(code)
	c.SetHeader("Content-type", "text/html")
	if _, err := c.Writer.Write([]byte(html)); err != nil {
		http.Error(c.Writer, err.Error(), 500)
	}
}
