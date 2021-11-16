# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from httplib2 import Http
import json
import time

hostName = "heroku-exemplo-servers-python.herokuapp.com"#app-name
serverPort = 8080




class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        #================== Recebemos o primeiro GET
        request_client = self.requestline
        ip = self.client_address[0]
        print("request: " + request_client)
        print(ip)

        # ====================Estamos a trabalhar no GET para o DOCKER
        h = Http()
        content_type=""
        with open("Server.txt", "r") as servers:
            for server in servers:
                uri="https://"
                uri+=server

                #header = h.request(uri,"HEAD")
                #content_type = header[0]['content-type'].split(';')[0]


                response,content = h.request(uri)
                print("content:",content)
                print("response:",response)


                if content_type == "text/html":
                    pass
                if content_type == "text/json":
                    pass

                #=============Response para o cliente
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                self.wfile.write(bytes(content))
                #self.send_response(response)
                break
        '''
        with open("myfile.json","w") as jsonFile:
            json.dump(self.Dados_to_Json("pedido1",ip,request_client),jsonFile)
            jsonFile.close()
  

       
        #Escreve no ficheiro o ip do cliente que fez o pedido
        #Se já existir esse ip lá, ignora
        existe = False
        try:
            f = open("Clientes.txt", "r")
            for line in f:
                if line == str(ip):
                    existe=True
                    break
                f.close()
                if existe == False:
                    f = open("Clientes.txt", "r")
                    conteudo = f.readlines()
                    conteudo.append(ip)
                    f.close()
                    f = open("Clientes.txt", "w")
                    f.writelines(conteudo)
                    f.close()
        except:
            f = open("Clientes.txt", "w")
            f.close()
    '''

'''
    def Dados_to_Json(self,nome,ip,pedido):
        s = {}
        return s

'''

if __name__ == "__main__":
    print("Hello World!")
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started https://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.") 
