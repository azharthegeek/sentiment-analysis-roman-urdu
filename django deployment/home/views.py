from django.shortcuts import render
from django.http import HttpResponse
import pickle

# Loading the saved model
loaded_model = pickle.load(open(
    'C:\\Users\\azhar\\OneDrive\\Documents\\sentiment-analysis-roman-urdu\\django deployment\\home\\spnn-model.sav', 'rb'))
cv = pickle.load(open(
    'C:\\Users\\azhar\\OneDrive\\Documents\\sentiment-analysis-roman-urdu\\django deployment\\home\\countvectorizer.sav', 'rb'))


def home(request):
    return render(request, 'index.html')


def predict_sentiment(review):
    review = [review]
    review = cv.transform(review).toarray()
    sentiment = loaded_model.predict(review)
    if sentiment == 2:
        return "Positive 😀"
    elif sentiment == 1:
        return "Neutral 😐"
    else:
        return "Negative 😠"


def sentiment(request):
    if request.method == "POST":
        review = request.POST.get("review")
        sentiment = predict_sentiment(review)
        return render(request, 'sentiment.html', {'sentiment': sentiment})
    else:
        return render(request, 'sentiment.html')
