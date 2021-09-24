# 지뢰찾기


## 소개
- 게임 보드는 가로 10줄, 세로 10줄로 구성되어 있습니다.
- 지뢰는 총 10개로 랜덤 배치되어 있습니다.
- 각 사각형은 주변부(최대 8칸)에 위치하며 __자신을 제외한__ 지뢰의 갯수를 나타냅니다.
- 모든 사각형이 가지고 있는 숫자를 출력합니다.
- 주변에 폭탄이 하나라도 있다면 __하늘색__ 으로 출력됩니다.
- 폭탄이 위치한 자리는 __분홍색__ 으로 출력됩니다.
- 폭탄이 위치한 자리의 주변에 하나 이상의 폭탄이 있다면 __분홍색__ 으로 출력됩니다.

## 기술
- Python

## 실행 방법
```python
- python을 설치한 경우
git clone https://github.com/anrunda9/minesweeper.git
cd minesweeper
python execute.py

- python 미설치시
docker pull anrunda9/ubuntu-python3-assignment
docker run -it anrunda9/ubuntu-python3-assignment
cd minesweeper
python3 execute.py
```
