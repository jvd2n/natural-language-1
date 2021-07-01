from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# class Member(models.Model):
#
#     username = models.CharField(primary_key=True, max_length=10)
#     password = models.CharField(max_length=10)
#     name = models.CharField(max_length=12)
#     email = models.EmailField()
#
#     class Meta:
#         managed = True
#         # db_table = 'members'
#         # ordering = ['created']
#
#     def __str__(self):
#         return f'[{self.pk}]{self.username}'


class MemberVO(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=12)
    email = models.EmailField()

    class Meta:
        managed = True
        db_table = 'members'
        # ordering = ['created']

    def __str__(self):
        return f'[{self.pk}]{self.username}, {self.password}, {self.name}'
