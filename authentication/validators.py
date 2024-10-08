
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'
    

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins un chiffre."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _("Votre mot de passe doit contenir au moins un chiffre.")