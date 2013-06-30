from django.db import models

# Create your models here.

class Pattern(models.Model):
    name = models.TextField()
    description = models.TextField()
    intent = models.TextField()
    motivation = models.TextField()
    structure = models.TextField() # yuml description
    consequences = models.TextField()
    tags = models.ManyToManyField('Tags', related_name="patterns")    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name=models.TextField()
    icon= models.URLField()
    def __str__(self):
        return self.name
       
    
class Language(models.Model):
    name = models.TextField()
    wikipedia = models.URLField()
    super_lang = models.ForeignKey('Language', null=True, blank=True, related_name="dialects")
    def __str__(self):
        return self.name
    
    
class Implementation(models.Model):
    pattern = models.ForeignKey(Pattern, related_name="implementations")
    gist = models.IntegerField() # for gist
    language = models.ForeignKey(Language)
    file = models.TextField(null=True, blank =True)
     
    
    
class Use(models.Model):
    pattern = models.ForeignKey(Pattern, related_name="uses")
    name = models.TextField()
    url = models.URLField()
    language = models.ManyToManyField(Language, null=True, blank=True)
    line_start = models.IntegerField(null=True, blank=True)
    line_end = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name