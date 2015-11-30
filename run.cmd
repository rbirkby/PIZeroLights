scp lights.py pi@192.168.2.104:
git commit -am "Update script"
git push
ssh -t pi@192.168.2.104 python lights.py
 