from ssl import wrap_socket
import justpy as jp

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")
    pi = jp.QDiv(a = wp, text = "These graphs represnt course review analysis")

    return wp 

jp.justpy(app)
