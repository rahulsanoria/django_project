# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib import admin
# from  .models import Question,Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

from django.contrib import admin

from .models import Question,Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date','was_published_recently')
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)



