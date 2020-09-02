import subprocess


def run():
    print('AI server is ready for operating.....')
    while True:
        print("AI server have passed the image!!")
        img = '~/Downloads/20200901_164257.jpg'
        outputs = subprocess.check_output("cd ~/darknet; ./darknet detect cfg/yolov3.cfg yolov3.weights "+img, stderr=subprocess.STDOUT, shell=True)
        outputs = outputs.decode('utf-8').split('\n')[110:]

        objs = []               
        for output in outputs:
            objs.append(output.split(':')[0])

        onoff = False
        for obj in objs:        #인식한 사물중 사람이 있는지 확인
            if obj == 'person':
                onoff = True
                break

        print(onoff, end='\n')


if __name__ == '__main__':
    run()