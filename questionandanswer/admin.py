from django.contrib import admin
from room.models import Room
from .models import Question, Response, Scoring

class ResponseAdmin(admin.TabularInline):
    model = Response
    max_num = Response.MAX_RESPONSE
    min_num = Response.MIN_RESPONSE
    can_delete = False
    
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ResponseAdmin, )
    list_display = ['text',]
    search_fields = ['text','questions__text',]

class ScoringAdmin(admin.ModelAdmin):
    list_display = ['question', 'response', 'correct', 'points']
    
    class Meta:
        model = Scoring

admin.site.register(Scoring, ScoringAdmin)
admin.site.register(Question, QuestionAdmin)
