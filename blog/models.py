from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Create A Blog models
#title
#pub_date
#body(of blog test)
#image


#Add the Blog app to the settings

#create a migration

#Migrate

#Add to the admin
