__author__ = 'stone'
#encoding:utf-8
#File:order.py
import web
from web.contrib.template import render_mako

urls = (
        '/order/(.*)','order'
        )

app = web.application(urls,globals(),autoreload=True)

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories = ['templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
        )

class order:
    def GET(self,contactid):
        return render.order(contactid = contactid)
        # Another way:
        #return render.order(**locals())

if __name__ == "__main__":
    app.run()
