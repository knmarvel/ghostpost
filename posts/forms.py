from django import forms


class GhostPostForm(forms.Form):
    BOAST_ROAST_CHOICES = [
        (True, "BOAST"),
        (False, "ROAST")
    ]
    boast = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=BOAST_ROAST_CHOICES
    )
    text = forms.CharField(max_length=200)

    def __str__(self):
        return self.text

class SortForm(forms.Form):
    SORT_CHOICES = [
        ("new", "Sort by newest"),
        ("old", "Sort by oldest"),
        ("hot", "Sort by most upvoted"),
        ("not", "Sort by most downvoted")
    ]
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES
    )

