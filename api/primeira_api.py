from flask import Flask, jsonify

app = Flask(__name__)

postagens = [
    {
        'nome': 'Tácio',
        'idade': '31'
    },
    {
        'nome': 'Johnny',
        'idade': '34'
    },
    {
        'nome': 'Chris',
        'idade': '24'
    }
]

#print(len(postagens))
# Rota padrão GET http://localhost:5001/
@app.route('/')
def obter_postagens():
    response = jsonify(postagens)
    return response

@app.route('/postagens/<int:indice>',methods=['GET'])
def obter_postagem_por_id(indice):
    if indice >= 0 < len(postagens):
        response_get = jsonify(postagens[indice],200)
    
        return response_get
    else:
        return jsonify()

app.run(port=5001, host='localhost', debug=True)