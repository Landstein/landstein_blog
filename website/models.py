from django.core.validators import RegexValidator
from django.db import models
from taggit.managers import TaggableManager

permalink_validator = RegexValidator(
    r'^[a-zA-Z0-9-_]+$',
    'Only alphanumeric, hyphen and underscore characters are allowed (no spaces).'
)


class Base(models.Model):
    """ Base model for multiple page types """
    title = models.CharField(max_length=500)
    date_published = models.DateTimeField('Date Published', auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Page(Base):
    """ Page type """
    permalink = models.CharField(max_length=200,
            unique=True, validators=[permalink_validator])
    body = models.TextField()


class Post(Base):
    """ Post type """
    tags = TaggableManager()
    summary = models.TextField()
    image = models.URLField()
    link = models.URLField()
    new_tab = models.BooleanField(default=False)


class Work(Base):
    """ Works type """
    tags = TaggableManager()
    summary = models.TextField()
    image = models.URLField()
    link = models.URLField()
    new_tab = models.BooleanField(default=False)


class Nav(models.Model):
    """ Main navigation """
    name = models.CharField(max_length=200)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Config(SingletonModel):
    """ Config """
    greeting = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    intro = models.TextField()
    image = models.URLField()
    resume = models.URLField()

    def __str__(self):
        return 'Website Config'


class Social(models.Model):
    """ Social media links """
    name = models.CharField(max_length=200)
    link = models.URLField()
    image = models.URLField()
    order = models.IntegerField()

    def __str__(self):
        return self.name
