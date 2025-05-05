from flask import Flask, render_template, request
app = Flask(__name__)

# Perguntas do questionário (15 perguntas, 5 opções cada)
perguntas = [
    {
        "id": 1,
        "texto": "Em um dia especial, o que te faz sentir mais amado(a)?",
        "opcoes": [
            {"texto": "Receber um abraço caloroso ou um toque carinhoso.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras sinceras de carinho ou elogio.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo de qualidade juntos, sem distrações.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo especial para te ajudar.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente escolhido com cuidado.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 2,
        "texto": "O que te faz sentir mais valorizado(a) no dia a dia?",
        "opcoes": [
            {"texto": "Pequenos gestos de carinho físico, como segurar a mão.", "linguagem": "Toque Físico"},
            {"texto": "Receber uma mensagem de apoio ou gratidão.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo juntos fazendo algo que você gosta.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém te ajuda com uma tarefa sem pedir.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente surpresa, mesmo que simples.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 3,
        "texto": "O que te deixa mais feliz em um relacionamento?",
        "opcoes": [
            {"texto": "Sentir um toque afetuoso, como um abraço ou cafuné.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que reconhecem seus esforços.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Planejar um momento especial juntos, como um passeio.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo prático para facilitar sua vida.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que reflete seu gosto.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 4,
        "texto": "Em um momento difícil, o que te faz sentir mais apoiado(a)?",
        "opcoes": [
            {"texto": "Um abraço reconfortante ou toque carinhoso.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras de encorajamento e apoio.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Alguém passar tempo te ouvindo atentamente.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém te ajuda a resolver um problema.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que mostra que pensaram em você.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 5,
        "texto": "O que te faz sentir mais próximo(a) de alguém?",
        "opcoes": [
            {"texto": "Um momento de carinho físico, como um beijo.", "linguagem": "Toque Físico"},
            {"texto": "Receber uma mensagem carinhosa ou elogio.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Uma conversa longa e significativa.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo para te surpreender.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que mostra que te conhecem.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 6,
        "texto": "Qual gesto te faz sentir mais especial?",
        "opcoes": [
            {"texto": "Um toque carinhoso em um momento inesperado.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que mostram que você é importante.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar um dia inteiro juntos, sem pressa.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo que você precisava.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente feito à mão ou personalizado.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 7,
        "texto": "O que te faz sorrir mais em um dia comum?",
        "opcoes": [
            {"texto": "Pequenos toques afetuosos, como um abraço rápido.", "linguagem": "Toque Físico"},
            {"texto": "Receber um elogio inesperado.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Fazer algo simples juntos, como assistir a um filme.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém te ajuda com algo sem esperar nada.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presentinho que alegra seu dia.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 8,
        "texto": "O que te faz sentir mais cuidado(a)?",
        "opcoes": [
            {"texto": "Sentir um toque carinhoso, como segurar a mão.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que expressam gratidão por você.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Alguém dedicar tempo para estar com você.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo para facilitar sua rotina.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que mostra atenção.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 9,
        "texto": "O que te faz sentir mais amado(a) em uma ocasião especial?",
        "opcoes": [
            {"texto": "Um abraço longo ou toque afetuoso.", "linguagem": "Toque Físico"},
            {"texto": "Receber palavras emocionadas ou um discurso carinhoso.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo de qualidade, como um jantar especial.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém organiza algo para te surpreender.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que você sempre quis.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 10,
        "texto": "O que te faz sentir mais conectado(a) emocionalmente?",
        "opcoes": [
            {"texto": "Um toque físico, como um cafuné ou abraço.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que mostram que te entendem.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo juntos em uma atividade significativa.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo para te apoiar.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que reflete sua personalidade.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 11,
        "texto": "O que te faz sentir mais querido(a) no dia a dia?",
        "opcoes": [
            {"texto": "Gestos de carinho físico, como um beijo rápido.", "linguagem": "Toque Físico"},
            {"texto": "Receber uma mensagem de carinho ou apoio.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo juntos, mesmo em momentos simples.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém te ajuda com uma tarefa diária.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente pequeno, mas significativo.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 12,
        "texto": "O que te faz sentir mais apoiado(a) em um desafio?",
        "opcoes": [
            {"texto": "Um toque reconfortante, como um abraço apertado.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que te motivam a continuar.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Alguém passar tempo te ajudando a pensar em soluções.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo prático para te ajudar.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que levanta seu ânimo.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 13,
        "texto": "O que te faz sentir mais especial em um relacionamento?",
        "opcoes": [
            {"texto": "Toques carinhosos, como segurar a mão ou um abraço.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que mostram que você é valorizado(a).", "linguagem": "Palavras de Afirmação"},
            {"texto": "Planejar um momento só para vocês dois.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo para te surpreender.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que foi escolhido com carinho.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 14,
        "texto": "O que te faz sorrir mais em um momento inesperado?",
        "opcoes": [
            {"texto": "Um toque afetuoso, como um beijo surpresa.", "linguagem": "Toque Físico"},
            {"texto": "Receber um elogio ou mensagem carinhosa.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo juntos em uma atividade espontânea.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo gentil sem você esperar.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presentinho que alegra seu dia.", "linguagem": "Presentes"}
        ]
    },
    {
        "id": 15,
        "texto": "O que te faz sentir mais amado(a) em um momento comum?",
        "opcoes": [
            {"texto": "Pequenos gestos de carinho físico, como um abraço.", "linguagem": "Toque Físico"},
            {"texto": "Ouvir palavras que mostram que se importam com você.", "linguagem": "Palavras de Afirmação"},
            {"texto": "Passar tempo de qualidade, como uma conversa tranquila.", "linguagem": "Tempo de Qualidade"},
            {"texto": "Quando alguém faz algo para facilitar seu dia.", "linguagem": "Atos de Serviço"},
            {"texto": "Receber um presente que demonstra atenção.", "linguagem": "Presentes"}
        ]
    }
]

# Rota para exibir o questionário
@app.route('/')
def index():
    return render_template('questionario.html', perguntas=perguntas)

# Rota para processar as respostas
@app.route('/resultado', methods=['POST'])
def resultado():
    pontuacao = {
        "Toque Físico": 0,
        "Palavras de Afirmação": 0,
        "Tempo de Qualidade": 0,
        "Atos de Serviço": 0,
        "Presentes": 0
    }
    
    # Contar pontos com base nas respostas
    for i in range(1, len(perguntas) + 1):
        resposta = request.form.get(f'pergunta_{i}')
        if resposta:
            for pergunta in perguntas:
                if pergunta['id'] == i:
                    for opcao in pergunta['opcoes']:
                        if opcao['texto'] == resposta:
                            pontuacao[opcao['linguagem']] += 1
    
    # Determinar a linguagem predominante
    linguagem_predominante = max(pontuacao, key=pontuacao.get)
    
    return render_template('questionario.html', perguntas=perguntas, resultado=linguagem_predominante, pontuacao=pontuacao)

if __name__ == '__main__':
    app.run(debug=True)