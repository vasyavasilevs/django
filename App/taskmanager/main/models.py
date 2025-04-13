from django.db import models

class EnglishLevel(models.Model):
    """
    Represents a CEFR English proficiency level.

    Attributes:
        LEVEL_CHOICES (list): List of available English levels.
        name (CharField): Code of the level (e.g., 'A1', 'B2'), unique.
    """
    LEVEL_CHOICES = [
        ('A1', 'Beginner'),
        ('A2', 'Elementary'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper-Intermediate'),
        ('C1', 'Advanced'),
    ]
    name = models.CharField(max_length=2, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        """
        Returns the human-readable name of the level (e.g., 'Beginner').
        """
        return self.get_name_display()

class Tutor(models.Model):
    """
    Represents a tutor who teaches students at a specific English level.

    Attributes:
        name (CharField): Full name of the tutor.
        level (ForeignKey): Related English level the tutor teaches.
    """
    name = models.CharField(max_length=100)
    level = models.ForeignKey(EnglishLevel, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the name of the tutor.
        """
        return self.name
