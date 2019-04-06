from django.db import models

# Create your models here.
J_AND_A_AUTHORITY = (
    ('FAR 6.302-1(c) - Brand name', 'FAR 6.302-1(c) - Brand name')
)
JUSTIFICATION_AUTH = (
    ('Urgency', 'Urgency'),
    ('Minimum Guarantee', 'Minimum Guarantee'),
    ('Other Statutory Authority', 'Other Statutory Authority')
)


class Result(models.Model):
    title = models.CharField(max_length=200)
    headers = models.TextField()
    synopsis = models.TextField()
    naics = models.PositiveIntegerField()
    period = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    incumbent = models.TextField()
    matched = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    company_name = models.CharField(max_length=100)

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
        max_length=30, choices= < J_AND_A_AUTHORITY > )

    fair_opportunity_limited_source_justification_authority = models.CharField(
        max_length=30, choices=JUSTIFICATION_AUTH)

    posted_date_range = models.DateField(null=True)

    response_deadline = models.DateField(null=True)

    last_modified = models.DateField(null=True)

    contract_award_date = models.DateField(null=True)

    def __str__(self):
    return self.company_name


class Keyword(models.Model):
    keyword1 = models.CharField(max_length=200)
    keyword2 = models.CharField(max_length=200)
    keyword3 = models.CharField(max_length=200)
    keyword4 = models.CharField(max_length=200)
    keyword5 = models.CharField(max_length=200)
    keyword6 = models.CharField(max_length=200)

    def __str__(self):
    return self.title
