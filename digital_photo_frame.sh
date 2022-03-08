sudo mount //192.168.3.8/Public /mnt/nas -o "user=ユーザー名,password=パスワード"
until feh -Y -x -q -D 5 -F -z -r -d -e NotoSansCJK-Regular.ttc/12 -C /usr/share/fonts/opentype/noto /mnt/nas/Pictures/ true; do : ; done &
/home/pi/bin/display_output_switch.py &