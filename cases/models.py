from django.db import models


class CaseType(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type

class CaseStage(models.Model):
    stage = models.CharField(max_length=60)
    
    def __str__(self):
        return self.stage

class Court(models.Model):
    court = models.CharField(max_length=60)
    
    def __str__(self):
        return self.court

# Create your models here.
class Cases(models.Model):
    title = models.CharField(max_length=250)
    number = models.BigIntegerField()
    year = models.IntegerField()

    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    # court_complex = models.TextField()
    type = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    stage = models.ForeignKey(CaseStage, on_delete=models.CASCADE)

    tags = models.CharField(max_length=100, blank=True)
    filling_date = models.DateField()
    appearing_lawyer = models.CharField(max_length=250)
    remarks = models.TextField()



    # Party Details
    for_party_name = models.CharField(max_length=30)

    party_contact_no = models.CharField(max_length=15)
    party_email = models.CharField(max_length=40, blank=True, default="")
    party_alternative_contact_no = models.CharField(max_length=14, blank=True, default="")
    party_adress = models.TextField(blank=True, default="")

    # Hearing Dates
    next_date = models.DateField(null=True)

    # Case files

    # Case history
    additional_comments = models.TextField()


    def case_type_short(self):
        print(self.type)
        return self.type.split(" ")[0]

    def __str__(self) -> str:
        return f"{self.for_party_name}: {self.stage}"