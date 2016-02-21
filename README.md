# Python Türkiye Web Sitesi

[Python Türkiye](http://pythonturkiye.com/)


## PostgreSQL kurulumu ve Django ile kullanımı

1. **Paketleri Güncelle**  
`sudo apt-get update`  
`sudo apt-get upgrade`
2. **Gerekli Paketlerin Kurulumu**  
`sudo apt-get install python(3)-dev libpq-dev postgresql postgresql-contrib`
3. **Database ve Database Kullanıcısı oluştur**  
İlk önce postgres kullanıcısına oturum açmamız gerekiyor.  
`sudo su - postgres`  
`psql`  
giriş yaptıktan sonra veritabanımızı oluşturabiliriz. Konsolun değiştiğini fark edeceksiniz.  
`CREATE DATABASE ptweb;`  
Şimdi bu veritabanı için kullanıcı oluşturacağız.  
`CREATE USER maksat WITH PASSWORD 'password';`  
Şimdi ise bazı ayarları değiştireceğiz.  
`ALTER ROLE maksat SET client_encoding TO 'utf8';`  
`ALTER ROLE maksat SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE maksat SET timezone TO 'UTC';`  
Oluşturduğumuz kullanıcımıza yetki vereceğiz.  
`GRANT ALL PRIVILEGES ON DATABASE ptweb TO maksat;`  
**postgres** oturumuna geri dönmek için:  
`\q`  
**postgres** oturumundan çıkmak için:  
`exit`  
4. **Virtualenv içine *Django* ve *Psycopg2* Kurulumu**  
    1. **Virtualenv'mizi aktive edelim**  
    `cd`  
    `mkdir venvs`  
    `cd venvs`  
    `virtualenv --python=python3 ptweb`  
    `source ptweb/bin/activate`  
    2. **Paketleri kuralım**  
    `pip install django psycopg2`  
    3. **Projede düzenlemeler yapalım(Bu kısmı ben push yapacağım)**  
    `cd`  
    `cd python-turkiye-web`  
    `cd ptweb`  
    `vim ptweb/settings.py`  
    aşağıdaki satırları bulup comment haline getirelim:
```
    #DATABASES = {
    #    'default': {
    #        'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #    }
    #}
```
ve aşağıdakiyi ekleyelim:
```
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'ptweb',
             'USER': 'maksat',
             'PASSWORD': 'password',
             'HOST': 'localhost',
             'PORT': '',
         }
    }
```
**Son olarak Migrate yapalım:**  
`python manage.py migrate`

# Projeyi Çalıştırmak için Yapmanız Gerekenler  
Virtualenv içindeyken:  
`pip install -r requirements.txt`  
yaparsınız tüm paketleri sizin için kurar.

# Web settings ayarları
ptweb dizinindeki settings.py üzerinden şu ayarları yapalım.
## Database
```python
DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.postgresql_psycopg2',
     'NAME': '{db_name}',
     'USER': '{db_user}',
     'PASSWORD': '{db_pass}',
     'HOST': '{localhost}',
     'PORT': '',
 }
}
```

## Uygulama parametreleri
```python
FACEBOOK_ACCESS_TOKEN = "{FACEBOOK_ACCESS_TOKEN}"
YOUTUBE_API_KEY = "{YOUTUBE_API_KEY}"
YOUTUBE_CHANNEL_ID = "{YOUTUBE_CHANNEL_ID}"
TWITTER_CONSUMER_KEY = "{TWITTER_CONSUMER_KEY}"
TWITTER_CONSUMER_SECRET_KEY = "{TWITTER_CONSUMER_SECRET_KEY}"
TWITTER_ACCESS_TOKEN_KEY = "{TWITTER_ACCESS_TOKEN_KEY}"
TWITTER_ACCESS_TOKEN_SECRET_KEY = "{TWITTER_ACCESS_TOKEN_SECRET_KEY}"
```
