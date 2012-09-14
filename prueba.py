

if __name__ == '__main__':
    import json
    json_data=open('datos.json')
    data = json.load(json_data)
    json_data.close()
#    data['mensajes']
    data['mensajes'].append("chao")
    print json.dumps(data)