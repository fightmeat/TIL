
  # 아나콘다 버전 확인
    conda -V
    conda --version

  # 파이썬 버전 확인
    python -V
    python --version

  # pip 버전 확인
    pip -V
    pip --version

2. 업데이트
  # 아나콘다를 최신 버전으로 업데이트
    conda update conda

  # 파이썬을 최신 버전으로 업데이트
    conda update python

  # pip을 최신 버전으로 업데이트
    python -m pip install --upgrade pip

  # 모든 패키지를 최신 버전으로 업데이트
    conda update --all

3. 가상환경
  # 현재 활성화된 가상환경에 설치된 패키지 리스트
    conda list

  # 가상환경 리스트
    conda env list

  # 사용 가능한 패키지 버전
    conda search <패키지이름>

  # 파이썬 3.x버전의 가상환경 생성
    conda create -n <가상환경이름> python=3.x
    conda create --name <가상환경이름> python=3.x
    ex)python=3.9 이런식으로 붙혀서 써야한다.

  # 현재 활성화된 가상환경의 패키지 삭제
    conda remove <패키지이름>

  # 특정 가상환경의 패키지 삭제
    conda remove -n <가상환경이름> <패키지이름>
    conda remove --name <가상환경이름> <패키지이름>

  # 가상환경 삭제
    conda env remove -n <가상환경이름>
    conda env remove --name <가상환경이름>

  # 현재 활성화된 가상환경에 패키지 설지
    conda install <패키지이름>

  # 특정 가상환경에 패키지 설치
    conda install -n <가상환경이름> <패키지이름>
    conda install --name <가상환경이름> <패키지이름>

  # 특정 가상 환경에 패키지를 특정 버전으로 패키지 설치
    conda install -n  <가상환경이름> <패키지이름>==버전
    conda install --name  <가상환경이름> <패키지이름>==버전

  # 가상환경 활성화
    activate <가상환경이름>

  # 가상환경 비활성화
    conda deactivate
