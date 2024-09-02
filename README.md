# ros2-tutorial
## 1. VcXsrv Windows X Server 설치하기
1. Docker에서 사용하는 Linux는 화면을 출력하기 위해서는 11이라는 프로토콜을 이용합니다. X11을 Windows에서 사용할 수 있도록 하기 위한 VcXsrv라는 프로그램을 설치하는 과정입니다.
VcXsrv Windows X Server 사이트에 접속 후 설치 프로그램을 다운로드합니다. [VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/) 사이트에 접속 후 설치 프로그램을 다운로드합니다.
2. 다운로드한 설치 프로그램을 더블클릭해서 ‘VcXsrv’ 프로그램을 설치합니다. 
3. Windows 프로그램에서 ‘XLaunch’를 실행합니다.
4. ‘Display settings’ 창에서 ‘Display number’를 0으로 설정하고 ‘다음’ 버튼을 누릅니다.
5. ‘Client startup’ 창에서는 기본 값 그대로 ‘다음’ 버튼을 누릅니다.
6. ‘Extra settings’ 창에서 ‘Disable access control’을 선택 후 ‘다음’ 버튼을 누릅니다.
7. ‘Finish configuration’ 창에서 ‘마침’ 버튼을 누르면 설정이 완료됩니다. ‘Save configuration’ 버튼을 눌러서 설정값을 저장해 놓으면 이후에는 저장된 설정값을 더블 클릭하면 현재 설정으로 ‘VcXsrv’가 실행됩니다.
8. Windows의 ‘작업 표시줄’의 ‘숨겨진 아이콘 표시’를 누르면 ‘XLaunch’ 아이콘을 확인할 수 있습니다.

[참고](https://with-rl.tistory.com/entry/Windows%EC%97%90%EC%84%9C-Docker%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-ROS2-Gazebo-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)