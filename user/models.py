from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify


class ExtendedUser(AbstractUser):
    image = models.ImageField(blank=True)
    bio = models.CharField(max_length=280)
    is_yk = models.BooleanField(default=False)
    slug = models.SlugField()

    class Meta:
        ordering = ('-id', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(ExtendedUser, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user:profile', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username


class Team(models.Model):
    president = models.ForeignKey(ExtendedUser, on_delete=models.PROTECT, related_name='president')
    members = models.ManyToManyField(ExtendedUser, related_name='members')
    title = models.CharField(max_length=280, unique=True)
    image = models.ImageField(blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user:team_page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.president.is_yk:
            self.slug = slugify(self.title)
            super(Team, self).save(*args, **kwargs)


class MotivationLetters(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    author = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    letter = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('user:team_page', kwargs={'slug': team.slug})





