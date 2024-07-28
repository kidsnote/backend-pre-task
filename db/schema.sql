
-- 각 테이블 utf 설정 (한글 데이터 insert 가능하도록)
ALTER TABLE users_user CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE contact_contact CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE contact_label CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 유저생성 (각 유저들의 비밀번호는 1111로 통일)
INSERT INTO users_user (password, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES
    ('pbkdf2_sha256$260000$AmrgViaeeryhjdjKzMfISB$sYvAQolbaDLD/ExG9gR7hP7mWZyTtQQ5JwDScfs6nLM=', false, 'user_1', 'One', 'user_1@test.com', false, true, CURRENT_TIMESTAMP),
    ('pbkdf2_sha256$260000$AmrgViaeeryhjdjKzMfISB$sYvAQolbaDLD/ExG9gR7hP7mWZyTtQQ5JwDScfs6nLM=', false, 'user_2', 'Two', 'user_2@test.com', false, true, CURRENT_TIMESTAMP),
    ('pbkdf2_sha256$260000$AmrgViaeeryhjdjKzMfISB$sYvAQolbaDLD/ExG9gR7hP7mWZyTtQQ5JwDScfs6nLM=', false, 'user_3', 'Three', 'user_3@test.com', false, true, CURRENT_TIMESTAMP);

-- 라벨 추가
INSERT INTO contact_label (name)
VALUES
    ('기타'),
    ('휴대전화'),
    ('대표전화'),
    ('집팩스'),
    ('직장팩스'),
    ('GoogleVoice'),
    ('호출기');

 -- user_1의 연락처들
INSERT INTO contact_contact (user_id, profile_image, name, email, contact_number, company, job_title, memo, address, birthday, website, created_at)
VALUES
(1, 'https://example.com/profile1.jpg', '김영희', 'younghee.kim@gmail.com', '010-1234-5678', '테크 주식회사', '소프트웨어 엔지니어', '대학 동창', '서울시 강남구 테헤란로 152', '1990-05-15', 'https://younghee.com', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile2.jpg', '이철수', 'chulsoo.lee@naver.com', '010-9876-5432', '금융 은행', '투자 분석가', '고등학교 친구', '경기도 성남시 분당구 판교역로 235', '1989-11-20', 'https://chulsoo.net', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile3.jpg', '박지영', 'jiyoung.park@daum.net', '010-2468-1357', '패션 브랜드', '마케팅 매니저', '여행 동호회 멤버', '서울시 송파구 올림픽로 300', '1992-08-03', 'https://jiyoung.io', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile4.jpg', '정민수', 'minsoo.jung@kakao.com', '010-1357-2468', '스타트업 인큐베이터', 'CEO', '멘토', '인천시 연수구 컨벤시아대로 153', '1985-02-28', 'https://minsoo.co.kr', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile5.jpg', '강다운', 'dawn.kang@gmail.com', '010-3698-5214', '그린에너지 주식회사', '환경 컨설턴트', '환경 세미나에서 만난 친구', '서울시 마포구 월드컵북로 396', '1991-07-22', 'https://dawn-kang.com', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile6.jpg', '서민재', 'minjae.seo@naver.com', '010-7412-8523', '글로벌 교육원', '영어 강사', '언어 교환 파트너', '경기도 수원시 영통구 월드컵로 206', '1988-12-10', 'https://minjae-edu.net', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile7.jpg', '오세은', 'se-eun.oh@daum.net', '010-9517-5328', '뷰티 케어 브랜드', '제품 개발자', '헬스장에서 만난 친구', '서울시 강서구 마곡중앙로 161', '1993-04-05', 'https://seeun-beauty.kr', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile8.jpg', '최준호', 'junho.choi@kakao.com', '010-8529-6374', '모바일 게임 스튜디오', '게임 디자이너', '온라인 게임 길드원', '경기도 성남시 분당구 판교로 256번길 25', '1987-09-18', 'https://junho-game.com', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile9.jpg', '윤하늘', 'sky.yoon@gmail.com', '010-4569-7823', '클라우드 서비스 기업', '시스템 엔지니어', '대학원 동기', '서울시 구로구 디지털로 288', '1990-01-30', 'https://sky-cloud.io', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile10.jpg', '임소라', 'sora.lim@naver.com', '010-7896-3214', '미디어 콘텐츠 제작사', '영상 편집자', '영화 동호회 회원', '서울시 마포구 와우산로 94', '1992-11-15', 'https://sora-media.net', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile11.jpg', '한도윤', 'doyoon.han@daum.net', '010-2587-4136', '바이오 연구소', '연구원', '과학 박람회에서 만난 지인', '대전시 유성구 엑스포로 125', '1989-06-20', 'https://doyoon-bio.co.kr', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile12.jpg', '곽승민', 'seungmin.kwak@kakao.com', '010-9632-8741', '건축 디자인 스튜디오', '건축가', '대학 선배', '서울시 종로구 세종대로 175', '1986-03-08', 'https://seungmin-arch.com', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile13.jpg', '송미래', 'mirae.song@gmail.com', '010-1478-5236', '투자 중개 회사', '금융 어드바이저', '재테크 스터디 멤버', '서울시 영등포구 여의나루로 67', '1991-10-25', 'https://mirae-finance.kr', CURRENT_TIMESTAMP),
(1, 'https://example.com/profile14.jpg', '노태현', 'taehyun.noh@naver.com', '010-3698-7412', '인공지능 연구소', '데이터 사이언티스트', '학회에서 만난 동료', '대구시 동구 동대구로 489', '1988-08-12', 'https://taehyun-ai.net', CURRENT_TIMESTAMP);
-- user_2의 연락처들
INSERT INTO contact_contact (user_id, profile_image, name, email, contact_number, company, job_title, memo, address, birthday, website, created_at)
VALUES
(2, 'https://example.com/profile5.jpg', '홍길동', 'gildong.hong@gmail.com', '010-1111-2222', '전자 기업', '하드웨어 엔지니어', '동네 이웃', '부산시 해운대구 마린시티2로 33', '1988-07-07', 'https://gildong.dev', CURRENT_TIMESTAMP),
(2, 'https://example.com/profile6.jpg', '강서연', 'seoyeon.kang@naver.com', '010-3333-4444', '교육 기관', '영어 강사', '언어 교환 파트너', '대구시 동구 동대구로 550', '1993-12-25', 'https://seoyeon.edu', CURRENT_TIMESTAMP),
(2, 'https://example.com/profile7.jpg', '임재현', 'jaehyun.lim@daum.net', '010-5555-6666', '건설 회사', '건축가', '헬스장 친구', '광주시 서구 상무중앙로 110', '1991-04-18', 'https://jaehyun.archi', CURRENT_TIMESTAMP);

-- user_3의 연락처들
INSERT INTO contact_contact (user_id, profile_image, name, email, contact_number, company, job_title, memo, address, birthday, website, created_at)
VALUES
(3, 'https://example.com/profile8.jpg', '오민지', 'minji.oh@gmail.com', '010-7777-8888', '광고 대행사', '크리에이티브 디렉터', '대학원 동기', '대전시 유성구 대학로 99', '1987-09-30', 'https://minji.design', CURRENT_TIMESTAMP),
(3, 'https://example.com/profile9.jpg', '서준호', 'junho.seo@naver.com', '010-9999-0000', '법률 사무소', '변호사', '고문 변호사', '울산시 남구 삼산로 35', '1984-01-10', 'https://junho.law', CURRENT_TIMESTAMP),
(3, 'https://example.com/profile10.jpg', '최유리', 'yuri.choi@daum.net', '010-2580-1379', '여행사', '여행 컨설턼트', '여행 동행', '제주시 노형동 노연로 55', '1994-06-22', 'https://yuri.travel', CURRENT_TIMESTAMP),
(3, 'https://example.com/profile11.jpg', '윤성민', 'sungmin.yoon@kakao.com', '010-8642-9753', '연구소', '데이터 과학자', '프로젝트 파트너', '세종시 한누리대로 2130', '1986-03-14', 'https://sungmin.science', CURRENT_TIMESTAMP);

-- 연락처와 라벨 연결
INSERT INTO contact_contact_labels (contact_id, label_id)
VALUES
(1, 2), (1, 3),  -- 김영희: 휴대전화, 대표전화
(2, 2), (2, 6),  -- 이철수: 휴대전화, GoogleVoice
(3, 2), (3, 1),  -- 박지영: 휴대전화, 기타
(4, 2), (4, 3),  -- 정민수: 휴대전화, 대표전화
(5, 2), (5, 5),  -- 홍길동: 휴대전화, 직장팩스
(6, 2), (6, 1),  -- 강서연: 휴대전화, 기타
(7, 2), (7, 3),  -- 임재현: 휴대전화, 대표전화
(8, 2), (8, 4),  -- 오민지: 휴대전화, 집팩스
(9, 2), (9, 5),  -- 서준호: 휴대전화, 직장팩스
(10, 2), (10, 6),-- 최유리: 휴대전화, GoogleVoice
(11, 2), (11, 7); -- 윤성민: 휴대전화, 호출기
