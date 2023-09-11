from django.db import models


class Court(models.Model):
    court = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.court

class CaseType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.type

class CaseStage(models.Model):
    stage = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.stage

# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=255)
    number = models.BigIntegerField()
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    type = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    stage = models.ForeignKey(CaseStage, on_delete=models.CASCADE)

    tags = models.CharField(max_length=100, blank=True)
    filling_date = models.DateField()
    appearing_lawyer = models.CharField(max_length=255)
    remarks = models.TextField()



    # Party Details
    party_name = models.CharField(max_length=30)
    party_contact_no = models.CharField(max_length=15)
    party_email = models.CharField(max_length=40, blank=True, default="")
    party_alternative_contact_no = models.CharField(max_length=14, blank=True, default="")
    party_adress = models.TextField(blank=True, default="")

    # Hearing Dates
    prev_date = models.DateField()
    next_date = models.DateField(null=True)

    # Case files

    # Case history
    case_history = models.TextField()

    def __str__(self) -> str:
        return self.title

    




    



