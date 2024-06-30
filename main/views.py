from django.shortcuts import render
from .models import Article

from openai import OpenAI, RateLimitError

client = OpenAI()
from django.conf import settings

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        try:
            response = client.completions.create(model="gpt-3.5-turbo",
                                                 prompt=user_message,
                                                 max_tokens=150)
            bot_response = response.choices[0].text.strip()
        except RateLimitError:
            bot_response = "We're currently experiencing high demand and have exceeded our usage limits. Please try again later."
        return render(request, 'main/chatbot.html', {'response': bot_response})
    return render(request, 'main/chatbot.html')