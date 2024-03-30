from django import forms

class RandomGames(forms.Form):
    games = [('coin', 'Бросить монету'), ('cube', 'Бросить игральную кость'), ('number', 'Случайное число')]
    game = forms.ChoiceField(choices=games, label='Выберите игру')
    count = forms.IntegerField(min_value=1, max_value=64, label='Выберите количество попыток')

