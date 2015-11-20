# a simple html server
import
  jester, asyncdispatch, htmlgen

routes:
  get "/":
    # resp h1("Hello world")
    resp "Hello, world!"

runForever()
