# wanted-pre-onboarding-backend ์ฌ์  ๊ณผ์ 

## ๐ ํ๋ก์ ํธ ์๊ฐ
<hr>

**Wanted**๊ฐ์ ๊ธฐ์ ์ฑ์ฉ ์น ์๋น์ค API ๊ตฌํ
- ์ฑ์ฉ๊ณต๊ณ  - ์์ฑ, ๋ชฉ๋ก, ์์ธ
- ์ฌ์ฉ์ - ์ง์

## ๐ ์๊ตฌ์ฌํญ ๋ถ์
<hr>


* ORM ์ฌ์ฉํ์ฌ ๊ตฌํ: ORM์ธ Django Model
* RDBMS ์ฌ์ฉ(SQLite, PostgreSQL ๋ฑ) : SQLite ์ฌ์ฉ
* ์ฝ๋ ๊ฐ๋์ฑ์ ์ํด ํ์ด์ฌ PEP 8 ์ฐธ์กฐ (https://scshim.tistory.com/609)
* Git commit ๋ฉ์์ง ์ปจ๋ฒค์ : [Add], [feat], [docs] ์ฌ์ฉ
* Unit Test 

## ๐ ๊ธฐ์  Stack
<hr>

- ``Django``, ``SQLite3``, ``Git``, ``Postman``

## ๐ ์๋น์ค ๊ฐ์
<hr>

* ๋ณธ ์๋น์ค๋ ๊ธฐ์์ ์ฑ์ฉ์ ์ํ ์น ์๋น์ค์๋๋ค.
* ํ์ฌ๋ ์ฑ์ฉ๊ณต๊ณ ๋ฅผ ์์ฑํ๊ณ , ์ด์ ์ฌ์ฉ์๋ ์ง์ํฉ๋๋ค.



## โ ๊ตฌํ ๊ณผ์ 

---
### โถ๏ธModeling
- **Company** , **job**, **user**, **apply** ํ์ด๋ธ์ ๋ฉ์ธ์ผ๋ก ๊ตฌํ ์งํ
- **region**, **country** ๋ ์ ๊ทํ๋ฅผ ์ํด ํ์ด๋ธ ๋ถ๋ฆฌ

---
### โถ๏ธ์ฑ์ฉ๊ณต๊ณ  ๋ฑ๋ก
- **Post๋ก ์ฑ์ฉ๊ณต๊ณ  ๋ฑ๋ก & DB๋ฐ์ ํ์ธ** 
<img src="https://user-images.githubusercontent.com/95831345/185069923-112638fd-5757-4edb-bfa2-7507b0c98456.jpg"  width="800"/>

---
### โถ๏ธ์ฑ์ฉ๊ณต๊ณ  ์์ 
- **Post๋ก ์ฑ์ฉ๊ณต๊ณ  ์์  & DB๋ฐ์ ํ์ธ**
<img src="https://user-images.githubusercontent.com/95831345/185075107-2dc016a3-62ad-47ca-870d-55d31bbdf696.jpg"  width="800"/>

---
### โถ๏ธ์ฑ์ฉ๊ณต๊ณ  ์ญ์ 
- **Delete๋ก ์ฑ์ฉ๊ณต๊ณ  ์ญ์  & DB๋ฐ์ ํ์ธ**
<img src="https://user-images.githubusercontent.com/95831345/185075595-db3f4d2e-af32-48bd-9b06-a6c8715d447f.jpg"  width="800"/>

---
### โถ๏ธ์ฑ์ฉ๊ณต๊ณ  ๋ชฉ๋ก & ๊ฒ์๊ธฐ๋ฅ(์ ํ)
- **Post๋ก ์ฑ์ฉ๊ณต๊ณ  ๋ชฉ๋ก & DB๋ฐ์ ํ์ธ**
- **ํ์ฌ์ด๋ฆ๊ณผ ํฌ์ง์ ๋์ค ํ๋ ์ผ์น์ ๊ฒธ์๊ฒฐ๊ณผ ์ถ๋ ฅ**
<img src="https://user-images.githubusercontent.com/95831345/185075781-3471008c-4bc0-4286-ae11-3b5a8d2718f1.jpg"  width="800"/>
<img src="https://user-images.githubusercontent.com/95831345/185075790-a40e18e0-2422-4031-a922-f2a5e3e54aca.jpg"  width="800"/>
<img src="https://user-images.githubusercontent.com/95831345/185075815-d97bc58b-2582-48ce-8e54-12f585e96720.jpg"  width="800"/>

---
### โถ๏ธ์ฑ์ฉ์์ธ ํ์ด์ง + ๋ค๋ฅธ ์ฑ์ฉ์ ๋ณด(id)
- **์ฑ์ฉ์์ธํ์ด์ง์ ๊ทธ ์ฑ์ฉ์ ๋ณด๋ฅผ ์ ์ธํ ๋๋จธ์ง ์ฑ์ฉ id ์ถ๋ ฅ**
<img src="https://user-images.githubusercontent.com/95831345/185076057-bd2ee0de-16c9-498b-84af-e7f3548cefb3.jpg"  width="800"/>

---
### โถ๏ธ์ฑ์ฉ์ง์
- **์ ์ ๊ฐ ๊ทธ ์ฑ์ฉ์ ๋ณด์ ์ด๋ฏธ ์ง์์ ํ ๊ฒฝ์ฐ ์ค๋ฅ๋ฉ์ธ์ง ์ถ๋ ฅ : ALREADY_APPLY**
- **UserID์ JobID๊ฐ ์ ํจํ์ง์๋๊ฒฝ์ฐ ์ค๋ฅ๋ฉ์์ง ์ถ๋ ฅ : USER_NOT_EXIST / JOB_NOT_EXIST**
<img src="https://user-images.githubusercontent.com/95831345/185076266-435c950d-ef22-4527-bc26-d8e62c30a979.jpg"  width="400"/>
<img src="https://user-images.githubusercontent.com/95831345/185076299-d9717c37-f435-4573-b69c-837d0e041f11.jpg"  width="400"/>
<img src="https://user-images.githubusercontent.com/95831345/185076317-8d6848de-618f-4b0b-8f52-f1859e44b2d4.jpg"  width="400"/>
<img src="https://user-images.githubusercontent.com/95831345/185076341-c892c855-e4e2-4842-82a4-3b613bd08bbf.jpg"  width="400"/>


