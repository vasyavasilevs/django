from django.shortcuts import render
from .forms import EnglishTestForm
from .models import Tutor, EnglishLevel


def index(request):
    """
    Renders the main index page of the site.
    """
    return render(request, 'main/index.html')

def anna(request):
    """
    Renders the profile page of tutor Anna Ivanova.
    """
    return render(request, 'main/ivanova.html')

def mikhail(request):
    """
    Renders the profile page of tutor Mikhail Smirnov.
    """
    return render(request, 'main/smirnov.html')

def ekaterina(request):
    """
    Renders the profile page of tutor Ekaterina Li.
    """
    return render(request, 'main/li.html')

def english_test_view(request):
    """
    Handles the English level test form.

    If the request method is POST, it evaluates the submitted answers,
    calculates the score, determines the user's English level,
    and returns a list of tutors who teach at that level.

    If the request is GET, it renders the test form.
    """
    if request.method == 'POST':
        form = EnglishTestForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data
            score = 0

            if answers['question1'] == 'an':
                score += 1
            if answers['question2'] == 'goes':
                score += 1
            if answers['question3'] == 'in':
                score += 1
            if answers['question4'] == 'She can sing well.':
                score += 1
            if answers['question5'] == 'had':
                score += 1
            if answers['question6'] == 'The cake is eaten by him.':
                score += 1
            if answers['question7'] == 'were':
                score += 1
            if answers['question8'] == 'is reading':
                score += 1
            if answers['question9'] == 'Although it was raining, we went for a walk.':
                score += 1
            if answers['question10'] == 'attend':
                score += 1

            if score >= 8:
                level_code = 'C1'
            elif score >= 6:
                level_code = 'B2'
            elif score >= 4:
                level_code = 'B1'
            elif score >= 2:
                level_code = 'A2'
            else:
                level_code = 'A1'

            level = EnglishLevel.objects.get(name=level_code)
            tutors = Tutor.objects.filter(level=level)

            return render(request, 'main/results.html', {
                'level': level,
                'tutors': tutors
            })
    else:
        form = EnglishTestForm()

    return render(request, 'main/test.html', {'form': form})
