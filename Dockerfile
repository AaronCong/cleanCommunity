FROM python:3.6

RUN pip install Flask==0.12.2 Flask-APScheduler==1.11.0 Flask-Cors==3.0.4 Flask-Login==0.4.0 Flask-SQLAlchemy==2.4.0
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /codes
COPY codes /codes

CMD ["python", "app.py"]