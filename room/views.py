from django.shortcuts import render, redirect, get_object_or_404
from player.models import Player
from django.urls import reverse
from room.models import Room
from questionandanswer.models import Response, Scoring

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('quiz_code')

        # Busca a sala do jogador
        room = get_object_or_404(Room, code=code)

        #Criar jogador associado a sala
        player = Player.objects.create(
            name=name,
            room=room
        )

        return redirect(reverse('room_detail', kwargs={'code': room.code, 'id_player':player.id})) # type: ignore
    return render(request, 'index.html')


def room_detail(request, code, id_player):
    room = get_object_or_404(Room, code=code)
    players = room.player.all()  # type: ignore
    current_player = get_object_or_404(Player, id=id_player)

    # Obtenha todas as perguntas na sala
    questions = room.question.all()  # type: ignore

    # Controle do índice da pergunta atual
    current_question_index = request.session.get('current_question_index', 0)

    # Se houver perguntas
    if current_question_index < len(questions):
        question = questions[current_question_index]
        responses = Response.objects.filter(question=question)

        # Inicializa a pontuação do jogador, se necessário
        if not hasattr(current_player, 'points'):
            current_player.points = 0  # Inicializa a pontuação
            current_player.save()

        if request.method == 'POST':
            selected_answer_id = request.POST.get('answer')
            if selected_answer_id:
                # Lógica para salvar a resposta e a pontuação
                response = get_object_or_404(Response, id=selected_answer_id)
                scoring = Scoring.objects.create(
                    user=current_player,
                    question=question,
                    response=response,
                    correct=response.correct,
                    points=1 if response.correct else 0  # Exemplo simples de pontuação
                )
                
                # Atualiza a pontuação do jogador
                current_player.points += scoring.points
                current_player.save()

                # Atualiza o índice da pergunta atual
                request.session['current_question_index'] = current_question_index + 1

                # Redireciona para a mesma view para mostrar a próxima pergunta
                return redirect('room_detail', code=code, id_player=id_player)

    else:
        # Reseta o índice se todas as perguntas já foram respondidas
        del request.session['current_question_index']
        question = None
        responses = None

    # Coletar pontuações de todos os jogadores
    players_scores = {player.id: player.points for player in players}
        
    return render(request, 'room_detail.html', {
        'room': room,
        'players': players,
        'response': responses,
        'question': question,
        'current_player': current_player,
        'players_scores': players_scores
    })