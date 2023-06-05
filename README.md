# REST API GET NEWS (Berita)

![Markdown News](img/news.jpeg)

_using python_ flask

_using postgresql / mypostresql_

_using vercel_

## Install Dependecies

```
pip install -r requirements.txt
```

## Usage

### run the app

```
flask run
```

##### or

```
py runserver.py
```

## ENDPOINT

| METHOD | ROUTE                          | FUNCTIONALITY                                  | ACCESS     |
| ------ | ------------------------------ | ---------------------------------------------- | ---------- |
| GET    | /api/berita                    | Mendapatkan semua berita secara umum           | semua user |
| GET    | /api/berita/berita/{id_berita} | Mendapatkan semua berita berdasarkan id berita | semua user |
| GET    | /api/berita/lokasi/{id_lokasi} | Mendapatkan semua berita berdasarkan id lokasi | semua user |
| GET    | /api/berita/sumber             | Mendapatkan sumber berita                      | semua user |
| POST   | /login                         | login user dan mendapatkan token jwt           | semua user |
| POST   | /signup                        | daftar user                                    | semua user |
| POST   | /refresh                       | mendapatkan token jwt kembaliberita            | semua user |

#add feature
otentikasi email
