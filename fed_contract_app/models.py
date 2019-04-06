from django.db import models

# Create your models here.


class Result(models.Model):
    title = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    posted_date = models.DateField(null=True)

    place_of_performance_state = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST >)

    place_of_performance_zip_code = models.IntegerField()

    documents_to_search = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    set_aside_code = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    opportunity_procurement_type = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    agency_office_location = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    recovery_and_reinvestment_act_action = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    keywords_or_sol = models.CharField(max_length=100)

    naics_code = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    classification_code = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    j_and_a_statutory_authority = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    fair_opportunity_limited_source_justification_authority = models.CharField(
        max_length=30, choices= < NAME_OF_CHOICE_LIST > )

    posted_date_range = models.DateField(null=True)

    response_deadline = models.DateField(null=True)

    last_modified = models.DateField(null=True)

    contract_award_date = models.DateField(null=True)
