import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        try:
            import json
            json_data = open('datos.json')
            data = json.load(json_data)
            json_data.close()
            self.response.write(json.dumps(data))
            self.response.headers['Content-Type'] = 'application/json'
        except Exception:
            self.response.status = 404
        
    def post(self):
        try:
            import json
            json_data = open('datos.json')
            data = json.load(json_data)
            json_data.close()
            mensaje = self.request.POST['mensaje']
        except Exception:
            mensaje = {"mensajes":[]}
        try:
            if self.request.headers['Content-Type'] == 'application/json':
                data = json.loads(mensaje)
                data['mensajes'].append(mensaje_json)
            else:
                data['mensajes'].append(mensaje)
                
            with open('datos.json', 'w') as f:
                f.write(json.dumps(data))
            self.response.write("Mensaje archivado")
        except Exception:
            self.response.write("No hay mensaje")
            
        

        
app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')
    
if __name__ == '__main__':
    main()
