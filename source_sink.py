import os.path

# tornado imports
import tornado.ioloop
import tornado.options
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

app = tornado.web.Application(
    handlers=[(r'/', MainHandler),
    (r'/(.*)', tornado.web.StaticFileHandler,
        {'path': os.path.dirname(__file__)})],
    debug=True
    )

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
