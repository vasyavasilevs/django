from django import forms

class EnglishTestForm(forms.Form):
    # A1 Level
    question1 = forms.ChoiceField(
        label="Choose the correct article: ___ apple",
        choices=[('a', 'a'), ('an', 'an'), ('the', 'the')],
        widget=forms.RadioSelect
    )
    question2 = forms.ChoiceField(
        label="Choose the correct form: He ___ to school every day.",
        choices=[('go', 'go'), ('goes', 'goes'), ('going', 'going')],
        widget=forms.RadioSelect
    )

    # A2 Level
    question3 = forms.ChoiceField(
        label="Choose the correct preposition: She is interested ___ music.",
        choices=[('in', 'in'), ('on', 'on'), ('at', 'at')],
        widget=forms.RadioSelect
    )
    question4 = forms.ChoiceField(
        label="Which of the following is correct?",
        choices=[('She can sings well.', 'She can sings well.'),
                 ('She can sing well.', 'She can sing well.')],
        widget=forms.RadioSelect
    )

    # B1 Level
    question5 = forms.ChoiceField(
        label="Choose the correct past tense form: Yesterday, I ___ a great time.",
        choices=[('had', 'had'), ('have', 'have'), ('having', 'having')],
        widget=forms.RadioSelect
    )
    question6 = forms.ChoiceField(
        label="Which sentence is in the passive voice?",
        choices=[('The cake is eaten by him.', 'The cake is eaten by him.'),
                 ('He eats the cake.', 'He eats the cake.')],
        widget=forms.RadioSelect
    )

    # B2 Level
    question7 = forms.ChoiceField(
        label="Choose the correct condition: If I ___ you, I would call her.",
        choices=[('am', 'am'), ('was', 'was'), ('were', 'were')],
        widget=forms.RadioSelect
    )
    question8 = forms.ChoiceField(
        label="Choose the correct form of the verb: She ___ a book at the moment.",
        choices=[('reads', 'reads'), ('read', 'read'), ('is reading', 'is reading')],
        widget=forms.RadioSelect
    )

    # C1 Level
    question9 = forms.ChoiceField(
        label="Which sentence is correct?",
        choices=[('Although it was raining, we went for a walk.',
                  'Although it was raining, we went for a walk.'),
                 ('Although it raining, we went for a walk.',
                  'Although it raining, we went for a walk.')],
        widget=forms.RadioSelect
    )
    question10 = forms.ChoiceField(
        label="Choose the correct word to complete the sentence: I can’t __________ the meeting.",
        choices=[('attend', 'attend'), ('attending', 'attending'), ('attended', 'attended')],
        widget=forms.RadioSelect
    )
