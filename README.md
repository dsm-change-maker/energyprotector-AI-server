# 에너지 지킴이 AI-Server

에너지 지킴이 프로젝트에서 라즈베리파이에 들어갈 사람을 인식하는 프로그램입니다.



## 환경 설정

라즈베리파이에서 실행하려면 환경 설정 작업이 필요합니다

```
# darknet 프레임워크를 git을 통해 clone
$ git clone https://github.com/pjreddie/darknet
$ cd darknet
$ make

# 미리 학습된 가중치를 다운
$ wget https://pjreddie.com/media/files/yolov3.weights

# coco.data 파일에서 names 수정
$ cd darknet/cfg
$ vi coco.data
```



