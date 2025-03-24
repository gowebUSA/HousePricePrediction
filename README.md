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
      - `python manage.py runserver`
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
   


## Reference
- USA houses dataset: [https://www.kaggle.com/vedavyasv/usa-...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWlJX2p3VWdic0xnaXlIdnFGZEpDZEEtQXhVUXxBQ3Jtc0ttb1pBbno5ZzlrVVRmWlpHcWx4ZlNMQnpxSGt5X051Uk1KT0JnTVNGSTd2Znc3VFFQMWNHVTM2dXNuYnpvNF94TXBFQkJXbFVBVW4tRWh1NDNVbU9EOWxOcTlzN3FCN1JmUnN4eFV5eWRrSHZvWlVQZw&q=https%3A%2F%2Fwww.kaggle.com%2Fvedavyasv%2Fusa-housing&v=mkUt6-y1MSs)
- Django: https://anaconda.org/anaconda/django
- Python: https://www.python.org/downloads/
- Anaconda: [https://docs.anaconda.com/anaconda/in...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2U2OF8xdTFTeExtQW5MNmQxTHRyNTcwZG8tQXxBQ3Jtc0ttVENvRUtCNjZhLURBQUlTTnQ1OXEyTGNucHdfMWFlX3JydndEZkNLbEhqR2JUQmhHTHJQWTN6YlZaWUtNc0RvbjFXTTJwb0V1YnBJMVlOZTl4eTZSblJKbDhJc1dlaXc4VXQ3UTExUGFndWI5N0UyTQ&q=https%3A%2F%2Fdocs.anaconda.com%2Fanaconda%2Finstall%2Fwindows%2F&v=mkUt6-y1MSs)
- PyCharm: [https://www.jetbrains.com/pycharm/dow...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazdxZ0taa0VCd1dROFJTMG5ZVUJLd2xmcDY1UXxBQ3Jtc0tsXzhQTllTQS1VdUR3a0U1cFIzZnZMM3ZnaHUwaGtuMWdDakpDUmhSVTQ1ZXpyRGx6cFBkd1E0UkZCNjZNMTFSUU95RnlOaDBKVVVaSS1zdmtYN3dCVGtWenVCRGRhVENDcC1jc3VlRGZBckpzUXNVSQ&q=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2F%23section%3Dwindows&v=mkUt6-y1MSs)
- Google Chrome: https://www.google.com/chrome/
- NumPy: https://anaconda.org/anaconda/numpy
- Pandas: https://anaconda.org/anaconda/pandas
- Sklearn: [https://scikit-learn.org/stable/insta...
](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGlnNkdIdHhiSWJ3aEdtbWVTZGc1VXN0emZ0QXxBQ3Jtc0treFVCTnl4emtwdmhjRlc2bmY0TElFTmtrY0RJX3R5RkxiX0Yyd0VIdXBrU28xX2YwQmZocm9iVHR3cHJOZFFZbHgtTk1NeS10YkkwRS11eDBFSFFWLU9ja1BwbXJMeVNGMUtscEhpOW9OLTJIVnhwUQ&q=https%3A%2F%2Fscikit-learn.org%2Fstable%2Finstall.html&v=mkUt6-y1MSs)
