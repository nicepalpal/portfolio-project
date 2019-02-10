from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add = True)
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
