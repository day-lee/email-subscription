# Email Subscription 이메일 구독

## 📌 How to Install the "Email Subscription" Project 설치 방법
```
# Create a New Folder for Project
mkdir project_folder

# Create a Virtual Environment 
cd project_folder 
python -m venv venv

# Activate the Virtual Enviroment on terminal
source project_folder\venv\Scripts\activate
if below line shows up, virtual environment has been successfully created
(venv) C:\> 

# Install Required Packages
pip install -r requirements.txt

# Migrate Tables
python manage.py makemigrations 
python manage.py migrate

# Create Admin Account
python manage.py createsuperuser

# Run Server
python manage.py runserver


```
## 📌 Features

## Add Subscriber 구독 신청

- **URL**

    /subscription/add

- **Method:**

    `POST`

- **Success Response:**
    - **Code:** 201 CREATED
    - **Content:** `[{"id":1,"title":"hello","author":1,"excerpt":"hi","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]`
    
  
- **Error Response:**
    - **Code:** 400
    - **Content:** `HTTP_400_BAD_REQUEST`

    -------------------------------------------------------------------------

## Unsubscribe 구독 해지

- **URL**

    /subscription/cancel/<int:pk>

- **Method:**

    `DELETE`   

- **Success Response:**
    - **Code:** 200 OK
  
- **Error Response:**
    - **Code:** HTTP_404_NOT_FOUND

    -------------------------------------------------------------------------

## Filter by Category 카테고리 필터

- **URL**

    /subscription/search/?category=여행

- **Method:**

    `GET`



- **Success Response:**
    - **Code:** 200 OK
    - **Content:** ` {
        "id": 3,
        "subject": "hi",
        "content": "hey",
        "subscriber": {
            "id": 5,
            "email": "user1@mail.com",
            "name": "user1",
            "category": [
                "IT",
                "반려 동물"
            ]
        }
    }`
    
  

    -------------------------------------------------------------------------

## Send Email 이메일 전송과 저장

- **URL**

    /email/send/

- **Method:**

    `POST`

- **Success Response:**
    - **Message:** {"status": "success"}
    
- **Error Response:**
    - **Message:** {"status": "fail"}

    -------------------------------------------------------------------------


## Filter By Email Subject

- **URL**

    /email/search/?subject=hello

- **Method:**

    `GET`


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `[{
        "id": 2,
        "subject": "hello",
        "content": "hi",
        "subscriber": {
            "id": 5,
            "email": "user1@mail.com",
            "name": "user1",
            "category": [
                "IT",
                "반려 동물"
            ]
        }
    }]`
    




