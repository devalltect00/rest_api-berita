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

| METHOD | ROUTE                                | FUNCTIONALITY                                                          | ACCESS     |
| ------ | ------------------------------------ | ---------------------------------------------------------------------- | ---------- |
| GET    | /api/berita/internal/                | Mendapatkan semua berita                                               | semua user |
| POST   | /api/berita/internal                 | Menyimpan berita yang dibuat                                           | admin      |
| GET    | /api/berita/internal/{id_berita}     | Mendapatkan semua berita berdasarkan id berita                         | semua user |
| PUT    | /api/berita/internal/{id_berita}     | Mengubah berita yang dibuat                                            | admin      |
| DELETE | /api/berita/internal/{id_berita}     | Mengubah berita yang dibuat                                            | admin      |
| GET    | /api/berita/external/sumber-berita   | Mendapatkan sumber berita yang tersedia                                | semua user |
| GET    | /api/berita/external/{newsSource_id} | Mendapatkan daftar berita yang didapat dari sumber berita yang diinput | semua user |
| POST   | /login                               | login user dan mendapatkan token jwt                                   | semua user |
| POST   | /signup                              | daftar user                                                            | semua user |
| POST   | /refresh                             | mendapatkan token jwt kembaliberita                                    | semua user |

#add feature
otentikasi email
