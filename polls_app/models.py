from django.db import models

# Create your models here.
class post(models.Model):
    post_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.post_name

class political_party(models.Model):
    party_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.party_name
    
class candidate(models.Model):
    candidate_name = models.CharField(max_length=100)
    party = models.ForeignKey(political_party, on_delete=models.CASCADE, null=True, blank=True)
    cand_post = models.ForeignKey(post, on_delete=models.CASCADE)
    cand_manifesto = models.TextField()
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.candidate_name

class voter(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class votes(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(voter, on_delete=models.CASCADE)
    timestamp = models.DateField()