from django.db import models

class PartyDesignation(models.Model):
    designation = models.CharField(max_length=30)

# Plaintiff
# Petitioner
# Appellant
# Applicant
# Complainant
# Decree Holder
# Caveator
# Defendent
# Respondent
# Judgement Debtor
# Accused
# Opponent


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
    year = models.IntegerField()

    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    # court_complex = models.TextField()
    type = models.ForeignKey(CaseType, on_delete=models.CASCADE)
    stage = models.ForeignKey(CaseStage, on_delete=models.CASCADE)

    tags = models.CharField(max_length=100, blank=True)
    filling_date = models.DateField()
    appearing_lawyer = models.CharField(max_length=255)
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


    def __str__(self) -> str:
        return f"{self.party_name}: {self.stage}"

    




    
# 
# <label for="title">title</label>
# <label for="number">number</label>
# <label for="court">court</label> : firm owner
# <label for="type">type</label>
# <label for="stage">stage</label> : anybody in firm
# <label for="tags">tags</label> : anybody in firm
# <label for="filling_date">filling_date</label>
# <label for="appearing_lawyer">appearing_lawyer</label> : firm owner
# <label for="remarks">remarks</label> : firm owner
# <label for="party_name">party_name</label> : firm owner
# <label for="party_contact_no">party_contact_no</label> : firm owner
# <label for="party_email">party_email</label>
# <label for="party_alternative_contact_no">party_alternative_contact_no</label>
# <label for="party_adress">party_adress</label>
# <label for="prev_date">prev_date</label>
# <label for="next_date">next_date</label> : anybody
# <label for="case_history">case_history</label>
# additional comments : anybody
