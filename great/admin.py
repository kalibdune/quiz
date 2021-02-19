from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #количество вопросов по умолчанию 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Вопрос', {'fields': ['question_text']}),
        ('Дата', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]# настройка полей в админке

    inlines = [ChoiceInline] # добавление в группу
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # Добавка фильтра
    search_fields = ['question_text'] # добавка поиска в фильтр 

admin.site.register(Question, QuestionAdmin)
