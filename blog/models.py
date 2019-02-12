from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')



# Create A Blog models
#title
#pub_date
#body(of blog test)
#image


#Add the Blog app to the settings

#create a migration

#Migrate

#Add to the admin
