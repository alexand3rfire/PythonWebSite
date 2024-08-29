from django.shortcuts import render
from .models import Test, Question, Answer

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Сайт Wcclub',
    	'content': 'интернет-сайт каналов разных пользователей',
		'date_posted': '28 декабря 2023'

	},
	{
    	'author': 'Администратор',
    	'title': 'канал музыки',
    	'content': 'Рок-канал.',
		'date_posted': '28 декабря 2023'

	}
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'wcclub/home.html', context)

def test(request):
	num_question = 0
	correctAnswers = 0
	if request.method == 'POST':
		answer = request.POST.get('answer', '')
		num_question = int(request.POST.get('numQuestion', 0))
		correctAnswers = int(request.POST.get('corrects', 0))
		correctLetter = request.POST.get('letter', '')
		if correctLetter == answer:
			correctAnswers += 1

		num_question += 1

	test = Test.objects.get(id=1)
	questions = Question.objects.all()[num_question:num_question + 1]
	if questions:
		answers = Answer.objects.filter(question_id = questions[0].id)
	else:
		context = {
			'message': 'Вы набрали баллов: ' + str(correctAnswers),
		}
		return render(request, 'wcclub/finish.html', context)

	context = {
		'test': test,
		'questions': questions,
		'answers': answers,
		'correct_letter': questions[0].correct,
		'num_question': num_question,
		'correct_answers': correctAnswers
	}
	return render(request, 'wcclub/test.html', context)

def channel(request):
	context = { 'title': 'WCClub', }
	return render(request, 'wcclub/channel.html', context)

def about(request):
	context = {}
	return render(request, 'wcclub/about.html', context)

def contact(request):
	context = {}
	return render(request, 'wcclub/contact.html', context)





