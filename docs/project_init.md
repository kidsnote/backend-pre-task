# 프로젝트 초기 설정

## pre-commit

- 자동화된 린트 및 코드 포맷터를 사용하여 코드 품질을 유지합니다.
    - flake8, black, pyright 등 사용

### TODO

1. requirements.txt를 자동 갱신하도록 hook을 추가합니다.

## Pull Request

- PR을 통해 코드 리뷰를 진행합니다.
- PR Template을 이용해 컨벤션을 정합니다.
- PR에서 lint 및 test를 자동으로 실행합니다.
    - flake8을 활용
    - pytest를 활용

## 환경 설정

- local,test, prod 환경을 구분합니다.
- 환경 변수를 사용하여 설정을 관리합니다.