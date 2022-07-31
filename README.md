# kleenex-backend

## ✅ 팀원

 - BACKEND
 
 김도연, 안상현
 
 - FRONTEND
 
 김영수, 오창훈, 최원익
 
 
 

## ✅  개발 기간
- 개발 기간 : 2022-07-18 ~ 2022-07-29 (12일)
- 협업 툴 : Slack, Trello, Github, Notion




## ✅  프로젝트 목표

테라로사(https://terarosa.com/) 사이트 클론코딩

---




## ✅ 구현 사항

__김도연 [kdylsky](https://github.com/kdylsky)__

- `dbdiagram`을 활용한 모델링

- `Django` 프로젝트 초기 설정

- MySQL 기본 데이터 구축 및 저장

- 로그인 기능 및 `bcrpyt`, `pyjwt`를 회원 인증/인가 API 구현

- 회원가입 기능 및 `bcrypt`를 통해 암호화된 회원정보 DB 저장

- 장바구니 API 구현 - POST, GET, PETCH, DELETE

---


## ✅ 구현 기능
이번 프로젝트에서 구현한 기능은 총 3가지입니다.

1. 회원가입& 로그인 API

회원 정보에 대한 유효성 검사

회원 비밀번호 bcrypt 암호화

bcrypt를 활용한 비밀번호 암호화/복호화

jwt를 활용한 토큰 발급 및 토큰 인가


2. 장바구니 API

상품 상세 페이지에서 해당 상품 장바구니에 추가하기
로그인 한 유저의 장바구니에 담긴 상품 확인하기
로그인 한 유저의 장바구니에서 담기 상품에 대한 수량 변경하기
로그인 한 유저의 장바구니에서 선택된 상품 삭제하기 & 전체 상품 삭제하기



## ✅ 사이트 시현 영상

https://user-images.githubusercontent.com/99232122/181917935-402877fe-ae48-42bd-871c-3246b5ac6bf7.mov




## ✅ DB모델링
![DB](https://user-images.githubusercontent.com/99232122/181917443-5e959b79-4af4-4775-9c71-8be9a1e22194.png)





## ✅ API 명세서

![API](https://user-images.githubusercontent.com/99232122/181919207-527e7ba6-8043-41b4-9305-1fc4ea007d53.png)


## 기술 스택
|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |                                                  Deploy                                                 |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |:------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white">|



