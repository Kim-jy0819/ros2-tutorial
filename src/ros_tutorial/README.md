# ros tutorial 실습
여러 개의 node를 한꺼번에 실행할 수 있게 Package로 만듭니다. 

- python으로 ros_tutorial 패키지 생성
```
ros2 pkg create --build-type ament_python ros_tutorial
```

- setup.py에 ros_tutorial 하위에 launch 패키지가 인식되도록 리스트에 값을 추가합니다. turtlesim.launch.py도 생성합니다. 이후 root directory에서 build합니다. --symlink를 사용하면 파일을 복사하지 않고 링크를 참고하기 때문에 파일 변경 시 유리합니다.
```
colcon build --symlink-install
```

- build, install, log 파일이 생성됩니다. 이후 ros2가 ros_tutorial 패키지를 launch 할 수 있게 setup shell을 실행합니다.
```
source install/setup.zsh
```

- turtlesim_node와 rqt_graph를 동시에 실행합니다.
```
ros2 launch ros_tutorial turtlesim.launch.py
```