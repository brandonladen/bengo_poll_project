from django.db import models

# Create your models here.
class post(models.Model):
    post_name = models.CharField(max_length=200)
    
    #SELECT * FROM STUDENT WHERE ID=20;
    #STUDENT.objects.filter(ID=20)
    
    
# POLITICAL_PARTY_TABLE
# 	PARTY_ID
# 	PARTY_NAME
	
# POST TABLE
# 	POST_ID
# 	POST_NAME

# CANDIDATES TABLE
# 	CAND_ID
# 	CAND_NAME
# 	CAND_POST
# 	CAND_MANIFESTO
# 	CAND_VOTES
# 	CONTACT_DETAILS

# VOTES
# 	VOTE_ID
# 	CAND
# 	VOTES
# 	DATE/TIME