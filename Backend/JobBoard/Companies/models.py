from django.db import models
# Model for the Companies app
# Fields :
#         name -> name of the company
#         description -> description of the company
#         address -> address of the company
#         city -> city of the company
#         zipcode -> zipcode of the company
#         url_website -> url_website of the company
class Companies(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=65535)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    url_website = models.CharField(max_length=255)

    # Method "__str__"
    # return the PriparyKey of the company
    def __str__(self):
        return str(self.pk)

    # Method "Meta"
    # set 'Companies' as plural name in admin panel
    class Meta:
        verbose_name_plural = 'Companies'
