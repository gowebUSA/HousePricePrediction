# House Price Prediction Machine Learning
The Django project on the House Price Prediction System utilizes essential components such as software, datasets, and Python libraries. It demonstrates the final working website built using Django. Django is chosen for this project due to its reliability and ease of use as a Python web framework.
- Link: https://www.youtube.com/watch?v=mkUt6-y1MSs&list=PL-QRwhZe4lltW73TjetSj_ppKyddWs4W6

## Requirements
- Python libraries and framework
    - Numpy
    - Pandas
    - Sklearn
    - Django
    - IDE (VSCode, IntelliJ, Pycharm)
    - Chrome browser


## Steps
- Train the Model using Jupyter - [HousePricePredictionML.ipynb](https://colab.research.google.com/drive/1I5dmDap7y9FSPmch7uXgUofoe6nnj_LM?usp=sharing)
- Use Pycharm

### Pycharm
- Install Pycharm
- Install Django
    * `pip install --user django`
- Install Anaconda
- Open Pycharm and create +New Project
  * Ensure that environment is correct for Anaconda
  * Use the following starting codes
      - Start project: `python -m django startproject HousePricePrediction`
      - Change the directory: `cd HousePricePrediction`
      - `python manage.py runserver` **Use this to run program**
          * It will create a link: http://127.0.0.1:8000/
  * Create templates folder
      - Created html file called `home.html`
  * Under `urls.py`
      - ```
            """
            Class-based views
                1. Add an import: from other_app.views import Home
                2. Add a URL ro urlpatterns: path('', Home.as_view(), name='home')
            Including another URLconf
                1. Import the include() function: from django.urls import include, path
                2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
            """
            from django.contrib import admin
            from django.urls import path
            from . import views

            urlpatterns = [
                path('admin/' admin.site.urls),
                path('', views.home),    # add views.home
            ]
        ```
  * Create `views.py` under HousePricePrediction folder
      - ```
            from django.shortcuts import render;

            def home(request):
                return render(request, "home.html")
        ```
  * Under Setting.py
      - TEMPLATE:
          `'DIRS': [os.path.join(BASE_DIR, 'templates')],`  
   

## Troubleshootinh
- For installing Django: `pip install --user django`
- For upgrading pip: `python -m pip install --upgrade --user pip`

## Reference
- USA houses dataset: [https://www.kaggle.com/vedavyasv/usa-...](https://www.kaggle.com/datasets/vedavyasv/usa-housing)
- Django: https://anaconda.org/anaconda/django
- Python: https://www.python.org/downloads/
- Anaconda: [https://docs.anaconda.com/anaconda/in...](https://www.anaconda.com/docs/getting-started/anaconda/install)
- PyCharm: [https://www.jetbrains.com/pycharm/dow...](https://www.jetbrains.com/pycharm/download/?section=windows#section=windows)
- Google Chrome: https://www.google.com/chrome/
- NumPy: https://anaconda.org/anaconda/numpy
- Pandas: https://anaconda.org/anaconda/pandas
- Sklearn: [https://scikit-learn.org/stable/insta...](https://scikit-learn.org/stable/install.html)
